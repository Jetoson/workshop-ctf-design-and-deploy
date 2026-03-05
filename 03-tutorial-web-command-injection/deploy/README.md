# Deploy

## Build and Run

```console
# Build the image (from the parent directory context)
docker build -t web-cmd-injection -f Dockerfile ..

# Run the container
docker run -d --rm -p 8080:80 --name web-cmd-injection-container web-cmd-injection
```

The challenge will be available at `http://localhost:8080`.
