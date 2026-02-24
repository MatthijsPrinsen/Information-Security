"""
Description: given a key and input data, applies the key as a one time pad (Vernam cipher) 
to the input data to encrypt or decrypt it.

Input: first a key consisting of n bytes, followed by the binary value 0xFF, 
followed by the input data consisting of n bytes as well.

Output: the encrypted/decrypted data, also in binary.
"""
import sys


def get_input():
    bytes_obj = sys.stdin.buffer.read()
    print(f"This is a line of bytes:{bytes_obj}")
        
if __name__ == "__main__":
    get_input()
    

