n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,68,2]

# for num in n :
#   count = 0
#   for x in m :
#     if x == num:
#       count+=1
#   print(count)

hash_list = [0]*11
for num in n:
  hash_list[num]+=1

result = []
for x in m:
  if x<1 or x >10:
    result.append(0)
  else:
    result.append(hash_list[x])  
print(result)