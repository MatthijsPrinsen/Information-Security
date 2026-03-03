"""
given as input m, n, a private and a public key, checks if this private key
    is a valid key and whether the public key corresponds to it.

Input: m n; [private key]; public key

Output: -1 if the private key is invalid, 0 if the public key is invalid and 1 if both the public and
    private key are valid
"""
import sys
from math import gcd

def get_input():
    input = sys.stdin.read()
    lines = input.strip().splitlines()
    first_line = lines[0]
    m, n = first_line.split(' ')
    m, n = int(m), int(n)
    private = [int(x) for x in lines[1].split(' ')]
    public = [int(x) for x in lines[2].split(' ')]
    return m, n, private, public


def private_validation(key, m, n):
    # check if superincreasing
    total = 0
    for i in range(len(key)):
        if key[i] <= total:
            return False
        total += key[i]
    if n <= total:
        return False
    if gcd(m, n) != 1:
        return False
    return True


def public_validation(m, n, priv, pub):
    generated_key = []
    for i in range(len(priv)):
        generated_key.append((priv[i]*m)%n)        
    if generated_key == pub:
      return True
    return False  
        
        
if __name__ == '__main__':
    m, n, private, public = get_input()
    if not private_validation(private, m, n):
        print("-1")
    elif not public_validation(m, n, private, public):
        print("0")
    else:
        print("1")
    