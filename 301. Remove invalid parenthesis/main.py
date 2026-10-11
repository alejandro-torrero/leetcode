class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:        
        self.res = set()
        self.minRemoved = float('inf')
        
        self.removeParenthesis(s)
        
        return list(self.res)
        
    def removeParenthesis(self,s:str, i = 0,opc = 0,cpc=0, expression = [],remove_count = 0):
        # i: index to go trough the array
        # opc: open parenthesis count
        # cpc: close parenthesis count
        
        if i == len(s):
            # End of the string, evaluate if its valid
            if opc == cpc:
                # Valid parenthesis string
                
                if remove_count <= self.minRemoved:
                    # This is a good final expression
                    ans = "".join(expression)
                    
                    if remove_count < self.minRemoved:
                        # Set new value and reset result as it might have longer expressions
                        self.res= set()
                        self.minRemoved = remove_count
                        
                    self.res.add(ans)                    
                                         
        else:           
            if s[i] != "(" and s[i] != ")":
                # The character being a letter, is added to the result
                expression.append(s[i])
                self.removeParenthesis(s,i+1,opc,cpc,expression,remove_count)
                expression.pop()
            else:
                
                # First approach is to ignore this parenthesis and keep going
                self.removeParenthesis(s, i + 1, opc, cpc, expression, remove_count + 1)
                
                # Second, we do consider the parenthesis
                
                # Process parenthesis string
                expression.append(s[i])
                
                if s[i] == "(":
                    self.removeParenthesis(s,i+1,opc+1,cpc,expression,remove_count)
                elif cpc<opc:
                    self.removeParenthesis(s,i+1,opc,cpc+1,expression,remove_count)
                    
                expression.pop()
            
sol = Solution()
print(sol.removeInvalidParentheses("()())()"))