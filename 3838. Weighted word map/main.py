class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:  
        res = ""
        letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        letters_reversed = letters.copy()
        letters_reversed.reverse()
        
        for i in range(len(words)):
            currentSum = 0
            for j in range(len(words[i])):
                letter = words[i][j]
                currentSum += weights[letters.index(letter)]
            
            # Map to new letter
            modulo = currentSum % 26            
            decoded = letters_reversed[modulo]
            res +=decoded
            
        return res
    
sol = Solution()
print(sol.mapWordWeights(["abcd","def","xyz"],[5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]))
