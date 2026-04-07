from .models import Transaction
from django.db.models import Sum

def get_user_transactions(user, filters=None):
    if user.role == 'ADMIN':
        qs = Transaction.objects.all()
    else:
        qs = Transaction.objects.filter(user=user)

    if filters:
        if filters.get('type'):
            qs = qs.filter(type=filters['type'])
        if filters.get('category'):
            qs = qs.filter(category=filters['category'])
        if filters.get('start_date'):
            qs = qs.filter(date__gte=filters['start_date'])
        if filters.get('end_date'):
            qs = qs.filter(date__lte=filters['end_date'])

    return qs


def calculate_summary(user):
    # Admins get summary of all transactions, users get their own
    if user.role == 'ADMIN':
        qs = Transaction.objects.all()
    else:
        qs = Transaction.objects.filter(user=user)

    income = qs.filter(type='INCOME').aggregate(total=Sum('amount'))['total'] or 0
    expense = qs.filter(type='EXPENSE').aggregate(total=Sum('amount'))['total'] or 0

    return {
        "total_income": income,
        "total_expense": expense,
        "balance": income - expense
    }