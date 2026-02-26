def combine_mappings(map1, map2):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    final_mapping = {}
    for char in alpha:
        step = map1[char]
        step = map2[step]
        final_mapping[char] = step
    return final_mapping

alpha = "abcdefghijklmnopqrstuvwxyz"
testcase2 = "xybdflrcmtpzwnagevjhoskuqi"
testcase = "yxbdflrcmtpzwnagevjhoskuqi"
mapping = {}
test_map = {}
test_map2 = {}

for char in alpha:
    mapping[char] = char
    idx = alpha.index(char.lower())
    test_map[char] = testcase[idx]
    test_map2[char] = testcase2[idx]
final = combine_mappings(test_map2, test_map)
print(final)