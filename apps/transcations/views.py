from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Transaction
from .serializer import TransactionSerializer
from .services import get_user_transactions

class TransactionViewSet(ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return get_user_transactions(self.request.user, self.request.query_params)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)