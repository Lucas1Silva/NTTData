from django.db.models import Value

from models.BankAccount import BankAccount


class WithdrawlService:
    def __init__(self,user):
        self.user = user
        self.account = BankAccount.objects.get(user=user)

    def withdraw(self,amount):
        if amount > self.account.balance:
            raise ValueError('Insufficient funds')
        if amount > self.account.daily_withdrawal_count >= 3:
            raise ValueError('Withdrawal amount exceeds daily limitd')
        if self.account.daily_withdrawal_count >= 3:
            raise ValueError('Maximum daily withdrawal limit reached')
        self.account.balance -= amount
        self.account.daily_withdrawal_count += 1
        self.account.save()

