# Stack Smash Surprise

**Stack Smash Surprise** is a binary exploitation (pwn) CTF challenge.
The goal is to exploit a buffer overflow vulnerability in the provided binary to call a hidden function and retrieve the flag.

## Requirements

The only requirement to run, build, deploy, and solve this challenge is **Docker**. No other tools (like GCC, Make, Python) are required on your host machine.

This setup is designed to work seamlessly on:

* **Linux**
* **Windows** (via Docker Desktop)
* **macOS** (via Docker Desktop)

## Challenge Structure

This repository is organized into four main directories, each serving a specific phase of the challenge lifecycle:

1. **`build/`**:
   * **Purpose**: Contains the source code (`stack_smash.c`) and the build environment.
   * **Action**: Compiles the source code into the challenge binary (`stack_smash`) using a reproducible Docker environment.
   * **Output**: The compiled binary, which is then used by the other directories.

2. **`publish/`**:
   * **Purpose**: Prepares the challenge artifacts for distribution to players.
   * **Action**: Packages the binary and necessary libraries (libc, ld) into a zip archive (`stack-smash-surprise.zip`).
   * **Output**: A zip file ready to be shared with contestants.

3. **`deploy/`**:
   * **Purpose**: Configuration for hosting the challenge.
   * **Action**: Builds a Docker container that runs the vulnerable binary under `xinetd`, exposing it on a network port (default: 31600).
   * **Output**: A running service accessible via network (e.g., `nc localhost 31600`).

4. **`solve/`**:
   * **Purpose**: Contains the solution script (`exploit.py`) and a solver environment.
   * **Action**: Runs the exploit against the binary. Supports three modes:
     * **Local**: Runs the exploit against the binary directly inside a container.
     * **Deploy**: Runs the exploit against a locally deployed challenge container.
     * **Remote**: Runs the exploit against a remote target IP/Port.

## The Flag

The flag for this challenge is stored in the `flag` file in the root directory.

During deployment:

*   The `flag` file is copied into the challenge container at `/home/ctf/flag`.
*   The exploit retrieves the flag by calling the hidden `unlock_vault()` function which reads and prints this file.

## Getting Started

To get started with this challenge, follow the instructions in the `README.md` file within each directory, typically starting with `build/` to generate the binary.
