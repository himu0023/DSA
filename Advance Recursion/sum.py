def func(index, subset, target):
  if index>=len(nums):
    if sum(subset) == target:
      result.append(subset.copy())
    return
  subset.append(nums[index])
  func(index+1, subset, target)
  subset.pop()
  func(index+1, subset, target)




nums = [4, 5, 9]
result = []
target = 9
func(0,[], target)
print(result)