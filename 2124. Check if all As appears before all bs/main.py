# A string must always start with a's, if a b is detected between two a's, then return false

class Solution:
    def checkString(self, s: str) -> bool:
        return not "ba" in s
            
    
sol = Solution()
print(sol.checkString("aaabbb"))
print(sol.checkString("abab"))
print(sol.checkString("bbb"))