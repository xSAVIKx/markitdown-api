#!/bin/bash
# Script to rebuild and restart the MarkItDown container

# Set variables
CONTAINER_NAME="markitdown-api"
IMAGE_NAME="markitdown-api"
PORT="8080"

echo "Rebuilding and restarting MarkItDown container..."

# Check if the container is running and stop it if it is
if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
    echo "Stopping running container..."
    docker stop $CONTAINER_NAME
fi

# Remove the existing container if it exists
if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
    echo "Removing existing container..."
    docker rm $CONTAINER_NAME
fi

# Rebuild the image
echo "Building new Docker image..."
docker build -t $IMAGE_NAME:latest .

# Run the new container
echo "Starting new container..."
docker run -d --name $CONTAINER_NAME -p $PORT:$PORT $IMAGE_NAME

# Check if container started successfully
if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
    echo "Container successfully rebuilt and restarted."
    echo "Service is available at http://localhost:$PORT"
else
    echo "❌ Failed to start the container. Check Docker logs for details."
fi
