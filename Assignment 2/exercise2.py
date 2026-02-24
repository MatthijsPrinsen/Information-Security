"""
Implements the RC4 stream cipher.

Input:  first a key, followed by the binary value 0xFF, 
    followed by the input data

Output: the encrypted/decrypted data, also in binary 
"""

import sys


def get_input():
    """
    Reads stdin as binary, splitting on 0xFF into key bytes and data bytes.
    """
    bytes_obj = sys.stdin.buffer.read()
    key = True
    key_bytes = []
    data_bytes = []
    for char in bytes_obj:
        if char == 0xFF:
            key = False
            continue
        if key == True:
            key_bytes.append(char)
        else:
            data_bytes.append(char)
    #print(f"Key bytes: {len(key_bytes)}, Data bytes: {len(data_bytes)}", file=sys.stderr)
    return key_bytes, data_bytes