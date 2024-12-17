import pandas as pd
from django.core.management.base import BaseCommand
from myapp.models import DimCustomer

class Command(BaseCommand):
    help = 'Load data from CSV file into DimCustomer table'

    def handle(self, *args, **options):
        file_path = 'data/DimCustomer.csv'  # Path to CSV
        data = pd.read_csv(file_path)
        for _, row in data.iterrows():
            DimCustomer.objects.update_or_create(
                customer_id=row['customer_id'],
                defaults={
                    'username': row['username'],
                    'customer_name': row['customer_name'],
                    'email': row['email'],
                    'phone_number': row['phone_number'],
                    'created_at': row['created_at']
                }
            )
        self.stdout.write(self.style.SUCCESS('Successfully loaded DimCustomer data'))
