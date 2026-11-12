class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        
        # Counters start at one as the lastNum is included on the count
        increasingCount = 1
        decreasingCount = 1
        res = 1
        lastNum = nums[0]
        
        for i in range(1,len(nums)):
            if lastNum > nums[i]:
                # The number is decreasing
                decreasingCount += 1
                lastNum = nums[i]
                                
                
                # Reset the increasing counter as we found a decreasing scenario
                res = max(res,decreasingCount,increasingCount)
                increasingCount = 1
                
                # print('Decreasing scenario found', res,decreasingCount,increasingCount)
                
            elif lastNum < nums[i]:
                increasingCount += 1
                lastNum = nums[i]     
                
                # Reset the decreasing count
                res = max(res,decreasingCount,increasingCount)
                decreasingCount = 1
                # print('Increasing scenario found', res,decreasingCount,increasingCount)
            else:                
                decreasingCount = 1
                increasingCount = 1
                            
        return res
    
    
sol = Solution()
print(sol.longestMonotonicSubarray([1,4,3,3,2]))
# print(sol.longestMonotonicSubarray([3,2,1]))