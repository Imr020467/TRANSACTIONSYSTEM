from django.db import models
from django.contrib.auth.models import User
import uuid
class Transaction(models.Model):
    # Transaction status choices
    STATUS_PENDING = 'PENDING'
    STATUS_APPROVED = 'APPROVED'
    STATUS_REJECTED = 'REJECTED'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_APPROVED, 'Approved'),
        (STATUS_REJECTED, 'Rejected'),
    ]

    # Who initiated the transaction (multi-user support)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='transactions'
    )

    # Unique transaction ID (searchable)
    '''
    @Imr020467 - in case its searchable:
         - db index should be provided
         - concern: uuid4 indexing is un-optimized for any RDBMS, if your data size grows 100k+, you can experience lags on query 
    '''
    transaction_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    # Payment details
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    account_number = models.CharField(
        max_length=20
    )
    ifsc_code = models.CharField(
        max_length=11
    )
    beneficiary_name = models.CharField(
        max_length=100
    )

    # Transaction state
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING
    )

    # Admin decision fields
    admin_remark = models.TextField(
        blank=True,
        null=True
    )

    # Timestamps
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.transaction_id} - {self.status}"
