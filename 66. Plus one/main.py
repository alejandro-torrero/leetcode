class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits) # Array length
        i = n - 1 # Last element of the array        
        ctrFlag = True        
        
        while ctrFlag and i >= 0:
            sum = digits[i] + 1                                   
            
            if sum < 10:
                ctrFlag = False
                digits[i] = sum
            else:
                digits[i] = 0                  
            
            if i - 1 < 0 and sum == 10:
                # We need to add anoterh element
                digits.insert(0,1)
            
            
            i -=1
            
        return digits
    
sol = Solution()
print(sol.plusOne([0]))