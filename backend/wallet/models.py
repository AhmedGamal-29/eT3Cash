from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True, blank=False)

class Wallet(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username}'s Wallet"

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('cash_in', 'Cash In'),
        ('cash_out', 'Cash Out'),
        ('transfer', 'Transfer'),
        ('donation', 'Donation'),
        ('investment', 'Investment')
    )

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    recipient = models.ForeignKey(Wallet, on_delete=models.SET_NULL, null=True, blank=True, related_name='received_transactions')

    # New fields for investments
    symbol = models.CharField(max_length=10, null=True, blank=True)  # e.g., "AAPL" for Apple stock
    investment_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Price at the time of investment

    def save(self, *args, **kwargs):
        wallet = self.wallet

        # Process the transaction type
        if self.transaction_type == 'cash_in':
            wallet.balance += self.amount
        elif self.transaction_type == 'cash_out' and wallet.balance >= self.amount:
            wallet.balance -= self.amount
        elif self.transaction_type == 'transfer':
            wallet.balance -= self.amount
            if self.recipient:
                self.recipient.balance += self.amount
                self.recipient.save()
        elif self.transaction_type == 'donation' and wallet.balance >= self.amount:
            wallet.balance -= self.amount
        elif self.transaction_type == 'investment' and wallet.balance >= self.amount:
            wallet.balance -= self.amount
            # Additional logic specific to investments
            # Assuming `symbol` and `investment_price` are set in the view before calling save()

        wallet.save()  # Save the updated balance
        super().save(*args, **kwargs)  # Save the transaction instance

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} - {self.wallet.user.username} - {self.symbol or 'N/A'}"