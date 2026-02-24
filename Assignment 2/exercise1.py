"""
Description: given a key and input data, applies the key as a one time pad (Vernam cipher) 
    to the input data to encrypt or decrypt it.

Input: first a key consisting of n bytes, followed by the binary value 0xFF, 
    followed by the input data consisting of n bytes as well.

Output: the encrypted/decrypted data, also in binary.
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
        
        
def vernam(key_bytes, data_bytes):
    """
    XORs each data byte with the corresponding key byte and returns the result.
    """
    n = len(data_bytes)
    c = []
    for i in range(n):
        key_byte = key_bytes[i]
        data_byte = data_bytes[i]
        encrypted_byte = key_byte ^ data_byte
        c.append(encrypted_byte)
    return c
        
if __name__ == "__main__":
    key_bytes, data_bytes = get_input()
    c = vernam(key_bytes=key_bytes, data_bytes=data_bytes)
    sys.stdout.buffer.write(bytes(c))
    #print("done!", file=sys.stderr)
