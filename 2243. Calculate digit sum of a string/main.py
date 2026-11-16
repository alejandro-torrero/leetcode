class Solution:
    def digitSum(self, s: str, k: int) -> str:
        res = s
        
        while len(res) > k:            
            substrings = []
            for i in range(0,len(res),k):
                substring = res[i:i+k]                
                sumSubstring = 0     
                for j in range(len(substring)):
                    sumSubstring += int(substring[j])
                substrings.append(str(sumSubstring))
            
            res = ''.join(substrings)                        
            
        return res
    
    
sol = Solution()
print(sol.digitSum("11111222223",3))