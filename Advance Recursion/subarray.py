def sub_arr(nums):
  n = len(nums)
  result = []

  for i in range(n):
    for j in range(i, n):
      subarray = []
      for k in range(i, j+1):
        subarray.append(nums[k])
      result.append(subarray)
    print(subarray)
  return result

arr=[1,2,3,4]
sub_arr(arr)