from django.urls import path
from .views import (
    CreateTransactionAPIView,
    UserTransactionListAPIView,
    TransactionDetailAPIView,
    AdminTransactionListAPIView,
    AdminTransactionActionAPIView
)

urlpatterns = [
    # User APIs
    path('transactions/', CreateTransactionAPIView.as_view(), name='create-transaction'),
    path('transactions/my/', UserTransactionListAPIView.as_view(), name='my-transactions'),
    path('transactions/<str:transaction_id>/', TransactionDetailAPIView.as_view(), name='transaction-detail'),
    
    # Admin APIs
    path('admin/transactions/', AdminTransactionListAPIView.as_view(), name='admin-transactions'),
    path('admin/transactions/<str:transaction_id>/', AdminTransactionActionAPIView.as_view(), name='admin-transaction-action'),
]