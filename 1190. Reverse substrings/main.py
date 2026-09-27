class Solution:
    def reverseParentheses(self, s: str) -> str:
        parentehsis_idx = []
        res = []
        
        for c in s:
            if c == "(":
                # Save open parenthesis index
                parentehsis_idx.append(len(res))
            elif c == ")":
                # start: from where we need to reverse the string
                start = parentehsis_idx.pop() 
                res[start:] = res[start:][::-1]
            else:
                res.append(c)
        return "".join(res)        
    
    
sol = Solution()
print(sol.reverseParentheses("(a(13)b)"))