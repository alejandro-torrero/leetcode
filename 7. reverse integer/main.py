
class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        res = 0
        sign = 1 if x >+ 0 else -1
        x = abs(x)
        
        while x:
            pop = x % 10
            x = (x-pop)/10
            res = res * 10 +pop            

            if res > INT_MAX or res < INT_MIN:
                return 0
        
        return int(res)*sign            



sol = Solution()
print(sol.reverse(123))