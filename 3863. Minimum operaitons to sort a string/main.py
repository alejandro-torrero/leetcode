class Solution:
    def minOperations(self, s: str) -> int:
        sorted_string = [c for c in s].sort()    
        print(sorted_string)
    
    
sol = Solution()
print(sol.minOperations("dog"))