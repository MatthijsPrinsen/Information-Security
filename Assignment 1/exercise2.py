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
        mapping[char.upper()] = mapping_str[i].upper()
    
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


if __name__ == "__main__":
    operations, text = get_input()
    parsed_operations = parse_operations(operations)
    for op in parsed_operations:
        # convert to encrypt mapping
        op_type = op[0]
        op_mode = op[1]
        param = op[2]
        
        # shift to mapping
        if op_mode == 'shift':
            param = shift_to_mapping(param)
            op_mode = 'mapping'
        else:
            param = create_direct_mapping(param)
            
        # decrypt to encrypt
        if op_type == 'd':
            param = invert_mapping(param)
            op_type = 'e'
            
        if not op_mode == 'mapping' or not op_type == 'e':
            raise 'convertion failed'
        
        text = mapping(param, text)
        
    print(text)
        
    