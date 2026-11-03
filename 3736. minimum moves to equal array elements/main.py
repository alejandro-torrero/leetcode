class Solution:
    def minMoves(self, nums: list[int]) -> int:
        res = 0
        target = max(nums)                
        
        for i in range(len(nums)):
            if nums[i] != target:
                res += target - nums[i]
            
        return res
    
    
sol = Solution()
print(sol.minMoves([1,2,3]))
print(sol.minMoves([4,4,5]))