n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,68,2]

freq = {}
for num in n:
  freq[num] = freq.get(num,0)+1
print(freq)

result = {x:freq.get(x,0) for x in m}
print(result)