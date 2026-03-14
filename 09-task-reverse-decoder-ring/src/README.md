# Source / Generator

This directory contains the source code generator and build instructions for the "Secret Decoder Ring" challenge.

## Building

To generate the challenge binary in a reproducible environment (Docker), follow these steps.

1. **Build the Generator Image**

   ```console
   docker build -t decoder-ring-gen .
   ```

2. **Generate and Compile the Binary**

   Run the container, mounting the current directory to `/src` and the flag file to `/flag`.

   ```console
   docker run --rm -v "$(pwd):/src" -v "$(pwd)/../flag:/flag" decoder-ring-gen
   ```

   This command will:

   1. Read the `../flag` file.
   1. Generate `challenge.c` with the encoded flag stored as a global byte array.
   1. Compile `challenge.c` to produce the `decoder_ring` executable.
   1. Save debug info to `solution_info.txt`.

## Post-Build

After building, copy the binary to the `publish/` and `solve/` directories:

```console
cp decoder_ring ../publish/
cp decoder_ring ../solve/
```

## Clean

To clean up build artifacts:

```console
rm decoder_ring challenge.c solution_info.txt
```
