from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Transaction


class TransactionAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()

        # Create user
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )

        # Authenticate
        self.client.login(username="testuser", password="password123")

        self.transaction_data = {
            "amount": "100.00",
            "account_number": "1234567890",
            "ifsc_code": "SBIN0001234",
            "beneficiary_name": "John Doe"
        }

    # Test create transaction
    def test_create_transaction(self):

        response = self.client.post(
            "/api/v1/transactions/",
            self.transaction_data,
            format="json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Transaction.objects.count(), 1)


    # Test list transactions of logged user
    def test_list_transactions(self):

        Transaction.objects.create(
            user=self.user,
            amount="100.00",
            account_number="1234567890",
            ifsc_code="SBIN0001234",
            beneficiary_name="John Doe"
        )

        response = self.client.get("/api/v1/transactions/my/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)


    # Test retrieve transaction detail
    def test_transaction_detail(self):

        transaction = Transaction.objects.create(
            user=self.user,
            amount="100.00",
            account_number="1234567890",
            ifsc_code="SBIN0001234",
            beneficiary_name="John Doe"
        )

        url = f"/api/v1/transactions/{transaction.transaction_id}/"

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["beneficiary_name"], "John Doe")