# Leaky Library

**Leaky Library** is a web security CTF challenge.
The goal is to exploit a path traversal vulnerability in a Flask application to retrieve the flag.

## Requirements

* **Docker**

## Challenge Structure

* **`src/`**: Flask source code and book files.
* **`deploy/`**: Deployment configuration (Dockerfile).
* **`solve/`**: Solution script and Docker environment.

## The Flag

The flag is located at `/flag` inside the container.

## Getting Started

1. Go to `deploy/` to run the challenge.
2. Go to `solve/` to run the exploit.
