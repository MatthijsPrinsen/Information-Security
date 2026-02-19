import sys
import numpy as np

def get_input():
    """
    Get input
    """
    lines = sys.stdin.read().strip().split('\n')
    min_val, max_val, text = int(lines[0]), int(lines[1]), lines[2]

    return min_val, max_val, text


def frequency_analysis(group):
    x_sqr = 0 
    x_sum = 0 
    for i in range(26):
        x = group[i]
        x_sqr += x**2
        x_sum += x
    
    std = np.sqrt((x_sqr/26) - (x_sum/26)**2)
    return std




def key_length(key_len, text):
    alpha = "abcdefghijklmnopqrstuvwxyz"

    groups = [[0]* 26] * key_len

    i = 0
    text_length = len(text)

    for i in range(text_length):
        char = text[i]
        print("this is a letter",char)
        if char.lower() in alpha:
            index = alpha.index(char.lower())
            print(f"this is an index {index}")
            print(f"this is all the groups {groups}")
            print(f"this is a single group {groups[0]}")
            print(f"this is a single letter {groups[0][0]}")
            groups[i % key_len][index] += 1
            
        
        i += 1

    return groups 



def frequency_vector(min, max, text):
    means = []
    stds_means = []
    letters = [i.lower() for i in text if i.isalpha]
    print("these are the letters",letters)
    for k in range(min, max+1):
        print(f"Key length: {k}")
        groups = key_length(k, letters)
        for i in range(k):
            std = frequency_analysis(groups[i])
            stds_means.append(std)
        mean = sum(stds_means)/len(stds_means)
        means.append(mean)
        print(f"Sum of {k} std. devs: {mean}")
        stds_means = []
        
    print(f"All means: {means}")
    highest_number = max(means)
    return highest_number


def main():
    min_val, max_val, text = get_input()
    most_common_key = frequency_vector(min_val, max_val, text)

if __name__ == "__main__":
    main()