# Deploy

## Build and Run

```console
# Build the image (from the parent directory context)
docker build -t leaky-library -f Dockerfile ..

# Run the container
docker run -d --rm -p 8081:5000 --name leaky-library-container leaky-library
```

The challenge will be available at `http://localhost:8081`.

## Stopping the Container

```console
docker stop leaky-library-container
```
