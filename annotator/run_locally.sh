#!/bin/bash

# Ensure the script exits if any command fails
set -e

# Enable Docker BuildKit
export DOCKER_BUILDKIT=1

# Define the .env.local file
ENV_FILE=".env.local"

# Function to write secrets to individual files
write_secret() {
  local key=$1
  local value=$2
  echo -n "$value" > "secrets/$key"
}

# Read .env.local file and write each secret to its own file
mkdir -p secrets
while IFS='=' read -r key value; do
  # Skip comments and empty lines
  [[ "$key" =~ ^#.*$ ]] && continue
  [[ -z "$key" ]] && continue

  # Write the secret to its file
  write_secret "$key" "$value"
done < $ENV_FILE

# Run docker-compose
docker compose up -d

# Remove the secrets folder
rm -rf secrets

echo "Docker containers are up and secrets folder has been removed."
