import math
class Solution:
    def mySqrt(self, x: int) -> int:
        return math.floor(math.sqrt(x))
    
print(Solution().mySqrt(4))
print(Solution().mySqrt(8))

# source: https://leetcode.com/problems/sqrtx
