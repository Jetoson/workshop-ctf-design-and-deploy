# Publish

This directory is responsible for packaging the challenge artifacts for distribution to players.

## Prerequisites

1.  Ensure you have built the challenge binary in the `build/` directory.
1.  Ensure you have copied the built binary and loader and libc to this directory:

    ```console
    cp ../build/stack_smash ../build/ld-linux-x86-64.so.2 ../build/libc.so.6 .
    ```

## Creating Distribution Archive

To create a zip archive (`stack-smash-surprise.zip`) containing the necessary files for players (binary, libraries, etc.):

1.  **Build the Publisher Image**

    ```console
    docker build -t stack-smash-publisher .
    ```

1.  **Generate the Archive**

    Run the container, mounting the current directory to `/data`. The container will zip the contents and write `stack-smash-surprise.zip` back to your local directory.

    ```console
    docker run --rm -v "$(pwd):/data" stack-smash-publisher
    ```

## Clean

To remove the generated archive:

```console
rm stack-smash-surprise.zip
```
