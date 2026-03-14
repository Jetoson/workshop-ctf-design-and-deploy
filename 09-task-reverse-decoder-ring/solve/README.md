# Solve

This directory contains the solution script and a containerized environment to run it.

## Prerequisites

1.  **Build the Solver Image**

    ```console
    docker build -t decoder-ring-solver .
    ```

2.  Ensure you have the binary in this directory (or in `../src/decoder_ring`). The solver expects the binary to be mounted at `/app/decoder_ring`.

    ```console
    cp ../src/decoder_ring .
    ```

## Running the Solution

This runs the solver script `solve.py` against the binary.

```console
docker run --rm -v "$(pwd)/decoder_ring:/app/decoder_ring" decoder-ring-solver
```

The output should be:
```
Solving Secret Decoder Ring challenge...
Binary: ./decoder_ring
XOR Key: 0x42

Found encoded_flag at 0x..., size=... bytes
.data section: VMA=0x..., file_offset=0x...
Encoded bytes: ...

Flag: CTF{x0r_d3c0d3r_r1ng_m4st3r}
```

## Clean

To remove the binary:

```console
rm decoder_ring
```
