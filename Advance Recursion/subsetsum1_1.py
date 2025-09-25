def main(nums, result):

  def solve(index, total):
    if index >= len(nums):
      result.append(total)
      return 
    solve(index+1, total+nums[index])
    Sum=total 
    solve(index+1, total)
    return result
  
  solve(0,0)
arr = [5,9,6]
result = []
main(arr, result)
print(result)