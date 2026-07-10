from django.contrib import admin

# Register your models here.
from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'timestamp', 'category')
    list_display_links = ('name', 'amount', 'timestamp', 'category')
    list_filter = ('category', 'timestamp')
    search_fields = ('name', 'amount', 'timestamp', 'category')
