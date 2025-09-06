from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('groceries', 'Groceries'),
        ('transport', 'Transport'),
        ('rent', 'Rent'),
        ('entertainment', 'Entertainment'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expenses")
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.title} - {self.amount}"

    @staticmethod
    def monthly_total(user, year, month):
        """Calculate total expenses for a given user, year, and month."""
        return Expense.objects.filter(
            user=user,
            date__year=year,
            date__month=month
        ).aggregate(total=models.Sum("amount"))["total"] or 0