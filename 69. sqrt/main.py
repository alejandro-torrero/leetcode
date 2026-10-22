class Solution:
    def mySqrt(self, x: int) -> int:     
        
        max_iterations =300000

        sqrt_x = 1        
        
        for i in range(max_iterations):
            print(sqrt_x)
            sqrt_x = 0.5 * (sqrt_x+(x/sqrt_x))

        return int(sqrt_x)
    
    
sol = Solution()
print(sol.mySqrt(0))