class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:        
        index = -1
        for i in range(len(nums)):
            print(f"Processing i:{i}")
            # Go trhough each value            
            stableNumber=max(nums[0:i+1]) - min(nums[i:len(nums)])
            print(f"stableNumber:{stableNumber}")
            if  stableNumber <= k:
                # Stable number              
                index = i
                break
            
        return index
            
sol = Solution()
print(sol.firstStableIndex([2,0,2],3))