# Find the container that is using port 8000
CONTAINER_ID=$(docker ps --filter "publish=8000" -q)

# If a container is found, stop it
if [ ! -z "$CONTAINER_ID" ]; then
    docker stop $CONTAINER_ID
fi

# Define variables
DOCKERHUB_USER="shinkhan"
DOCKERHUB_PASS="WXCVBN1nbvcxw2,"
IMAGE_NAME="da_python_p13_oc-lettings-site"
TAG=$(git rev-parse --short HEAD)  # Use the short commit hash as the tag

# Set environment variables
export SECRET_KEY="fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s"
export SENTRY_DSN="https://879b66038fc86c0c47dbfba9c17b797d@o4506827891802112.ingest.sentry.io/4506858619535360"

# Build the Docker image
docker build -t $DOCKERHUB_USER/$IMAGE_NAME:$TAG .

# Login to Docker Hub
echo "$DOCKERHUB_PASS" | docker login -u "$DOCKERHUB_USER" --password-stdin

# Push the Docker image to Docker Hub
docker push $DOCKERHUB_USER/$IMAGE_NAME:$TAG

# Pull the Docker image from Docker Hub
docker pull $DOCKERHUB_USER/$IMAGE_NAME:$TAG

# Run the Docker image locally
docker run -e SECRET_KEY=$SECRET_KEY -e SENTRY_DSN=$SENTRY_DSN -p 8000:8000 $DOCKERHUB_USER/$IMAGE_NAME:$TAG