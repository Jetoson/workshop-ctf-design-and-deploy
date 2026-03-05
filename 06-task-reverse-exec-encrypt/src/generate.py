import os
import random
import sys
import subprocess
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def generate_challenge():
    flag_path = '../flag'
    if not os.path.exists(flag_path):
        print("Flag file not found")
        sys.exit(1)

    with open(flag_path, 'rb') as f:
        flag = f.read().strip()

    key = os.urandom(16)
    iv = os.urandom(16)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(flag, AES.block_size))

    c_code = f"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>

// Encrypted flag
unsigned char encrypted_flag[] = {{ {', '.join(hex(x) for x in ciphertext)} }};
unsigned char iv[] = {{ {', '.join(hex(x) for x in iv)} }};

// This function contains the key hidden in plain sight!
void secret_function() {{
    // The key is initialized here, putting it in the .text section as instructions
    unsigned char key[16];
    key[0] = {hex(key[0])};
    key[1] = {hex(key[1])};
    key[2] = {hex(key[2])};
    key[3] = {hex(key[3])};
    key[4] = {hex(key[4])};
    key[5] = {hex(key[5])};
    key[6] = {hex(key[6])};
    key[7] = {hex(key[7])};
    key[8] = {hex(key[8])};
    key[9] = {hex(key[9])};
    key[10] = {hex(key[10])};
    key[11] = {hex(key[11])};
    key[12] = {hex(key[12])};
    key[13] = {hex(key[13])};
    key[14] = {hex(key[14])};
    key[15] = {hex(key[15])};

    printf("This function does nothing useful... or does it?\\n");
    
    // Maybe some dummy operation to prevent optimization
    for(int i=0; i<16; i++) {{
        key[i] ^= 0xAA;
    }}
}}

int main() {{
    printf("I am a secure binary. My secrets are safe.\\n");
    secret_function();
    return 0;
}}
"""

    with open('challenge.c', 'w') as f:
        f.write(c_code)

    # Compile the challenge
    print("Compiling challenge...")
    subprocess.check_call(['gcc', '-o', 'plain_sight', 'challenge.c'])
    print("Compilation successful.")

    # Save key and IV for solver verification if needed (or just rely on the binary)
    with open('solution_info.txt', 'w') as f:
        f.write(f"Key: {key.hex()}\\n")
        f.write(f"IV: {iv.hex()}\\n")

if __name__ == "__main__":
    generate_challenge()
