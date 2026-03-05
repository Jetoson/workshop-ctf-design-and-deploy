# Build

This directory contains the source code and build instructions for the "Piece of Pie" challenge.

## Building

To build the challenge binary in a reproducible environment (Docker) and have it available locally, follow these steps.

1.  **Build the Builder Image**

    ```console
    docker build -t piece-of-pie-builder .
    ```

2.  **Compile the Binary**

    Run the container, mounting the current directory to `/build` so the compiled binary is written back to your host machine.

    ```console
    docker run --rm -v "$(pwd):/build" piece-of-pie-builder make
    ```

    This command will produce the `piece_of_pie` executable in the current directory.

## Post-Build

After building, you typically want to distribute the binary, loader and libc to the `publish/` directory:

```console
cp piece_of_pie ld-linux-x86-64.so.2 libc.so.6 ../publish/
```

## Clean

To clean up build artifacts:

```console
# Using Docker (recommended)
docker run --rm -v "$(pwd):/build" piece-of-pie-builder make clean
```
