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
        response = self.client.get('/expenses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], "Test Expense 1")
        self.assertEqual(response.data['amount'], "10.00")
        self.assertEqual(response.data['category'], "Food")
    
    def test_expense_creation(self):
        response = self.client.post('/api/expenses/', {
            'name': "Test Expense 4",
            'amount': "40.00",
            'category': "Utilities",
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Expense.objects.count(), 4)

    def test_expense_update(self):
        response = self.client.put('/api/expenses/1/', {
            'name': "Updated Expense 1",
            'amount': "15.00",
            'category': "Food",
        })
        self.assertEqual(response.status_code, 200)
        updated_expense = Expense.objects.get(id=1)
        self.assertEqual(updated_expense.name, "Updated Expense 1")
        self.assertEqual(updated_expense.amount, Decimal("15.00"))

    def test_expense_deletion(self):
        response = self.client.delete('/api/expenses/1/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Expense.objects.count(), 2)

        

    def Teardown(self):
        self.expense1.delete()
        self.expense2.delete()
        self.expense3.delete()
