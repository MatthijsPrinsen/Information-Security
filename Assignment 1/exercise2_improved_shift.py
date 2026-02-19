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


def mapping(mapping:dict, plaintext:str):
    result = []
    
    for char in plaintext:
        if char in mapping:
            result.append(mapping[char])
        elif char.lower() in mapping:
            result.append(mapping[char.lower()].upper())
        else:
            # Not a letter - keep unchanged
            result.append(char)
    
    return ''.join(result)


def shift_to_mapping(shift:int):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    mapping = {}
    
    #find mapping    
    for i, char in enumerate(alpha):
        # Shift the index, wrap around using modulo
        new_index = (i + shift) % 26
        mapping[char] = alpha[new_index]
        # Also handle uppercase
        mapping[char.upper()] = alpha[new_index].upper()
    
    return mapping

    
def create_direct_mapping(mapping_str):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    mapping = {}
    
    for i, char in enumerate(alpha):
        mapping[char] = mapping_str[i]
    
    return mapping    


def parse_operations(line):
    tokens = line.split()
    operations = []
    
    i = 0
    while i < len(tokens):
        op_type = tokens[i]  # 'e' or 'd'
        param = tokens[i + 1]  # either a number or mapping string
        
        # Check if it's a shift (number) or mapping (string)
        try:
            shift_value = int(param)
            operations.append((op_type, 'shift', shift_value))
            i += 2
        except ValueError:
            # It's a mapping string
            operations.append((op_type, 'mapping', param))
            i += 2
    
    return operations # list of tuples


def invert_mapping(mapping_dict):
    return {v: k for k, v in mapping_dict.items()}    

def shift(n, text):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    new_text = ""
    
    for char in text:
        if char.lower() in alpha:
            char_index = alpha.index(char.lower())
            new_index = (char_index + n) % 26
            new_char = alpha[new_index]
            
            # keep uppercase
            if char.isupper():
                new_text += new_char.upper()
            else:
                new_text += new_char
        else:
            # Keep other chars unchanged
            new_text += char
    
    return new_text


def combine_mappings(map1, map2):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    final_mapping = {}
    for char in alpha:
        step = map1[char]
        step = map2[step]
        final_mapping[char] = step
    return final_mapping


def shift_to_mapping(shift:int):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    mapping = {}
    
    #find mapping    
    for i, char in enumerate(alpha):
        # Shift the index, wrap around using modulo
        new_index = (i + shift) % 26
        mapping[char] = alpha[new_index]
    
    return mapping


if __name__ == "__main__":
    operations, text = get_input()
    parsed_operations = parse_operations(operations)
    final_shift = 0
    final_mapping = {}
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for char in alpha:
        final_mapping[char] = char 
    
    for op in parsed_operations:
        op_type = op[0]
        op_mode = op[1]
        param = op[2]
        
        #combine shifts
        if op_mode == 'shift':
            param = shift_to_mapping(param)
        #combine mappings
        if op_mode == 'mapping':
            param = create_direct_mapping(param)
        if op_type == 'd':
            param = invert_mapping(param)
            
        final_mapping = combine_mappings(param, final_mapping)
        
    final_shift = final_shift % 26
    
    #run operation
    text = mapping(final_mapping, text)
    
    print(text)
        
    