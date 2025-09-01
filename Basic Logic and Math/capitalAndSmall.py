from collections import Counter

S = "ABCDaaaBBCCIIOOppaaaaaxxZZ"
q = ['a','A','x','X','Z','b','z']

freq = Counter(S)

result = {}

for ch in q:
  result[ch] = freq.get(ch,0)
print(result)  

hash_list = [0]*128

for ch in q:
  index = ord(ch)
  hash_list[index]+=1

for ch in S:
  index = ord(ch)
print(len(hash_list))
print(hash_list)