class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1

        while i <= j:
            iValue = s[i]
            jValue = s[j]
            
            s[i] = jValue
            s[j] - iValue
            
            i+=1
            j -=1        
        
        
sol = Solution()

print(sol.reverseString(["h","e","l","l","o"]))