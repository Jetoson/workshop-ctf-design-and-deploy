#!/usr/bin/env python3
"""
Solver for the "Secret Decoder Ring" reverse engineering challenge.

The binary contains an encoded flag in the .data section as `encoded_flag[]`.
The encoding scheme is: encoded[i] = (flag[i] ^ 0x42) + i
To decode: flag[i] = (encoded[i] - i) ^ 0x42

This solver:
1. Uses objdump to find the encoded_flag symbol address and size
2. Reads the raw bytes from the binary's .data section
3. Reverses the encoding to recover the flag
"""

import subprocess
import re
import sys

BINARY = './decoder_ring'
XOR_KEY = 0x42


def get_symbol_info(symbol):
    """Get address and size of a symbol from the binary's symbol table."""
    try:
        output = subprocess.check_output(['objdump', '-t', BINARY]).decode()

        # Use the exact format from objdump -t output:
        # addr g     O .data\tsize              symbol_name
        # Example: 0000000000004040 g     O .data	000000000000001c              encoded_flag
        for line in output.splitlines():
            if symbol in line and '.data' in line and ' O ' in line:
                parts = line.split()
                addr = int(parts[0], 16)
                # The size field comes after .data (which contains a tab)
                # Find the size by looking for the hex value after .data
                data_idx = line.index('.data')
                after_data = line[data_idx + 5:].strip()
                size_str = after_data.split()[0]
                size = int(size_str, 16)
                print(f"  Symbol '{symbol}': addr=0x{addr:x}, size={size}")
                return addr, size
    except Exception as e:
        print(f"Error getting symbol {symbol}: {e}")
    return None, None


def get_data_section_info():
    """Get the VMA and file offset of the .data section."""
    try:
        output = subprocess.check_output(['objdump', '-h', BINARY]).decode()
        for line in output.splitlines():
            parts = line.split()
            if len(parts) >= 7 and '.data' in parts:
                idx = parts.index('.data')
                size = int(parts[idx + 1], 16)
                vma = int(parts[idx + 2], 16)
                file_offset = int(parts[idx + 4], 16)
                return vma, file_offset
    except Exception as e:
        print(f"Error getting .data section: {e}")
    return None, None


def read_bytes_from_binary(symbol_addr, symbol_size, data_vma, data_offset):
    """Read raw bytes from the binary file at the symbol's location."""
    offset_in_section = symbol_addr - data_vma
    file_pos = data_offset + offset_in_section

    print(f"  Reading {symbol_size} bytes at file offset 0x{file_pos:x}")

    with open(BINARY, 'rb') as f:
        f.seek(file_pos)
        return f.read(symbol_size)


def decode_flag(encoded_bytes):
    """Reverse the encoding: flag[i] = (encoded[i] - i) ^ XOR_KEY"""
    flag = bytearray()
    for i, b in enumerate(encoded_bytes):
        decoded = ((b - i) & 0xFF) ^ XOR_KEY
        flag.append(decoded)
    return flag.decode('utf-8', errors='replace')


def main():
    print("Solving Secret Decoder Ring challenge...")
    print(f"Binary: {BINARY}")
    print(f"XOR Key: 0x{XOR_KEY:02x}")
    print()

    # Step 1: Find encoded_flag symbol
    print("[Step 1] Finding encoded_flag symbol...")
    addr, size = get_symbol_info('encoded_flag')
    if addr is None:
        print("Could not find 'encoded_flag' symbol. Is this the right binary?")
        return

    # Step 2: Get .data section info
    print("[Step 2] Parsing .data section header...")
    data_vma, data_offset = get_data_section_info()
    if data_vma is None:
        print("Could not parse .data section.")
        return
    print(f"  .data VMA=0x{data_vma:x}, file_offset=0x{data_offset:x}")

    # Step 3: Read encoded bytes
    print("[Step 3] Extracting encoded flag bytes...")
    encoded = read_bytes_from_binary(addr, size, data_vma, data_offset)
    print(f"  Encoded: {' '.join(f'{b:02x}' for b in encoded)}")

    # Step 4: Decode
    print("[Step 4] Decoding flag...")
    flag = decode_flag(encoded)
    print(f"\n[+] Flag: {flag}")


if __name__ == '__main__':
    main()
