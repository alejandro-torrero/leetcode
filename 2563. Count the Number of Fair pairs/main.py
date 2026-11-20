class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:        
        nums.sort()
        
        return self.searchWindow(nums,upper+1) - self.searchWindow(nums,lower)        
                
    
    def searchWindow(self,nums,value):
        i = 0
        j = len(nums)-1
        res = 0
        
        while i<j:
            goal = value - nums[i]            
            if nums[j] < goal:                
                res += j - i                
                i +=1
            else:
                j-=1

        return res
    
        

sol = Solution()
# print(sol.countFairPairs([0,1,7,4,4,5],3,6))
print(sol.countFairPairs([1,7,9,2,5],11,11))
# print(sol.countFairPairs([0,1,7,4,4,5],3,6))