## DB setup:

1. Make sure user and database exist, if not, create them according to your .env file

## Annotation process

user1,user2 etc should be appended to the url like this: `http://localhost:8080/?session=user1`


## Run locally
1. Annotation: ./run_locally.sh
2. JSON editing: ./run_json_editing_locally.sh

## TODOs:
1. Make it possible to pass `.env` or `.env.local` as an argument to Dockerfile such that scripts/mkconfig.py gets to know which `.env` to file to work with
2. Make the dockerfiles reusable
3. Make sure to avoid copying .env to Docker container. Use secrets and env vars instead