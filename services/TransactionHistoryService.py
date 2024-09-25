from models.BankAccount import BankAccount
from views.views import withdraw


class TransactionHistoryService:
    def __init__(self, user):
        self.user = user
        self.account = BankAccount.objects.get(user=user)

    def get_transactions(self):
        deposits =  self.account.deposit_set.all()
        withdrawals = self.account.withdraw_set.all()
        transactions = [
            {
                'type' : 'Deposit',
                'amount' : deposit.amount,
                'timestamp' : deposit.timestamp.isoformat()
            }
            for deposit in deposits
        ] + [
            {
                'type': 'Withdraw',
                'amount': withdrawl.amount,
                'timestamp': withdrawl.timestamp.isoformat()
            }
            for withdrawl in withdrawals
        ]
        transactions.sort(key=lambda x : x['timestamp'], reverse=True)
        return transactions