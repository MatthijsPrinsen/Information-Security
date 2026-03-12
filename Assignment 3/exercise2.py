"""
Diffie-Hellman key exchange based on Elliptical Curve Cryptography.

Input: a starting point on the curve y2 = x3 + ax + b, the values 
    of a, b, and modulo p and lastly the values m and n

Output:  the shared secret, in the following format: (x’, y’)
"""

