FROM alpine:latest
RUN apk add --no-cache zip
WORKDIR /data
CMD ["zip", "-r", "stack-smash-surprise.zip", ".", "-x", "Dockerfile", "-x", "README.md"]
