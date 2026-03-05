# Hidden in Plain Sight

**Hidden in Plain Sight** is a reverse engineering CTF challenge.
The goal is to analyze an ELF binary to recover a hidden flag that is encrypted within the file.

## Requirements

The only requirement to run, build, deploy, and solve this challenge is **Docker**. No other tools (like GCC, Python) are required on your host machine.

This setup is designed to work seamlessly on:

* **Linux**
* **Windows** (via Docker Desktop)
* **macOS** (via Docker Desktop)

## Challenge Structure

This repository is organized into three main directories, each serving a specific phase of the challenge lifecycle:

1. **`src/`**:
   * **Purpose**: Contains the generator script (`generate.py`) and the build environment.
   * **Action**: Generates the C source code with the encrypted flag and compiles it into the challenge binary (`plain_sight`).
   * **Output**: The compiled binary.

1. **`publish/`**:
   * **Purpose**: Prepares the challenge artifacts for distribution to players.
   * **Action**: Packages the binary into a zip archive (`plain_sight.zip`).
   * **Output**: A zip file ready to be shared with contestants.

1. **`solve/`**:
   * **Purpose**: Contains the solution script (`solve.py`) and a solver environment.
   * **Action**: Statically analyzes the binary to recover the encryption key and decrypt the flag.

## The Flag

The flag for this challenge is stored in the `flag` file in the root directory.

## Getting Started

To get started with this challenge, follow the instructions in the `README.md` file within each directory, starting with `src/` to generate the binary.
