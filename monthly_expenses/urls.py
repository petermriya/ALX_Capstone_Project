"""
URL configuration for monthly_expenses project.
"""

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


# Temporary home view
def home_view(request):
    return HttpResponse("Welcome to Monthly Expense Tracker")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('expenses/', include('expenses.urls')),
    path('', include('expenses.urls')),
]