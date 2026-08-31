class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        minVal = float('inf')
        minValI = -1
        maxVal = float('-inf')
        maxValI = -1
        
        for i in range(len(nums)):
            n=nums[i]            
            if n < minVal:
                minVal = n
                minValI = i
            if n > maxVal:
                maxVal = n
                maxValI = i
        
        # Remove from left
        removeLeft = max(minValI+1,maxValI+1)
        
        # Remove from right            
        
        removeRight = max(len(nums)-minValI,len(nums)-maxValI)
        
        # Remove from both sides
        
        removeBoth = min(minValI+1,len(nums)-minValI) + min(maxValI+1,len(nums)-maxValI) 
        return min (removeLeft,removeRight,removeBoth)



sol = Solution()
nums = [2,10,7,5,4,1,8,6]

def evaluate(fn,expectedResult, *args):
    res = fn(*args)
    if res == expectedResult:
        print("Sucess")
    else:
        print(f"Test failed. Recieved: {res} expected: {expectedResult}")

evaluate(sol.minimumDeletions,5,[2,10,7,5,4,1,8,6])
evaluate(sol.minimumDeletions,3,[0,-4,19,1,8,-2,-3,5])
evaluate(sol.minimumDeletions,1,[101])
evaluate(sol.minimumDeletions,6,[-14,61,29,-18,59,13,-67,-16,55,-57,7,74])
evaluate(sol.minimumDeletions,11,[-1,-53,93,-42,37,94,97,82,46,42,-99,56,-76,-66,-67,-13,10,66,85,-28])