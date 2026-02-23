from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404

from .models import Transaction
from .serializers import *


class CreateTransactionAPIView(generics.CreateAPIView):
    """
    User creates a new fund transfer request (like pressing 'Pay' in Google Pay).
    """
    serializer_class = TransactionCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
 
    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            status=Transaction.STATUS_PENDING
        )


class UserTransactionListAPIView(generics.ListAPIView):
    """
    Returns only the transactions of the logged-in user (Google Pay Activity).
    """
    serializer_class = TransactionListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(
            user=self.request.user
        ).order_by('-created_at')


class TransactionDetailAPIView(generics.RetrieveAPIView):
    """
    Fetch a single transaction by transaction_id for the logged-in user.
    """
    serializer_class = TransactionDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    # @Imr020467 - transaction_id was not indexed on db - will take eternity for rows over 10k 
    lookup_field = 'transaction_id'

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)


class AdminTransactionListAPIView(generics.ListAPIView):
    """
    Admin can view all transactions in the system.
    @Imr020467 - are we looking for separate REST based dashboard for admin ? 
    - else can be shown on django admin portal only

    """
    serializer_class = TransactionListSerializer
    permission_classes = [permissions.IsAdminUser]
    # @Imr020467 - objects.all() queries can break your system - as you are trying to fetch all at once - try pagination
    queryset = Transaction.objects.all().order_by('-created_at')


class AdminTransactionActionAPIView(generics.UpdateAPIView):
    """
    Admin can approve or reject a transaction.
    @Imr020467 - are we looking for separate REST based dashboard for admin ? 
    """
    serializer_class = AdminTransactionActionSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'transaction_id'
    # @Imr020467 - objects.all() queries can break your system - as you are trying to fetch all at once - try pagination
    queryset = Transaction.objects.all()


# Create your views here.
