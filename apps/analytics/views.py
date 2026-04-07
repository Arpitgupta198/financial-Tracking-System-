from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.users.permission import IsAdmin
from apps.transcations.models import Transaction
from apps.users.models import User
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
class AnalyticsView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    def get(self, request):
        total_users = User.objects.count()
        total_transactions = Transaction.objects.count()

        income = Transaction.objects.filter(type='INCOME').aggregate(
            total=Sum('amount')
        )['total'] or 0

        expense = Transaction.objects.filter(type='EXPENSE').aggregate(
            total=Sum('amount')
        )['total'] or 0

        monthly_data = Transaction.objects.annotate(
            month=TruncMonth('date')
        ).values('month', 'type').annotate(
            total=Sum('amount'),
            count=Count('id')
        ).order_by('month')

        return Response({
            "status": True,
            "message": "Analytics fetched successfully",
            "data": {
                "total_users": total_users,
                "total_transactions": total_transactions,
                "total_income": income,
                "total_expense": expense,
                "net_balance": income - expense,
                "monthly_breakdown": list(monthly_data)
            }
        })