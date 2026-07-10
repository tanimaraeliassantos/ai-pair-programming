from rest_framework import serializers

from .models import Expense

"""Exposes Expense model fields to the API, allowing for serialization and deserialization of Expense instances."""


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'name', 'amount', 'timestamp', 'category']
