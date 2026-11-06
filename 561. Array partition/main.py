class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        print(nums)
        res = 0
        for i in range(0,len(nums),2):
            res += min(nums[i],nums[i+1])
            
        return res
    
    
sol = Solution()
print(sol.arrayPairSum([1,4,3,2]))