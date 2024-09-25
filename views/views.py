from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from services import DepositService,WithdrawalService,TransactionHistoryService


@login_required
def deposit(request):
    amount = float(request.POST['amount'])
    DepositService.deposit(amount)
    return JsonResponse({'message':'Deposit successful'}, status=200)

@login_required
def withdraw(request):
    amount = float(request.POST['amount'])
    try:
        WithdrawalService(request.user).withdraw(amount)
        return JsonResponse({'message':'Deposit successful'}, status=200)
    except ValueError as e :
        return JsonResponse({'error': str(e)}, status=400)

@login_required
def transaction_history(request):
    transactions = TransactionHistoryService(request.user).get_transactions()
    return JsonResponse({'transactions': transactions}, status=200)