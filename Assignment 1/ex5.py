import sys
import numpy as np
import math

def most_common_each_row(row):
    pass

def find_hidden_key(best_key_len, text):
    groups = np.zeros((best_key_len, 26), dtype=int)

    pos = 0
    #frequency of each letter a certain index.
    for i in text:
        group = pos % best_key_len
        groups[group][ord(i)-ord('a')] += 1
        pos += 1

    word = []
    
    for i in groups:
        letter = most_common_each_row(i)
        word.append(letter)

    clean_word = ''.join(word)
    print(clean_word)


def row_std(row):
    mean = sum(row) / 26
    var = sum((x - mean)**2 for x in row) / 26
    return math.sqrt(var)


def singular_row_std(group):
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
    # Remove special characters
    text = [i.lower() for i in string if i.isalpha()]

    # create 26 letter list for each letter and for each key length. 
    groups = np.zeros((key_len, 26), dtype=int)

    pos = 0
    #frequency of each letter a certain index.
    for i in text:
        group = pos % key_len
        groups[group][ord(i)-ord('a')] += 1
        pos += 1

    #Groups by the key length of the frequency of letters occuring there. 
    return groups


def main():
    lines = sys.stdin.read().strip().split('\n')
    min_val = int(lines[0])
    max_val = int(lines[1])
    text = ''.join(lines[2:])  # Join ALL remaining lines

    best_std = 0
    best_key = min_val

    for k in range(min_val, max_val + 1):
        print(f"Key length: {k}")
        groups = get_key_length(k, text)
        avg_std = singular_row_std(groups)
        print(f"Sum of {k} std. devs: {avg_std:.2f}")

        #find the best
        if avg_std > best_std:
            best_std = avg_std
            best_key = k

    print(best_key)
    find_hidden_key(best_key, text)

    

if __name__ == "__main__":
    main()