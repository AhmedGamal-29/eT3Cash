from django.core.management.base import BaseCommand
from etl_app.etl_pipeline.pipeline import run_etl

class Command(BaseCommand):
    help = "Run the ETL pipeline to load data into the database"

    def handle(self, *args, **kwargs):
        run_etl()
        self.stdout.write(self.style.SUCCESS('ETL pipeline executed successfully!'))
