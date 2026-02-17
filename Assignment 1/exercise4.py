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


def parse_operations(line):
    tokens = line.split()
    operations = []
    
    i = 0
    while i < len(tokens):
        op_type = tokens[i]  # 'e' or 'd'
        param = tokens[i + 1]  # key string 
        operations.append((op_type, param))
        i += 2
    
    return operations # list of tuples


def encrypt(text, key):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    encrypted_text = ""    
    i = 0
    key_len = len(key)
    for char in text:
        #print(f"test: char = {char}")
        if char.lower() in alpha:
            #print(f"char '{char}' in alpha")
            char_idx = alpha.index(char.lower())
            
            key_char = key[i % key_len] 
            key_shift = alpha.index(key_char)
            
            new_idx = (char_idx + key_shift) % 26
            new_letter = alpha[new_idx]
            
            # Preserve case
            if char.isupper():
                encrypted_text += new_letter.upper()
            else:
                encrypted_text += new_letter
            
            i += 1
        else:
            # Keep non-alphabetic characters unchanged
            encrypted_text += char
            
    return encrypted_text

if __name__=="__main__":
    operations, text = get_input()
    #print(f"test: operations = {operations}, plaintext = {text}\n")
    parsed_operations = parse_operations(operations)
    #print(f"test: parsed operations = {parsed_operations}\n")
    for operation in parsed_operations:
        if operation[0] == 'e':
            text = encrypt(text, operation[1])
            #print(f"test: text = {text}\n")
        else:
            raise ValueError("Expected encryption")
    print(text)