class Solution:
    def maxDepth(self, s: str) -> int:
        p_stack = []
        max_nested = 0
        
        for c in s:
            if c == "(":
                p_stack.append("(")
            elif c == ")":
                max_nested = max(max_nested,len(p_stack))
                p_stack.pop()    
        
        return max_nested
                
                
sol = Solution()
print(sol.maxDepth("(1+(2*3)+((8)/4))+1"))