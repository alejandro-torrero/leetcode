class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        res = float('inf')
        
        for i in range(len(nums)):
            nStr = str(nums[i])
            sum = 0            
            for char in nStr:
                sum += int(char)
                
            print(sum)
            
            if sum == i:
                res = min(sum,res)
                
        return res if res != float('inf') else -1
            
            
            
sol = Solution()

print(sol.smallestIndex([1,3,2]))