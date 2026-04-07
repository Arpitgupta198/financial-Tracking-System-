from django.db import models
from django.conf import settings


class Transaction(models.Model):
    INCOME = 'INCOME'
    EXPENSE = 'EXPENSE'

    TYPE_CHOICES = (
        (INCOME, 'Income'),
        (EXPENSE, 'Expense'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='transactions'
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    category = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # 🔥 useful
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.type} - {self.amount}"