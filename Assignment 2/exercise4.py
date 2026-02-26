"""
given as input m, n, a private and a public key, checks if this private key
    is a valid key and whether the public key corresponds to it.

Input: m n; [private key]; public key

Output: -1 if the private key is invalid, 0 if the public key is invalid and 1 if both the public and
    private key are valid
"""
import sys

def input():
    input = sys.stdin.read()
    lines = input.strip().splitlines()
    first_line = lines[0]
    m, n = first_line.split(' ')
    m, n = int(m), int(n)
    private = [int(x) for x in lines[1].split(' ')]
    public = [int(x) for x in lines[2].split(' ')]
    return m, n, private, public

if __name__ == '__main__':
    m, n, private, public = input()
    print(m, n, private, public)