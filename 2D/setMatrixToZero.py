def matrixZero(nums, row, col):
    rows = len(nums)
    cols = len(nums[0])

    # Mark the entire row
    for j in range(cols):
        if nums[row][j] != 0:
            nums[row][j] = float('-inf')

    # Mark the entire column
    for i in range(rows):
        if nums[i][col] != 0:
            nums[i][col] = float('-inf')

def setZeros(nums):
    row = len(nums)
    col = len(nums[0])

    for i in range(row):
        for j in range(col):
            if nums[i][j] == 0:
                matrixZero(nums, i, j)

    for i in range(row):
        for j in range(col):
            if nums[i][j] == float('-inf'):
                nums[i][j] = 0

# Example matrix
nums = [[1, 2, 3, 10],
        [4, 5, 0, 11],
        [7, 0, 9, 12],
        [13,14,15,16]]

setZeros(nums)

# Print modified matrix
for row in nums:
    print(row)
