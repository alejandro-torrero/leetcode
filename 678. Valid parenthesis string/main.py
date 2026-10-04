class Solution:
    def checkValidString(self, s: str) -> bool:
        return self.check(s)
    
    def check(self, s,opc = 0, i =0, lookup = None):        
        # opc = open parenthesis count
        # i = index        
        
        lookup = {} if lookup is None else lookup
        
        if (opc,i) in lookup:
            return lookup[(opc,i)]
        
        # Base cases #
        
        # Got to the end of the string
        if i == len(s):
            return opc == 0
        
        if opc == 0 and s[i] == ")":
            # We cannot take a close parenthesis by having o on opc
            # This run is an invalid parenthesis string
            print("This string is unsolvable")
            return False
        
        if opc > len(s) - i:
            # There are not enough chars to get a valid parenthesis string
            return False
        
        # Decide how to advance #
        
        res = False
        
        if s[i] == "(":
            res = res or self.check(s,opc+1,i+1,lookup)
            
        
        if s[i] == ")":
            res = res or self.check(s,opc-1,i+1,lookup)
            
        if s[i] == "*":
            # Asterisk could mean 3 possibilities: open parenthesis, close parenthesis or empty string
            
            if opc > 0:
                # Try close parenthesis
                res = res or self.check(s,opc-1,i+1,lookup)
                
            # Trye remaining two
            res = res or self.check(s,opc,i+1,lookup) or self.check(s,opc+1,i+1,lookup)
        
        lookup[(opc,i)] = res
        return res                            
            
    
sol = Solution()
print(sol.checkValidString("(*)"))