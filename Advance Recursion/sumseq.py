def func(nums):
  n = len(nums)
  total_subset = 1<<n
  result = []

  for num in range(total_subset):
    subset_sum =0
    for i in range(n):
      if num & (1<<i):
        subset_sum  += nums[i]
    result.append(subset_sum)
  return result

arr = [1,3,4,5]
ans = func(arr)
print(ans)