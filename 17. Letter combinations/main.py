class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        phone_map ={
            '2' :['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r', 's'],
            '8':['t','u','v'],
            '9':['w','x','y','z'],
        }
        
        res = phone_map[digits[0]]

        if len(digits) == 1:
            return res
        
        # For any length larger than 1 we must create the combintatiosn                    
        
        for i in range(1,len(digits)):            
            currentDigits = phone_map[digits[i]]        
            newRes = []
            
            for j in range(len(res)):
                for k in range(len(currentDigits)):
                    newRes.append(res[j]+currentDigits[k])
                    
            res = newRes
            
        return res
        
sol = Solution()
print(sol.letterCombinations('7'))