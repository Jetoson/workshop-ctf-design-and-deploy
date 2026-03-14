# Build

This directory contains the source code and build instructions for the "Stack Smash Surprise" challenge.

## Building

To build the challenge binary in a reproducible environment (Docker) and have it available locally, follow these steps.

1. **Build the Builder Image**

   ```console
   docker build -t stack-smash-builder .
   ```

2. **Compile the Binary**

   Run the container, mounting the current directory to `/build` so the compiled binary is written back to your host machine.

   ```console
   docker run --rm -v "$(pwd):/build" stack-smash-builder make
   ```

   This command will produce the `stack_smash` executable in the current directory.

## Post-Build

After building, you typically want to distribute the binary, loader and libc to the `publish/` directory:

```console
cp stack_smash ld-linux-x86-64.so.2 libc.so.6 ../publish/
```

## Clean

To clean up build artifacts:

```console
# Using Docker (recommended)
docker run --rm -v "$(pwd):/build" stack-smash-builder make clean
```
