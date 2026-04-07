from .models import Transaction
from django.db.models import Sum
def calculate_summary(user):
    if user.role == 'ADMIN':
        transactions = Transaction.objects.all()
    else:
        transactions = Transaction.objects.filter(user=user)
    income = transactions.filter(type='INCOME').aggregate(total=Sum('amount'))['total'] or 0
    expense = transactions.filter(type='EXPENSE').aggregate(total=Sum('amount'))['total'] or 0
    return {
        "total_income": income,
        "total_expense": expense,
        "balance": income - expense
    }