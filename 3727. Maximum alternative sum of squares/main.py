import math

class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        
        absNums = [abs(n) for n in nums]        
        # Sort array so that the first numbers are taken as substracts
        absNums.sort()
        
        # 1 on imparis
        # 0 on pairs
        susbtractUntil = len(absNums) - math.ceil(len(absNums)/2)
        
        res = 0
        i = 0
        while i < susbtractUntil:
            res -= absNums[i]**2
            i+=1
            
            
        while i < len(absNums):
            res += absNums[i]**2
            i+=1
            
        return res
            
    
    
sol = Solution()
print(sol.maxAlternatingSum([1,2,3]))