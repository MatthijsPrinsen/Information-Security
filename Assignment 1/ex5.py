import sys
import math

def most_common_each_row(row):
    """
    Find the most common letter in the row, which corresponds to the key letter for that position.
    """
    max_index = 0 
    max_val = 0 
    for i in range(26):
        if row[i] > max_val:
            max_val = row[i]
            max_index = i

    key_shift = (max_index - 4) % 26
    key_letter = chr(key_shift + ord('a'))
    
    return key_letter

def find_hidden_key(best_key_len, text):
    """
    Frequency of each letter a certain index.
    """
    groups = [[0]*26 for _ in range(best_key_len)]

    pos = 0
    for i in text:
        if i.isalpha():
            i = i.lower()
            group = pos % best_key_len
            groups[group][ord(i)-ord('a')] += 1
            pos += 1

    word = []
    
    for i in groups:
        letter = most_common_each_row(i)
        word.append(letter)

    return ''.join(word)
    


def row_std(row):
    """
    Calculate the standard deviation of the frequencies in the row.
    """
    x_sqr = 0
    x_sum = 0
    for i in range(26):
        x = row[i]
        x_sqr += x**2
        x_sum += x
    
    std = math.sqrt((x_sqr/26) - (x_sum/26)**2)
    return std


def singular_row_std(group):
    """
    Calculate the sum of the standard deviations for each row in the group.
    """
    total = 0.0
    for row in group:
        total += row_std(row)
    return total


def get_key_length(key_len:int, string:str):
    """
    Taking in the current key length, to find the frequency for each letter at the key length. 
    Return it to be printed. 
    For loop for all possible key lengths. 
    

    Tested and working correctly. 
    """
    text = [i.lower() for i in string if i.isalpha()]
    groups = [[0]*26 for _ in range(key_len)]

    pos = 0
    for i in text:
        group = pos % key_len
        groups[group][ord(i)-ord('a')] += 1
        pos += 1

    return groups


def main():
    lines = sys.stdin.read().strip().split('\n')
    min_val = int(lines[0])
    max_val = int(lines[1])
    text = ''.join(lines[2:])  

    best_std = 0
    best_key = min_val

    for k in range(min_val, max_val + 1):
        groups = get_key_length(k, text)
        avg_std = singular_row_std(groups)
        print(f"The sum of {k} std. devs: {avg_std:.2f}")

        #find the best
        if avg_std > best_std:
            best_std = avg_std
            best_key = k

    print('')
    print("Key guess:")
    hidden_key =find_hidden_key(best_key, text)
    print(hidden_key)
    

if __name__ == "__main__":
    main()