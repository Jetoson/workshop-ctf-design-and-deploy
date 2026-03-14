# Deploy

This directory contains the deployment configuration for the "Stack Smash Surprise" challenge.
It uses `xinetd` inside a Docker container to serve the challenge.

## Prerequisites

1.  Ensure you have built the challenge binary and artifacts are in the `publish/` directory.
1.  If you haven't run the `publish` steps, verify that `../publish/` contains `stack_smash`, `ld-linux-x86-64.so.2`, and `libc.so.6`.

## Building the Image

Build the Docker image. Note that the build context must be the parent directory (`..`) to allow copying files from `publish/` and `deploy/`.

```console
docker build -t stack-smash-deploy -f Dockerfile ..
```

## Running the Container

Run the container, exposing port 31600:

```console
docker run -d --rm -p 31600:31337 --name stack-smash-container stack-smash-deploy
```

The challenge will be accessible at `localhost:31600`.

## Stopping the Container

To stop and remove the container:

```console
docker stop stack-smash-container
```
