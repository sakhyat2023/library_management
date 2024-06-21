from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from transactions.models import TransactionsModel

# Create your views here.
class UserProfileView(LoginRequiredMixin, ListView):
    template_name = "profile.html"
    model = TransactionsModel
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(transactions_type=2,account=self.request.user.account)
        self.balance = self.request.user.account.balance
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"amount": self.request.user.account})
        return context
    