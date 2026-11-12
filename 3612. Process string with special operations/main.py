class Solution:
    def processStr(self, s: str) -> str:
        resStr = []
        
        if len(s) == 0:
            return ''
        
        for c in s:                        
            if c == '#':
                # Duplicate current string and append
                resStr.extend(resStr)
                continue
            
            if c == '*':
                if len(resStr) == 0: continue
                resStr.pop()
                continue
                
            if c == '%':
                resStr.reverse()
                continue
            
            resStr.append(c)
            
        return "".join(resStr)
    
sol = Solution()
print(sol.processStr("a#b%*"))