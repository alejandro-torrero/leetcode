class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # # means backspace
        finalS = []
        finalT = []
        
        for i in range(len(s)):
            c = s[i]
            if c == '#':
                if len(finalS) >0:
                    finalS.pop()
            else:
                finalS.append(c)
                
        for i in range(len(t)):
            c = t[i]
            if c == '#':
                if len(finalT) >0:
                    finalT.pop()
            else:
                finalT.append(c)       
        
        return finalS == finalT
    
    
sol = Solution()
# print(sol.backspaceCompare("ab#c","ad#c"))
# print("---")
# print(sol.backspaceCompare("ab##","c#d#"))
# print("---")
# print(sol.backspaceCompare("a#c","b"))
# print("---")
print(sol.backspaceCompare("y#fo##f","y#f#o##f"))