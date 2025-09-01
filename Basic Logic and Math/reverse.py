class Solution:
  def reverse(self, x):
    num = x 
    sum = 0
    while num > 0:
      id = num%10
      sum = sum*10 + id
      num=num//10
    return sum 
  
sol = Solution()
print(sol.reverse(1234))  