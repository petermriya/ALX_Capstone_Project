from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Sum
from .models import Expense
from .forms import ExpenseForm


@login_required
def expense_list(request):
    """List expenses only for the logged-in user."""
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})


@login_required
def add_expense(request):
    """Add a new expense linked to the logged-in user."""
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user  # attach logged-in user
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})


@login_required
def delete_expense(request, pk):
    """Allow users to delete only their own expenses."""
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    expense.delete()
    return redirect('expense_list')


@login_required
def monthly_summary(request):
    """Show total expenses for the current month."""
    today = timezone.now()
    total = Expense.objects.filter(
        user=request.user,
        date__year=today.year,
        date__month=today.month
    ).aggregate(total=Sum('amount'))['total'] or 0

    return render(request, 'expenses/monthly_summary.html', {'total': total})
