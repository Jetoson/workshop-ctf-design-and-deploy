# Solve

## Build Solver

```console
docker build -t leaky-library-solver .
```

## Run Solver

Against local deployment:

```console
# Using host networking (Linux)
docker run --rm --network host leaky-library-solver python3 exploit.py http://127.0.0.1:8081

# Or using host.docker.internal (Mac/Windows)
docker run --rm leaky-library-solver python3 exploit.py http://host.docker.internal:8081
```

Against a remote target:

```console
# Replace with actual target URL
docker run --rm leaky-library-solver python3 exploit.py http://TARGET_IP:PORT
```
