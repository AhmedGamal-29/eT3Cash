BACKEND_IMAGE="docker.et3.co/internship2024.et3cash-backend:latest"

echo "Building backend Docker image..."
docker build -t $BACKEND_IMAGE ./backend

echo "Pushing backend Docker image to the registry..."
docker push $BACKEND_IMAGE
