#!/bin/sh

# Remove the existing celerybeat.pid file
rm -rf celerybeat.pid

# Start the Celery Beat scheduler for the smart_wallet project
celery -A smart_wallet beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

