class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)      # rows i
        n = len(board[0])   # columns j                
        
        # So, search is a recurisve function that will be used to check every adyacent cell to validate if a match can be found
        def search(i: int, j: int, letteridx:int):
            # Represent that this cell is already checked
            originalValue = board[i][j]
            board[i][j] = '#'
            
            if letteridx == len(word):
                # got to the end
                return True
            
            # Check in all four directions to determine if we can build the word
            res = False
            
            # Check right
            if j + 1 < n and board[i][j+1] == word[letteridx]:
                res = res or search(i,j+1,letteridx+1)
                
            # Check down
            if i+1 < m and board[i+1][j] == word[letteridx]:
                res = res or search(i+1,j,letteridx+1)
            
            # Check left
            if j -1 >= 0 and board[i][j-1] == word[letteridx]:
                res = res or search(i,j-1,letteridx+1)
                
            # check up
            
            if i -1 >= 0 and board[i-1][j] == word[letteridx]:
                res = res or search(i-1,j,letteridx+1)
                
            board[i][j] = originalValue
            return res
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    # First letter found, search for the rest
                    result = search(i,j,1)
                    
                    if result:
                        return True
                    
        return False
    
    
sol = Solution()
print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"XBCCED"))