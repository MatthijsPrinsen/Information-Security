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
    obj = sys.stdin.read().splitlines()
    mode = str(obj[0])
    p, q, e = obj[1].split()
    p, q, e = int(p), int(q), int(e)
    numbers = []
    for row in obj[2:]:
        numbers.append(row)
    return mode, p, q, e, numbers


def key_gen(p, q, e, mode):
    n = p*q
    d = None
    phi = (p-1)*(q-1)
    if mode == 'd':
        d = pow(e, -1, phi) # modular inverse
    return n, d


def rsa(m, exp, n):
    return pow(m, exp, n)

if __name__ == "__main__":
    mode, p, q, e, numbers = get_input()
    n, d = key_gen(p,q,e, mode)
    
    if mode == 'e':
        exp = e
    else:
        exp = d

    for num in numbers:
        print(rsa(int(num), exp, n))