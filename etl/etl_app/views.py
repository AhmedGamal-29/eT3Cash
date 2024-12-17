from django.shortcuts import render
from django.http import JsonResponse
from .models import DimWallet, FactTransactions
from django.db.models import Sum

def get_money_spent(request):
    total_spent = FactTransactions.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    return JsonResponse({'total_spent': total_spent})

def get_total_savings(request):
    total_savings = DimWallet.objects.aggregate(Sum('balance'))['balance__sum'] or 0
    return JsonResponse({'total_savings': total_savings})

def get_used_services(request):
    transaction_types = FactTransactions.objects.values('transaction_type').distinct()
    return JsonResponse({'used_services': list(transaction_types)})

def get_transactions_count(request):
    transactions_count = FactTransactions.objects.count()
    return JsonResponse({'transactions_count': transactions_count})


def dashboard(request):
    return render(request, 'dashboard.html')
