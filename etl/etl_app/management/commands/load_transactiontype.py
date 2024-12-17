import pandas as pd
from django.core.management.base import BaseCommand
from myapp.models import DimTransactionType

class Command(BaseCommand):
    help = 'Load data from CSV file into DimTransactionType table'

    def handle(self, *args, **options):
        file_path = 'data/DimTransactionType.csv'
        data = pd.read_csv(file_path)
        for _, row in data.iterrows():
            DimTransactionType.objects.update_or_create(
                transaction_type_id=row['transaction_type_id'],
                defaults={'transaction_type': row['transaction_type']}
            )
        self.stdout.write(self.style.SUCCESS('Successfully loaded DimTransactionType data'))
