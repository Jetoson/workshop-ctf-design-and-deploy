FROM alpine:latest
RUN apk update && apk add zip
WORKDIR /publish
COPY plain_sight .
RUN zip plain_sight.zip plain_sight
CMD ["cat", "plain_sight.zip"]
