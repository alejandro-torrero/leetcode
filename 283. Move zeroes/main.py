class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0 and i < len(nums)-1:
                nextNumber = None
                #Change to the next non zero element
                for j in range(i,len(nums)):
                    if nums[j] != 0:
                        nextNumber = j
                        break
                if nextNumber is not None:                    
                    nums[i],nums[j] = nums[j],nums[i]                        
        
m = [0,1,0,3,12]        
sol = Solution()
sol.moveZeroes(m)