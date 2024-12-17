#!/bin/sh

# Run Django setup commands
echo "Running migrations..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate

echo "Collecting static files..."
python3 manage.py collectstatic --noinput

# Ensure superuser is created
echo "Checking for admin user..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@domain.com', 'P@ssw0rd')" | python3 manage.py shell

# Start the application using Gunicorn
echo "Starting Gunicorn server..."
gunicorn --config gunicorn-cfg.py smart_wallet.wsgi
