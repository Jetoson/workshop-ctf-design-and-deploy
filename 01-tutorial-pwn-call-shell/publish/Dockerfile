FROM alpine:latest
RUN apk add --no-cache zip
WORKDIR /data
CMD ["zip", "-r", "piece-of-pie.zip", ".", "-x", "Dockerfile", "-x", "README.md"]
