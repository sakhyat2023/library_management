from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserBalanceAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
    account_number = models.IntegerField(unique=True)
    balance = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)
    
    def __str__(self):
        return str(self.account_number)
    
