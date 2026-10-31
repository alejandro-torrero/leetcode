class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = float('-inf')
        n = len(nums)
        lookup = {}
        
        def move(i):
            if i == n:
                return 0
            
            if i in lookup:
                return lookup[i]
            
            lookup[i] = max(nums[i], nums[i] + move(i+1))
            return lookup[i]
            
        for i in range(n):    
            res = max(res,move(i))
        
        return res


# The array order cannot be changed    
sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))