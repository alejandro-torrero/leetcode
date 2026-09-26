class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Parse array to dict
        vars = {}
        for k in knowledge:
            vars[k[0]] = k[1]
                                
        # Process string
        
        readingVar = False
        var = ""
        res = ""
        
        for i in range(len(s)):
            c = s[i]            
            
            if c == "(":
                readingVar = True
                continue
                            
            if c == ")":
                # Finish reading var, replace
                readingVar = False
                # Search var
                if var in vars:
                    res += vars[var]    
                else:
                    res+="?"                                    
                var = ""
                continue
                
            if readingVar:
                var += c
            else:
                res +=c
                
        return res
    
sol = Solution()
# print(sol.evaluate("(names)is(age)yearsold",[["name","bob"],["age","two"]]))
print(sol.evaluate("hi(name)",[["a","b"]]))