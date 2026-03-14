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
        # Match format: addr flags section size symbol_name
        # e.g.: 0000000000004040 g     O .data	000000000000001e              encoded_flag
        match = re.search(
            rf'([0-9a-f]+)\s+.*?O\s+\.data\s+([0-9a-f]+)\s+{symbol}',
            output
        )
        if match:
            addr = int(match.group(1), 16)
            size = int(match.group(2), 16)
            return addr, size
    except Exception as e:
        print(f"Error getting symbol {symbol}: {e}")
    return None, None

def get_data_section_info():
    """Get the VMA and file offset of the .data section."""
    try:
        output = subprocess.check_output(['objdump', '-h', BINARY]).decode()
        match = re.search(
            r'\.data\s+([0-9a-f]+)\s+([0-9a-f]+)\s+[0-9a-f]+\s+([0-9a-f]+)',
            output
        )
        if match:
            size = int(match.group(1), 16)
            vma = int(match.group(2), 16)
            file_offset = int(match.group(3), 16)
            return vma, file_offset
    except Exception as e:
        print(f"Error getting .data section: {e}")
    return None, None

def read_bytes_from_binary(symbol_addr, symbol_size, data_vma, data_offset):
    """Read raw bytes from the binary file at the symbol's location."""
    offset_in_section = symbol_addr - data_vma
    file_pos = data_offset + offset_in_section

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
    addr, size = get_symbol_info('encoded_flag')
    if addr is None:
        print("Could not find 'encoded_flag' symbol.")
        print("Trying alternative approach with flag_len...")

        # Try to get the flag length from the flag_len symbol
        len_addr, len_size = get_symbol_info('flag_len')
        if len_addr is None:
            print("Could not find symbols. Is this the right binary?")
            return
    else:
        print(f"Found encoded_flag at 0x{addr:x}, size={size} bytes")

    # Step 2: Get .data section info
    data_vma, data_offset = get_data_section_info()
    if data_vma is None:
        print("Could not parse .data section.")
        return
    print(f".data section: VMA=0x{data_vma:x}, file_offset=0x{data_offset:x}")

    # Step 3: Read encoded bytes
    encoded = read_bytes_from_binary(addr, size, data_vma, data_offset)
    print(f"Encoded bytes: {' '.join(f'{b:02x}' for b in encoded)}")

    # Step 4: Decode
    flag = decode_flag(encoded)
    print(f"\nFlag: {flag}")

if __name__ == '__main__':
    main()
