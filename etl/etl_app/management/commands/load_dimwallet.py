import pandas as pd
from django.core.management.base import BaseCommand
from myapp.models import DimWallet, DimCustomer

class Command(BaseCommand):
    help = 'Load data from CSV file into DimWallet table'

    def handle(self, *args, **options):
        file_path = 'data/DimWallet.csv'
        data = pd.read_csv(file_path)
        for _, row in data.iterrows():
            customer = DimCustomer.objects.get(customer_id=row['customer_id'])
            DimWallet.objects.update_or_create(
                wallet_id=row['wallet_id'],
                defaults={
                    'customer': customer,
                    'balance': row['balance'],
                    'created_at': row['created_at']
                }
            )
        self.stdout.write(self.style.SUCCESS('Successfully loaded DimWallet data'))
