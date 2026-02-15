import sys


def get_input():
    # Read first line (operations)
    operations_line = input()
 
    # Read all remaining lines (plaintext)
    text_lines = []
    for line in sys.stdin:
        text_lines.append(line.rstrip('\n'))

    text = '\n'.join(text_lines)
 
    return operations_line, text

#def shift letter (letter, n)
#def find n based on key
key = "lemon"
alpha = "abcdefghijklmnopqrstuvwxyz"
text = "Hello World!"
encrypted_text = ""
i = 0
key_len = len(key)

for char in text:
    if char.lower() in alpha:
        # Get the index of the character in the alphabet
        char_idx = alpha.index(char.lower())
        
        # Get the shift amount from the key
        key_char = key[i % key_len]  # Use modulo here instead
        key_shift = alpha.index(key_char)
        
        # Apply the shift with wrapping
        new_idx = (char_idx + key_shift) % 26
        new_letter = alpha[new_idx]
        
        # Preserve case
        if char.isupper():
            encrypted_text += new_letter.upper()
        else:
            encrypted_text += new_letter
        
        i += 1  # Only increment for actual letters
    else:
        # Keep non-alphabetic characters unchanged
        encrypted_text += char

print(encrypted_text)  # Should output: "Sixzb Hsdzq!"