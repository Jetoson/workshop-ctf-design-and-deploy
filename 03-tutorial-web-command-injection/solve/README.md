# Solve

## Build Solver

```console
docker build -t web-cmd-injection-solver .
```

## Run Solver

Against local deployment:

```console
# Using host networking (Linux)
docker run --rm --network host web-cmd-injection-solver python3 exploit.py http://127.0.0.1:8080

# Or using host.docker.internal (Mac/Windows)
docker run --rm web-cmd-injection-solver python3 exploit.py http://host.docker.internal:8080
```
