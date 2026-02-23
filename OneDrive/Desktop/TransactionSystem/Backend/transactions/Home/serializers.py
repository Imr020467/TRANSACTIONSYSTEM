from rest_framework import serializers
from .models import *

class TransactionCreateSerializer(serializers.ModelSerializer):
    '''
    @ Imr020467 - no valodation handled 
    - cases 1: account number sent as empty string -> invalid data to db
    - case 2 : account number of 50 chars - db raises 
    ~ same for other user inputs.

    - similar if not sending any field, say account number is missing on request body - db raises
    
    '''
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields=['transaction_id']
        
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
        

