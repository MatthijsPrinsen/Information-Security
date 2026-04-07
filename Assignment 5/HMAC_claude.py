'''
Purpose: implement HMAC.
...
'''

import sys
# TODO: from exercise2 import tiger  (or however your Tiger module is named)

BLOCK_SIZE = 64          # bytes
IPAD = bytes([0x36] * BLOCK_SIZE)
OPAD = bytes([0x5C] * BLOCK_SIZE)

# --- Step 1: Read binary input from stdin ---
# Split on 0xFF separator to get key and message
data = sys.stdin.buffer.read()
sep = data.index(0xFF)
key = data[:sep]
message = data[sep+1:]

# --- Step 2: Pad key to BLOCK_SIZE with 0x00 ---
# If key > 64 bytes, HMAC spec says to hash it first — check if your assignment requires this
key_padded = key.ljust(BLOCK_SIZE, b'\x00')

# --- Step 3: XOR padded key with ipad and opad ---
k_ipad = bytes(a ^ b for a, b in zip(key_padded, IPAD))
k_opad = bytes(a ^ b for a, b in zip(key_padded, OPAD))

# --- Step 4: Compute inner hash ---
# inner = Tiger(k_ipad || message)
inner = tiger(k_ipad + message)

# --- Step 5: Compute outer hash ---
# outer = Tiger(k_opad || inner)
result = tiger(k_opad + inner)

# --- Step 6: Write binary output ---
sys.stdout.buffer.write(result)