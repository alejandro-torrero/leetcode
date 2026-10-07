class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        
        return len(nums)                
       
    
    
sol = Solution()
print(sol.missingNumber([1,2]))