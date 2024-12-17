#!/bin/sh

# Navigate to the frontend directory
cd ../frontend

# Install dependencies
npm install

# Build the application
npm run build

# Build the Docker image
docker build -t docker.et3.co/smart-wallet.front:latest .

# Push the Docker image to the registry
docker push docker.et3.co/smart-wallet.front:latest

