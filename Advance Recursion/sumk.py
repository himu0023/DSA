def func(index, subset, total, nums, result, k):
    if total == k:
        result.append(subset.copy())
        return
    if total > k or index >= len(nums):
        return
    
    # Include the current element
    subset.append(nums[index])
    func(index + 1, subset, total + nums[index], nums, result, k)
    
    # Exclude the current element (backtrack)
    subset.pop()
    func(index + 1, subset, total, nums, result, k)

arr = [5, 9, 4]
result = []  # This should be a list, not 0
total = 0
k = 9
func(0, [], total, arr, result, k)

print(f"Subsets that sum to {k}:")
for subset in result:
    print(subset)