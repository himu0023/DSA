from collections import Counter
S = "azyxyyzaaaa"
q = ["a","a","a","y","x"]


hash_list = [0] * 26

# Count frequencies
for ch in S:
    index = ord(ch) - 97
    hash_list[index] += 1

# Query and print frequencies
for ch in q:
    index = ord(ch) - 97
print(hash_list)

freq = Counter(S)

result = {}

for ch in q:
   result[ch] = freq.get(ch,0)
print(result)