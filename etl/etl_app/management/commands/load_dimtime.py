import pandas as pd
from django.core.management.base import BaseCommand
from myapp.models import DimTime

class Command(BaseCommand):
    help = 'Load data from CSV file into DimTime table'

    def handle(self, *args, **options):
        file_path = 'data/DimTime.csv'
        data = pd.read_csv(file_path)
        for _, row in data.iterrows():
            DimTime.objects.update_or_create(
                date_key=row['date_key'],
                defaults={
                    'year': row['year'],
                    'month': row['month'],
                    'day': row['day'],
                    'quarter': row['quarter'],
                    'weekday': row['weekday']
                }
            )
        self.stdout.write(self.style.SUCCESS('Successfully loaded DimTime data'))
