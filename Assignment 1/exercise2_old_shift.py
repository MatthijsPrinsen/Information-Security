"""
Applies a sequence of shift/substitution cipher operations to plaintext,
composing them into a single mapping before applying.
"""
import sys


def get_input():
    """
    Reads operations line and plaintext from stdin.
    """
    # Read first line (operations)
    operations_line = input()
    
    # Read all remaining lines (plaintext)
    text_lines = []
    for line in sys.stdin:
        text_lines.append(line.rstrip('\n'))

    text = '\n'.join(text_lines)

    return operations_line, text


def mapping(mapping:dict, plaintext:str):
    """
    Applies a substitution mapping to plaintext, non-mapped chars pass through.
    """
    result = []
    
    for char in plaintext:
        if char in mapping:
            result.append(mapping[char])
        else:
            # Not a letter - keep unchanged
            result.append(char)
    
    return ''.join(result)


def shift_to_mapping(shift:int):
    """
    Converts an integer shift into a substitution mapping dict.
    """
    alpha = "abcdefghijklmnopqrstuvwxyz"
    mapping = {}
    
    for i, char in enumerate(alpha):
        new_index = (i + shift) % 26
        mapping[char] = alpha[new_index]
        mapping[char.upper()] = alpha[new_index].upper()
    
    return mapping


def create_direct_mapping(mapping_str):
    """
    Converts a 26-char mapping string into a substitution mapping dict.
    """
    alpha = "abcdefghijklmnopqrstuvwxyz"
    mapping = {}
    
    for i, char in enumerate(alpha):
        mapping[char] = mapping_str[i]
        mapping[char.upper()] = mapping_str[i].upper()
    
    return mapping


def parse_operations(line):
    """
    Parses the operations line into a list of (op_type, op_mode, param) tuples.
    """
    tokens = line.split()
    operations = []
    
    i = 0
    while i < len(tokens):
        op_type = tokens[i]  # 'e' or 'd'
        param = tokens[i + 1]  # either a number or mapping string
        
        try:
            shift_value = int(param)
            operations.append((op_type, 'shift', shift_value))
            i += 2
        except ValueError:
            operations.append((op_type, 'mapping', param))
            i += 2
    
    return operations  # list of tuples


def invert_mapping(mapping_dict):
    return {v: k for k, v in mapping_dict.items()}


def compbine_maps(map1, map2):
    """
    Composes two mappings into one by chaining map1 then map2.
    """
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    final_map = {}
    for char in alpha:
        step = map1[char]
        step = map2[step]
        final_map[char] = step
        final_map[char.upper()] = step.upper()
    return final_map


if __name__ == "__main__":
    operations, text = get_input()
    parsed_operations = parse_operations(operations)
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    # Start with identity map
    running_map = {char: char for char in alpha}

    for op in parsed_operations:
        op_type = op[0]
        op_mode = op[1]
        param = op[2]

        if op_mode == 'shift':
            if op_type == 'e':
                new_map = shift_to_mapping(param)
            else:  # 'd'
                new_map = shift_to_mapping(-param % 26)
        else:  # 'mapping'
            new_map = create_direct_mapping(param)
            if op_type == 'd':
                new_map = invert_mapping(new_map)

        running_map = compbine_maps(running_map, new_map)

    print(mapping(running_map, text))