# Variables
IMAGE_NAME = funny-fortune-app
DOCKER_USER = $(shell grep DOCKER_USERNAME .env | cut -d '=' -f2)

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run the Docker container
run:
	docker run -p 5000:5000 $(IMAGE_NAME)

# Tag the Docker image for Docker Hub
tag:
	docker tag $(IMAGE_NAME) $(DOCKER_USER)/$(IMAGE_NAME):latest

# Push the Docker image to Docker Hub
push: tag
	docker push $(DOCKER_USER)/$(IMAGE_NAME):latest

# Clean up Docker containers and images
clean:
	docker rm -f $(shell docker ps -aq) || true
	docker rmi -f $(IMAGE_NAME) $(DOCKER_USER)/$(IMAGE_NAME):latest || true

# Load environment variables
env:
	export $$(cat .env | xargs)
