class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        hash = {}
        
        for i in range(len(nums)):
            if nums[i] in hash:
                hash[nums[i]] += 1                
            else:
                hash[nums[i]] = 1
            if hash[nums[i]] > len(nums)/2:
                return nums[i]
                                               

    
    
sol = Solution()
print(sol.majorityElement([3,2,3]))