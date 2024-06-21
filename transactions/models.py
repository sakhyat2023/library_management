from django.db import models
from accounts.models import UserBalanceAccount
from books.models import BooksModel
from .constants import transactions_type


# Create your models here.
class TransactionsModel(models.Model):
    account = models.ForeignKey(
        UserBalanceAccount, on_delete=models.CASCADE, related_name="transactions"
    )
    amount = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    balance_after_purchase = models.DecimalField(
        decimal_places=2, max_digits=12, null=True
    )
    transactions_type = models.IntegerField(choices=transactions_type, null=True, blank=True)
    return_book = models.BooleanField(default=False)
    book = models.CharField(max_length=100, default="")
    book_id = models.IntegerField(default=1)
    timestamps = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.account)
    
