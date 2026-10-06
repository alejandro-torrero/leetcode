class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
            
sol = Solution()

print(sol.isPowerOfTwo(1))