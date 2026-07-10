from decimal import Decimal

from django.test import TestCase

from .models import Expense


class ExpenseModelTests(TestCase):
    def setUp(self):
        self.expense1 = Expense.objects.create(
            name="Test Expense 1",
            amount=Decimal("10.00"),
            category="Food",
        )
        self.expense2 = Expense.objects.create(
            name="Test Expense 2",
            amount=Decimal("20.00"),
            category="Transport",
        )
        self.expense3 = Expense.objects.create(
            name="Test Expense 3",
            amount=Decimal("30.00"),
            category="Entertainment",
        )
    
    def test_expenses_list(self):
        response = self.client.get('/api/expenses/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

    def test_expense_detail(self):
    
    def Teardown(self):
        self.expense1.delete()
        self.expense2.delete()
        self.expense3.delete()
