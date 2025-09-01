
import math

class Solution:
    def lcmAndGcd(self, a : int, b : int):
        # code here
        gcd = math.gcd(a,b)
        lcm = abs(a * b) // gcd
        return [lcm,gcd]
    
sol = Solution()
print(sol.lcmAndGcd(14,8))