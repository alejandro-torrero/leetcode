class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = []
        left = []
        right = []        
        i = len(nums)-1
        
        # Fill right side
        while i>=1:
            if right == []:
                # Add the first element
                right.append(nums[i])
            else:
                right.insert(0,nums[i]*right[0])
            i -=1                    
                
        # Pop the first result as we dont need it        
        
        for j in range(len(nums)):         
            # print("----")        
            # print(j)    
            # print("right: ",right)
            # print("left: ",left)   
            # print("res: ",res)            
            if j == 0:
                res.append(right.pop(0))
                left.append(nums[j])
            elif j == len(nums)-1:                
                res.append(left.pop())
            else:
                newValue = left[-1] * right.pop(0)
                left.append(left[-1]*nums[j])
                res.append(newValue)
                
        return res
    
    
sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))