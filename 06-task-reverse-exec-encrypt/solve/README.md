# Solve

This directory contains the solution script and a containerized environment to run it.

## Prerequisites

1.  **Build the Solver Image**

    ```console
    docker build -t challenge-solver .
    ```

2.  Ensure you have the binary in this directory (or in `../src/plain_sight`). The solver expects the binary to be mounted at `/app/plain_sight`.

    ```console
    cp ../src/plain_sight .
    ```

## Running the Solution

This runs the solver script `solve.py` against the binary.

```console
docker run --rm -v "$(pwd)/plain_sight:/app/plain_sight" challenge-solver
```

The output should be:
```
Solving...
Key: ...
Flag: D4S_CTF{hidden_in_plain_sight}
```

## Clean

To remove the binary:

```console
rm plain_sight
```
