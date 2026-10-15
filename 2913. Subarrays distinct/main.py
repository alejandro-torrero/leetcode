class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        res = 0

        for i in range(len(nums)):
            # The unique number is a subarray 
            for j in range(i,len(nums)):
                # Evaluate sub arrays                                   
                elementMap = {}                 
                for k in nums[i:j+1]:
                    # Go through the subarray
                    if k not in elementMap:
                        elementMap[k]= 1                             
                            
                res += len(elementMap) **2
        return res
    
sol = Solution()
print(sol.sumCounts([1,2,1]))