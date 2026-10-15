class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # validate if its possible to get that sum with the higher number
        # we could get with the parameters
        if sum > 9 * num:
            return ""
        
        # Calculate how many left side 9's can be added to the solution
        q, r = divmod(sum, 9)
        
        print(q,r)
        # Add every left side 9 possible
        ans = "9" * q
        
        if r > 0:
            ans += str(r)
        
        # Append the required zeros to fill the length of the string
        ans += "0" * (num - len(ans))
        return ans
    
sol = Solution()
print(sol.maxSumOfSquares(2,3))