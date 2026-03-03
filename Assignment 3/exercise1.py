"""
Description: computes the private RSA key from a public key, then encrypts or decrypts one or 
    more numbers

Input: The e or d in the first line specifies whether to encrypt or decrypt. This is followed by x
    lines of numbers to be encrypted. 
    
Output: The encrypted numbers, separated by newlines
    
N.B.: This exercise will feature intermediate values in the range of 1017. Keep this in mind
    when deciding what data types to use
"""
import sys

def get_input():
    obj = sys.stdin.buffer.read()
    mode = str(obj[1])
    numbers = []
    for row in obj[1:]:
        numbers.append(row)
    return mode, numbers

if __name__ == "__main__":
    mode, numbers = get_input()
    print(f"mode: {mode}, numbers: {numbers}")
