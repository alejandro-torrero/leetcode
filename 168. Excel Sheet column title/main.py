class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']                
        
        while columnNumber > 0:
            columnNumber -= 1
            
            remainder  = columnNumber % 26
            
            res = letters[remainder] + res
            
            columnNumber = columnNumber // 26
            
        return res
    
    
sol = Solution()
print(sol.convertToTitle(28))