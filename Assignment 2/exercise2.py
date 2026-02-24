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


def init_lookup_table(key):
    N = len(key)
    S = list(range(256))
    K = [key[i % N] for i in range(256)]
    
    j = 0
    for i in range(256):
        j = (j + S[i] + K[i]) % 256
        S[i], S[j] = S[j], S[i] 
    return S


def PRGA(S, data):
    i = 0
    j = 0
    output = []
    
    # drop first 256 keystream bytes
    for _ in range(256):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
    
    # encrypt
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        keystream_byte = S[(S[i] + S[j]) % 256]
        output.append(byte ^ keystream_byte) 
    return output

if __name__ == "__main__":
    key_bytes, data_bytes = get_input()
    S = init_lookup_table(key_bytes)
    c = PRGA(S, data_bytes)
    sys.stdout.buffer.write(bytes(c))
