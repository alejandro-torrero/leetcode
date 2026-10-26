class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m = len(grid) # Rows
        n = len(grid[0]) # columns
        res = 0
        
        def dfs(i: int,j:int):
            # Check 3 directions
            currentTotal = grid[i][j]
            # Reset grid value in order to avoid coming back to it
            grid[i][j] = 0
            
            # Test for each adyacent direction to this cell
            if i + 1 < m and grid[i+1][j] != 0:
                # Move down
                currentTotal += dfs(i+1,j)

            if j+1 < n and grid[i][j+1] != 0:
                # Move right
                currentTotal += dfs(i,j+1)
                
            if i - 1 >=0 and grid[i-1][j] != 0:
                # Move up
                currentTotal += dfs(i-1,j)
                
            if j -1 >= 0 and grid[i][j-1] != 0:
                # Move left
                currentTotal += dfs(i,j-1)
                                
                
            return currentTotal
                            
    
        for i in range(m):
            for j in range(n):                
                if grid[i][j] != 0:
                    res += 1 if dfs(i,j) % k == 0 else 0
        return res
    
    
sol = Solution()
print(sol.countIslands([[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]],5))