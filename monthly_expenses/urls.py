"""
URL configuration for monthly_expenses project.
"""

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('expenses/', include('expenses.urls')),
    # Redirect root URL to expense list
    path('', lambda request: redirect('expense_list'), name='home'),
]
