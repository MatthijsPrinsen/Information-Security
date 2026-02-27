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
    key_bytes = []
    data_bytes = []
    
    first_ff = bytes_obj.index(0xFF)
    
    for char in bytes_obj[:first_ff]:
        key_bytes.append(char)
    for char in bytes_obj[first_ff+1:]:
        data_bytes.append(char)

    return key_bytes, data_bytes
        
        
def vernam(key_bytes, data_bytes):
    """
    XORs each data byte with the corresponding key byte and returns the result.
    """
    n = len(key_bytes)
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
