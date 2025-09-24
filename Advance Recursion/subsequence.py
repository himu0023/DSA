def func(index, subset, nums, result):
  if index >= len(nums):
    result.append(subset.copy())
    return
  subset.append(nums[index])
  func(index+1, subset,nums, result)
  subset.pop()
  func(index+1, subset, nums, result)
  


nums = [1,2,3,4]
result = []
func(0, [], nums, result)
print("All subsets: ")
for subset in result:
  print(subset)