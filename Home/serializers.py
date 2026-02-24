from rest_framework import serializers
from .models import *

class TransactionCreateSerializer(serializers.ModelSerializer):

    account_number = serializers.CharField(
        max_length=20,
        allow_blank=False,
        required=True
    )

    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ['transaction_id']
        
class TransactionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'transaction_id',
            'amount',
            'beneficiary_name',
            'status',
            'created_at',
        ]
class TransactionDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Transaction
        fields = [
            'transaction_id',
            'user',
            'amount',
            'account_number',
            'ifsc_code',
            'beneficiary_name',
            'status',
            'created_at',
            'updated_at',
        ]
class AdminTransactionActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'status',
            'admin_remark',
        ]

    def validate_status(self, value):
        if value not in [
            Transaction.STATUS_APPROVED,
            Transaction.STATUS_REJECTED
        ]:
            raise serializers.ValidationError(
                "Admin can only approve or reject transactions."
            )
        return value
        

