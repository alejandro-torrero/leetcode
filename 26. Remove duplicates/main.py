class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:             
        map = {}
        j = -1 # Pointer to insert data        
        length = 0
        
        for i in range(len(nums)):            
            n = nums[i]            
            if n in map:
                # Repeated number, update replaceable index                
                if j==-1:                            
                    j = i                
            else:
                map[n] = True # Add number to map
                # New number, check if needs to change place
                if j >= 0 :                    
                    nums[j] = n
                    nums[i] = -1
                    j +=1              
                length += 1        
                
        return length
        
sol =  Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))