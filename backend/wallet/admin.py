from django.contrib import admin
from .models import Wallet, Transaction, CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['wallet', 'transaction_type', 'amount', 'date', 'recipient']


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    list_display = ['username', 'email', 'phone_number']

    fieldsets = (
        (None, {'fields': ('username', 'email', 'phone_number')}),
    )

    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'phone_number', 'password1', 'password2')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)