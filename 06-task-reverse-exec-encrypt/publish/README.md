# Publish

This directory is responsible for packaging the challenge artifacts for distribution to players.

## Prerequisites

1.  Ensure you have built the challenge binary in the `src/` directory.
2.  Ensure you have copied the built binary to this directory:

    ```console
    cp ../src/plain_sight .
    ```

## Creating Distribution Archive

To create a zip archive (`plain_sight.zip`) containing the necessary files for players (the binary):

1.  **Build the Publisher Image**

    ```console
    docker build -t challenge-publisher .
    ```

2.  **Generate the Archive**

    Run the container. It will output the zip file contents to stdout, so redirect it to a file.

    ```console
    docker run --rm challenge-publisher > plain_sight.zip
    ```

## Clean

To remove the binary and archive:

```console
rm plain_sight plain_sight.zip
```
