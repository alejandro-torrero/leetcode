class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        res = 0
        
        for c in s:
            if c == "(":
                stack.append("(")
            else:
                if len(stack) == 0:
                    res +=1 
                else:
                    stack.pop()
                    
        if len(stack) > 0 :
            res += len(stack)
                
        return res
    
sol = Solution()

# 4
print(sol.minAddToMakeValid("()))(("))

