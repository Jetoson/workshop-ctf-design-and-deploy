#!/usr/bin/env python3
"""
Generator for the "Secret Decoder Ring" reverse engineering challenge.

Reads the flag, encodes each byte using XOR + positional addition,
generates a C source file with the encoded data, and compiles it.

Encoding: encoded[i] = (flag[i] ^ XOR_KEY) + i
Decoding: flag[i] = (encoded[i] - i) ^ XOR_KEY
"""

import os
import sys
import subprocess

XOR_KEY = 0x42

def generate_challenge():
    flag_path = '../flag'
    if not os.path.exists(flag_path):
        flag_path = '/flag'
    if not os.path.exists(flag_path):
        print("Flag file not found")
        sys.exit(1)

    with open(flag_path, 'rb') as f:
        flag = f.read().strip()

    print(f"Flag length: {len(flag)} bytes")

    # Encode the flag: encoded[i] = (flag[i] ^ XOR_KEY) + i
    encoded = []
    for i, b in enumerate(flag):
        encoded.append((b ^ XOR_KEY) + i)

    # Generate C source code
    encoded_hex = ', '.join(f'0x{b:02x}' for b in encoded)

    c_code = f"""#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// The encoded flag data — can you decode it?
unsigned char encoded_flag[] = {{ {encoded_hex} }};
unsigned int flag_len = {len(flag)};

// The XOR key used for encoding
unsigned char xor_key = 0x{XOR_KEY:02x};

void check_password(const char *input) {{
    printf("Checking password: \\"%s\\"\\n", input);

    // This is a fake check — the real secret is in the data above!
    if (strlen(input) == flag_len) {{
        printf("Interesting length... but that's not enough!\\n");
    }} else {{
        printf("Not even close!\\n");
    }}
}}

int main(int argc, char *argv[]) {{
    printf("==========================================\\n");
    printf("     SECRET DECODER RING v2.0              \\n");
    printf("==========================================\\n");
    printf("\\n");
    printf("This program guards a very important secret.\\n");
    printf("Can you figure out what it is?\\n");
    printf("\\n");
    printf("Hint: The secret is encoded right here in\\n");
    printf("      this binary. Look carefully...\\n");
    printf("\\n");

    if (argc > 1) {{
        check_password(argv[1]);
    }} else {{
        printf("Usage: %s <password>\\n", argv[0]);
        printf("\\n");
        printf("Try to find the hidden secret!\\n");
    }}

    return 0;
}}
"""

    with open('challenge.c', 'w') as f:
        f.write(c_code)

    # Compile the challenge
    print("Compiling challenge...")
    subprocess.check_call([
        'gcc', '-O0', '-no-pie', '-o', 'decoder_ring', 'challenge.c'
    ])
    print("Compilation successful: decoder_ring")

    # Save solution info for verification
    with open('solution_info.txt', 'w') as f:
        f.write(f"XOR Key: 0x{XOR_KEY:02x}\\n")
        f.write(f"Encoding: encoded[i] = (flag[i] ^ 0x{XOR_KEY:02x}) + i\\n")
        f.write(f"Decoding: flag[i] = (encoded[i] - i) ^ 0x{XOR_KEY:02x}\\n")
        f.write(f"Flag: {flag.decode()}\\n")

if __name__ == "__main__":
    generate_challenge()
