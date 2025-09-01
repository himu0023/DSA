nums = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
row = len(nums)
col = len(nums[0])
result = [[0]*row for _ in range(col)]
for i in range(row):
  for j in range(col):
    result[j][i] = nums[i][j]
print(result)