class Solution(object):
    def convert(self, s, numRows):
        res =[""] * numRows        
        j = 0
        direction = 1 # Start going downward
        
        if numRows == 1:
            return s
        
        for i in range(len(s)):
            
            print("Inserting ",s[i], "into j: ",j)
            res[j] +=s[i]         
            
            if j + 1 == numRows:
                # Change direction
                direction = -1                
            elif i % (numRows*2-2) == 0:
                direction = 1
                
            # Set next j position
            j= j +(1*direction)
            
            print("Next j: ",j)                
        print(res)
        return "".join(res)

            
            
            
sol = Solution()
print(sol.convert("ABC",2))