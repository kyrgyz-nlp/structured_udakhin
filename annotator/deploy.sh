fly deploy $(cat .env | xargs -n 1 echo --build-secret)
