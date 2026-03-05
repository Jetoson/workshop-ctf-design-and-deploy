# Solve

This directory contains the solution script and a containerized environment to run it.

## Prerequisites

1.  **Build the Solver Image**

    ```console
    docker build -t piece-of-pie-solver .
    ```

1.  Ensure you have the binary in `../publish/piece_of_pie` (for local solving).

## Running the Solution

You can run the solution in three modes.

### 1. Local Solve (inside container)

This runs the exploit against the binary directly inside the solver container.
We mount the current directory (for `exploit.py`) and the `../publish` directory (for `piece_of_pie`).

```console
docker run --rm -it \
    -v "$(pwd):/solve" \
    -v "$(pwd)/../publish:/publish" \
    piece-of-pie-solver \
    python3 exploit.py
```

### 2. Solve against Local Deployment

This runs the exploit against the challenge service running on your host machine (e.g., started via `docker run` in the `deploy/` directory). It connects to `127.0.0.1:31500`.

> [!NOTE]
> **For Linux users:** We use `--network host` to allow the container to access `localhost` on the host easily.
> **For Mac/Windows:** You might need to use `host.docker.internal` instead of `127.0.0.1` and remove `--network host`.

```console
docker run --rm -it --network host \
    -v "$(pwd):/solve" \
    -v "$(pwd)/../publish:/publish" \
    piece-of-pie-solver \
    python3 exploit.py REMOTE HOST=127.0.0.1 PORT=31500
```

### 3. Solve against Remote Target

This runs the exploit against a remote IP and port.

```console
# Replace 1.2.3.4 and 31500 with actual target
docker run --rm -it \
    -v "$(pwd):/solve" \
    -v "$(pwd)/../publish:/publish" \
    piece-of-pie-solver \
    python3 exploit.py REMOTE HOST=1.2.3.4 PORT=31500
```
