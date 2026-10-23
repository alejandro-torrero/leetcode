class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j = 0,0
        turn = 1
        res = ""
        while i < len(word1) or j < len(word2):
            if i < len(word1) and turn == 1:
                res += word1[i]
                i += 1
                turn = 0 if j < len(word2) else 1
                continue
            
            if j < len(word2) and turn == 0:
                res += word2[j]
                j+=1
                turn = 1 if j < len(word1) else 0
                
        return res
                
sol = Solution()
print(sol.mergeAlternately("abc","pqr"))