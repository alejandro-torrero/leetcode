class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums) == 0:
            return []
        nums.append(nums[-1])
        res = []
        
        startIdx = None
        lastNum = None        
        
        for i in range(len(nums)):
            if startIdx is None:
                startIdx = nums[i]
                lastNum = nums[i]
                continue
            
            if lastNum+1 == nums[i]:                
                lastNum = nums[i]                
            else:
                if lastNum == startIdx:
                    res.append(f"{startIdx}")
                else:
                    res.append(f"{startIdx}->{lastNum}")
                startIdx = nums[i]
                lastNum = nums[i]
        
        return res
    
sol = Solution()
print(sol.summaryRanges([0,1,2,4,5,7]))
print(sol.summaryRanges([0,2,3,4,6,8,9]))