from django.contrib.auth.models import User
from django.db import models

class BankAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE())
    balance = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)
    daily_withdrawal_limit = models.DecimalField(max_digits=10, decimal_places=2, default=500.0)
    daily_withdrawal_count = models.IntegerField(default=0)