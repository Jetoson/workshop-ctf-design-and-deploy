# Source / Generator

This directory contains the source code generator and build instructions for the "Hidden in Plain Sight" challenge.

## Building

To generate the challenge binary in a reproducible environment (Docker), follow these steps.

1. **Build the Generator Image**

   ```console
   docker build -t challenge-generator .
   ```

2. **Generate and Compile the Binary**

   Run the container, mounting the current directory to `/src` and the flag file to `/flag`.

   ```console
   docker run --rm -v "$(pwd):/src" -v "$(pwd)/../flag:/flag" challenge-generator
   ```

   This command will:

   1. Read the `../flag` file.
   1. Generate `challenge.c` with the encrypted flag and key hidden in instructions.
   1. Compile `challenge.c` to produce the `plain_sight` executable.
   1. Save debug info to `solution_info.txt`.

## Post-Build

After building, copy the binary to the `publish/` and `solve/` directories:

```console
cp plain_sight ../publish/
cp plain_sight ../solve/
```

## Clean

To clean up build artifacts:

```console
rm plain_sight challenge.c solution_info.txt
```
