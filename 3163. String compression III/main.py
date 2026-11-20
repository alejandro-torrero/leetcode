class Solution:
    def compressedString(self, word: str) -> str:
        res = ""
        MAX_LEN = 9
        lastChar = None
        count = 0

        for i in range(len(word)):
            c = word[i]
            
            if c == lastChar:
                if count == MAX_LEN:
                    # Insert current char data
                    res += f"9{c}"
                    # Reset counter
                    count = 1
                else:
                    count += 1                
            else:
                if count > 0:
                    res += f"{count}{lastChar}"
                
                lastChar = c
                count = 1          
                
        res += f"{count}{lastChar}"                          
        
        return res
    
sol = Solution()
print(sol.compressedString("abcde"))
print("------")
print(sol.compressedString("aaaaaaaaaaaaaabb"))