import pandas as pd
from django.core.management.base import BaseCommand
from myapp.models import FactTransactions, DimCustomer, DimWallet

class Command(BaseCommand):
    help = 'Load data from CSV file into FactTransactions table'

    def handle(self, *args, **options):
        file_path = 'data/FactTransactions.csv'
        data = pd.read_csv(file_path)
        for _, row in data.iterrows():
            customer = DimCustomer.objects.get(customer_id=row['customer_id'])
            wallet = DimWallet.objects.get(wallet_id=row['wallet_id'])
            FactTransactions.objects.update_or_create(
                transaction_id=row['transaction_id'],
                defaults={
                    'transaction_date': row['transaction_date'],
                    'customer': customer,
                    'wallet': wallet,
                    'transaction_type': row['transaction_type'],
                    'amount': row['amount']
                }
            )
        self.stdout.write(self.style.SUCCESS('Successfully loaded FactTransactions data'))
