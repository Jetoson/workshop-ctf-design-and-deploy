import subprocess
import re
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

BINARY = './plain_sight'

def get_symbol_address(symbol):
    try:
        output = subprocess.check_output(['objdump', '-t', BINARY]).decode()
        # Matches: 0000000000004040 g     O .data	0000000000000020              encrypted_flag
        match = re.search(f'([0-9a-f]+) g     O .data\t([0-9a-f]+)              {symbol}', output)
        if match:
            return int(match.group(1), 16), int(match.group(2), 16)
    except Exception as e:
        print(f"Error getting symbol {symbol}: {e}")
    return None, None

def get_bytes_at_address(address, size):
    try:
        sections = subprocess.check_output(['objdump', '-h', BINARY]).decode()
        # Find .data section
        #  .data         00000030  0000000000004040  0000000000004040  00003040  2**5
        match = re.search(r'\.data\s+[0-9a-f]+\s+([0-9a-f]+)\s+[0-9a-f]+\s+([0-9a-f]+)', sections)
        if match:
            vma_start = int(match.group(1), 16)
            file_offset_start = int(match.group(2), 16)

            offset_in_section = address - vma_start
            final_file_offset = file_offset_start + offset_in_section

            with open(BINARY, 'rb') as f:
                f.seek(final_file_offset)
                return f.read(size)
        else:
            print("Could not find .data section header")

    except Exception as e:
        print(f"Error getting bytes: {e}")
    return None

def get_key():
    try:
        output = subprocess.check_output(['objdump', '-d', '-j', '.text', BINARY]).decode()
        lines = output.splitlines()

        in_secret = False
        key_bytes = {}

        for line in lines:
            if '<secret_function>:' in line:
                in_secret = True
                continue
            if in_secret and line.strip() == '': 
                pass
            if in_secret and '<' in line and '>:' in line: 
                break

            if in_secret:
                # Look for: movb   $0xIMM,-0xXX(%rbp)
                match = re.search(r'movb\s+\$0x([0-9a-f]+),-0x([0-9a-f]+)\(%rbp\)', line)
                if match:
                    val = int(match.group(1), 16)
                    # Since the C code initializes key[0], key[1]... in order,
                    # we can just append the values as we find them.
                    key_bytes[len(key_bytes)] = val

        sorted_keys = sorted(key_bytes.keys())
        if len(sorted_keys) != 16:
            print(f"Found partial key: {key_bytes}")
            return None

        final_key = bytearray()
        for k in sorted_keys:
            final_key.append(key_bytes[k])

        return bytes(final_key)

    except Exception as e:
        print(f"Error getting key: {e}")
    return None

def main():
    print("Solving...")

    # 1. Get addresses
    flag_addr, flag_size = get_symbol_address('encrypted_flag')
    iv_addr, iv_size = get_symbol_address('iv')

    if not flag_addr or not iv_addr:
        print("Could not find symbols.")
        return

    # 2. Get data
    encrypted_flag = get_bytes_at_address(flag_addr, flag_size)
    iv = get_bytes_at_address(iv_addr, iv_size)

    if not encrypted_flag or not iv:
        print("Failed to read data.")
        return

    # 3. Get key
    key = get_key()
    print(f"Key: {key.hex() if key else 'None'}")

    if not key:
        print("Failed to extract key.")
        return

    # 4. Decrypt
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(encrypted_flag), AES.block_size)
        print(f"Flag: {plaintext.decode()}")
    except Exception as e:
        print(f"Decryption failed: {e}")

if __name__ == '__main__':
    main()
