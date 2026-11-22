class Solution:
    def rob(self, nums: list[int]) -> int:
        if nums is None:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        lookup = {}
        # Start robing from the first house or the second onward
        # But starting from the first house cannot rob the last one
        return max(self.robHouse(nums,False,0,lookup), self.robHouse(nums,True,1,lookup)) 
    
    def robHouse(self, nums, canRobLast, i,lookup = None)->int:
        if i == len(nums)-1 and canRobLast == False:
            # Cannot rob the last house
            return 0        
        
        lookup ={} if lookup is None else lookup
        
        if (i,canRobLast) in lookup:
            return lookup[(i,canRobLast)]
        
        if i >= len(nums):
            # Got to the end
            return 0
        
        lookup[(i,canRobLast)]= max(nums[i]+self.robHouse(nums,canRobLast,i+2,lookup), self.robHouse(nums,canRobLast,i+1,lookup))
        return lookup[(i,canRobLast)]
        
    
    
sol = Solution()
print(sol.rob([94,40,49,65,21,21,106,80,92,81,679,4,61,6,237,12,72,74,29,95,265,35,47,1,61,397,52,72,37,51,1,81,45,435,7,36,57,86,81,72]))