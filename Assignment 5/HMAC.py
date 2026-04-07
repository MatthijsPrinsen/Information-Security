'''
Purpose: implement HMAC.
Create a program that reads a key and a message, then applies the HMAC algorithm to it
and shows the output. The hash function you should use is the Tiger hash you implemented
in exercise 2. The input of the program is given in binary form: first the key, followed by the
separator byte 0xFF, followed by the message. The key is never longer than 64 bytes. The
output should also be in binary.
Note: What isn’t stated very clearly in many places is that the key in the HMAC algorithm
should be padded with consecutive 0x00 bytes until it has a length equal to 64 bytes. This is
in fact necessary in order to do the XOR with the ipad and opad.
If you are using Python to implement this program, due to Themis limitations the filename
of the file containing the main function should be HMAC.py.
'''

# constants = opad, ipad
#  inner hash = ipad, 
#  outer hash = opad
#  B = 64

B = 64
ipad_byte = 0x36
opad_byte = 0x5c
ipad = B * ipad_byte
opad = B * opad_byte

# Input = key, message
#  The input of the program is given in binary form: first the key, followed by the separator 
#  byte 0xFF, followed by the message

def get_input():
    # Read key, message
    key, message = input()
    return key, message

# Apply HMAC
#  import tiger hash
#   at the key in the HMAC algorithm should be padded with consecutive 0x00 bytes until it has 
#   a length equal to 64 byte 
