from django import forms
from .models import Wallet
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

CustomUser = get_user_model()

class TransactionForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)

class TransferForm(forms.Form):
    recipient = forms.ModelChoiceField(queryset=CustomUser.objects.all(), label='Recipient')
    amount = forms.DecimalField(max_digits=10, decimal_places=2)

class DonationForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)

class InvestForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user