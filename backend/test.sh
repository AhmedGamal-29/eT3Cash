
#!/bin/sh
NETWORK_NAME="et3cash-test-network"
docker network create $NETWORK_NAME

echo "Running Django tests in the Docker container..."
docker run --network=$NETWORK_NAME --rm \
    -e DJANGO_SETTINGS_MODULE=smart_wallet.settings \
    -v "$(pwd):/app" \
    python:3.9 \
    sh -c "pip install -r /app/requirements.txt && cd /app && python3 manage.py test"

# Clean up
docker network rm $NETWORK_NAME

echo "Test execution completed!"

