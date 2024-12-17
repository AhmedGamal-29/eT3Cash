
#!/bin/sh

echo "Applying NGINX configuration..."
kubectl apply -f ./k8s/nginx/persistent-volume.yml
kubectl apply -f ./k8s/nginx/persistent-volume-claim.yml
kubectl apply -f ./k8s/nginx/persistent-volume-static.yml
kubectl apply -f ./k8s/nginx/persistent-volume-claim-static.yml
kubectl delete --ignore-not-found -f ./k8s/nginx/deployment.yml
kubectl apply -f ./k8s/nginx/deployment.yml
kubectl apply -f ./k8s/nginx/service.yml

echo "Applying application configuration..."
kubectl apply -f ./k8s/app/persistent-volume.yml
kubectl apply -f ./k8s/app/persistent-volume-claim.yml
kubectl delete --ignore-not-found -f ./k8s/app/deployment.yml
kubectl apply -f ./k8s/app/deployment.yml
kubectl apply -f ./k8s/app/service.yml
kubectl apply -f ./k8s/app/ingress.yml

echo "Applying Celery worker configuration..."
kubectl delete --ignore-not-found -f ./k8s/celery/deployment-worker.yml
kubectl apply -f ./k8s/celery/deployment-worker.yml

kubectl delete --ignore-not-found -f ./k8s/celery/deployment-beat.yml
kubectl apply -f ./k8s/celery/deployment-beat.yml



echo "Deployment process completed!"

