class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:            
        if k == len(nums):
            # Get the largest number in the entire array
            return max(nums)                
        
        hashTable = {}                        
            
        for n in nums:
            if n in hashTable:
                hashTable[n] = hashTable[n]+1
            else:
                hashTable[n]=1
    
        if k == 1:
            # Get the largest not repeated number
            return max((k for k, v in hashTable.items() if v == 1),default=-1)
        
        if hashTable[nums[0]] == 1 and hashTable[nums[-1]] == 1:
            return max(nums[0],nums[-1])
        
        if hashTable[nums[0]] > 1 and hashTable[nums[-1]] == 1:
            return nums[-1]
        elif hashTable[nums[-1]]>1 and hashTable[nums[0]] ==1 :
            return nums[0]
        else:
            return -1    
        
sol = Solution()
print(sol.largestInteger([3,9,7,2,1,7],4))
        