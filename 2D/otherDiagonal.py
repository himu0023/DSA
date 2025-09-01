nums = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

n = len(nums)

for i in range(n):
    for j in range(n):
        if j != n - 1 - i:
            nums[i][j] = '*'

# Display modified matrix
for row in nums:
    print(row)