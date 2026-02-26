"""
Feistel cipher implementation.

Input: first the binary value of d (0x64) or e (0x65)
specifying whether to decrypt or encrypt, followed by the binary value 0xFF, followed by a key,
then another 0xFF, and finally the input data. The key size is a multiple of 4 bytes, while the
input data is a multiple of 8 bytes

Output: 
"""
import sys

def get_input():
    bytes_obj = sys.stdin.buffer.read()
    
    if bytes_obj[0] == 0x65:
        mode = 'e'  # 0x64 = 'd', 0x65 = 'e'
    elif bytes_obj[0] == 0x64:
        mode = 'd'
    else:
        raise ValueError("first byte not recognised. 0x64 = 'd', 0x65 = 'e'")
    
    # find the two 0xFF separators
    first_ff = bytes_obj.index(0xFF)
    second_ff = bytes_obj.index(0xFF, first_ff + 1)
    
    key_bytes = list(bytes_obj[first_ff + 1 : second_ff])
    data_bytes = list(bytes_obj[second_ff + 1 :])
    
    return mode, key_bytes, data_bytes


def F(r, k):
    """Round function: simply returns the key."""
    return k


def xor_bytes(a, b):
    """XOR two equal-length lists of bytes together."""
    return [x ^ y for x, y in zip(a, b)]


def feistel_block(block, subkeys, mode):
    L = list(block[:4])
    R = list(block[4:])
    
    if mode == 'd':
        L, R = R, L 
    
    keys = subkeys if mode == 'e' else list(reversed(subkeys))
    
    for k in keys:
        L, R = R, xor_bytes(L, F(R, k))
    
    if mode == 'd':
        L, R = R, L 
    
    return L + R


def feistel(data, key, mode):
    """Split key into 4-byte subkeys, then process each 8-byte block."""
    # split key into 4-byte chunks
    subkeys = [key[i:i+4] for i in range(0, len(key), 4)]
    
    output = []
    # process data in 8-byte blocks
    for i in range(0, len(data), 8):
        block = data[i:i+8]
        output += feistel_block(block, subkeys, mode)
    
    return output

if __name__ == "__main__":
    mode, key_bytes, data_bytes = get_input()
    c = feistel(data_bytes, key_bytes, mode)
    sys.stdout.buffer.write(bytes(c))