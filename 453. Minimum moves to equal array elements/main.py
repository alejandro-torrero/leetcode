# remember each move increments two elements
# In one move, you can increment n - 1 elements of the array by 1.

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        return sum(nums) - len(nums) * min(nums)                   
    
sol = Solution()
print(sol.minMoves([1,2,3]))