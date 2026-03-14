FROM alpine:latest
RUN apk update && apk add zip
WORKDIR /publish
COPY decoder_ring .
RUN zip decoder_ring.zip decoder_ring
CMD ["cat", "decoder_ring.zip"]
