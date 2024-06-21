from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, View
from django.urls import reverse_lazy
from .models import TransactionsModel
from .forms import DepositFrom
from books.models import BooksModel


# Create your views here.
class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    model = TransactionsModel
    success_url = reverse_lazy("home")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"account": self.request.user.account})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DepositMoneyView(TransactionCreateMixin):
    template_name = "deposit_form.html"
    form_class = DepositFrom

    def get_initial(self):
        initial = {"transactions_type": 1}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get("amount")
        account = self.request.user.account
        account.balance += amount
        account.save(update_fields=["balance"])
        return super().form_valid(form)


class BorrowBookView(LoginRequiredMixin, View):
    def get(self, request, book_id):
        book = get_object_or_404(BooksModel, id=book_id)
        account = self.request.user.account
        if book.borrowing_price > account.balance:
            messages.warning(self.request, "Insufficient balance to borrow the book")
            return redirect("book_details", book.id)
        account.balance -= book.borrowing_price
        account.save()
        TransactionsModel.objects.create(
            account=account,
            amount=book.borrowing_price,
            balance_after_purchase=account.balance,
            transactions_type=2,
            book=book.title,
            book_id=book.id
        )
        if not book.is_borrow_book:
            book.is_borrow_book = True
        book.save()
        return redirect("profile")


class ReturnBookView(LoginRequiredMixin, View):
    def get(self, request, book_id):
        transaction = get_object_or_404(TransactionsModel, id=book_id)
        user_account = transaction.account
        user_account.balance += transaction.amount
        transaction.account.save()
        transaction.balance_after_purchase = user_account.balance
        transaction.save()
        transaction.delete()
        return redirect("profile")

            
