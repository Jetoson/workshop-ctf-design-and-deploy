# Deploy

This directory contains the deployment configuration for the "Piece of Pie" challenge.
It uses `xinetd` inside a Docker container to serve the challenge.

## Prerequisites

1.  Ensure you have built the challenge binary and artifacts are in the `publish/` directory.
1.  If you haven't run the `publish` steps, verify that `../publish/` contains `piece_of_pie`, `ld-linux-x86-64.so.2`, and `libc.so.6`.

## Building the Image

Build the Docker image. Note that the build context must be the parent directory (`..`) to allow copying files from `publish/` and `deploy/`.

```console
docker build -t piece-of-pie-deploy -f Dockerfile ..
```

## Running the Container

Run the container, exposing port 31500:

```console
docker run -d --rm -p 31500:31337 --name piece-of-pie-container piece-of-pie-deploy
```

The challenge will be accessible at `localhost:31500`.

## Stopping the Container

To stop and remove the container:

```console
docker stop piece-of-pie-container
```
