#!/bin/bash

# This script deploys the application using Docker and Kubernetes

echo "Building Docker image..."
docker build -t routeiq:latest .

echo "Applying Kubernetes configurations..."
kubectl apply -f infra/k8s/deployment.yaml
kubectl apply -f infra/k8s/service.yaml

echo "Deployment complete."
