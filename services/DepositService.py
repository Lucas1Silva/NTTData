from models.BankAccount import BankAccount


class DepositService:
    def __init__(self, user):
        self.user = user
        self.account = BankAccount.objects.get(user=user)


def deposit(self,amount):
    if amount > 0:
        self.account.balance += amount
        self.account.save()