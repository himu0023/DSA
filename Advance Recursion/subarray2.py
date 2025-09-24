def sub_arr(arr):
  n = len(arr)

  for i in range(n):
      for j in range(i, n):
          for k in range(i, j+1):
              print(arr[k], end = " ")
          print()

nums= [1,2,3,4]
sub_arr(nums)        