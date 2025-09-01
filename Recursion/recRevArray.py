def reverse(arr, left, right):
  if left>=right:
    return
  arr[left], arr[right] = arr[right], arr[left]
  reverse(arr, left+1, right-1)

array = [1,2,3,4,5,6,7]
print(array)
reverse(array,2,5)
print(array)