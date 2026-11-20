class Solution:
    def compress(self, chars: list[str]) -> int:
        insertIdx = 0
        lastChar = None
        lastCharCount = 0
        
        if len(chars) == 1:
            return 1
        
        for i in range(len(chars)):
            c = chars[i]
            
            if c == lastChar:
                lastCharCount += 1
            else:
                if lastCharCount != 0:                    
                    chars[insertIdx] = lastChar
                    insertIdx += 1
                    if lastCharCount > 1:
                        for j in range(len(str(lastCharCount))):                            
                            chars[insertIdx] = str(lastCharCount)[j]
                            insertIdx += 1                                                    
                            
                
                lastCharCount = 1
                lastChar = c
                
        if lastCharCount != 0:
            chars[insertIdx] = lastChar
            insertIdx += 1
            if lastCharCount > 1:
                for j in range(len(str(lastCharCount))):                            
                    chars[insertIdx] = str(lastCharCount)[j]
                    insertIdx += 1      
                
        del chars[insertIdx:]
        print(chars)
        
        return len(chars)
    
    
sol = Solution()
print(sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))