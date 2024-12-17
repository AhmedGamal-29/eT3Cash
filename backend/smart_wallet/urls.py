from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from wallet.views import CheckBalanceView, CashInView, CashOutView, TransferView, DonateView, InvestView, TransactionHistoryView
from wallet.views import UserRegisterView, UserLoginView, APIListView, InvestmentMarketView
from wallet import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', APIListView.as_view(), name='api_list'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/check-balance/', CheckBalanceView.as_view(), name='check_balance_api'),
    path('api/cash-in/', CashInView.as_view(), name='cash_in_api'),
    path('api/cash-out/', CashOutView.as_view(), name='cash_out_api'),
    path('api/transfer/', TransferView.as_view(), name='transfer_api'),
    path('api/donate/', DonateView.as_view(), name='donate_api'),
    path('api/invest/', InvestView.as_view(), name='invest_api'),
    path('api/transactions/', TransactionHistoryView.as_view(), name='transactions_api'),
    path('api/register/', UserRegisterView.as_view(), name='register_api'),
    path('api/login/', UserLoginView.as_view(), name='login_api'),
    path('api/market-data/', InvestmentMarketView.as_view(), name='market_data_api'),
]
