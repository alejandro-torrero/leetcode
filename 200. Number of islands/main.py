class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        
        def dfs(i:int,j:int):
            # Mark this cell as visited
            grid[i][j] = "0"
            
            # Clean adyacent land
            
            if i + 1 < m and grid[i+1][j] != "0":
                dfs(i+1,j)
                
            if j +1 < n and grid[i][j+1] != "0":
                dfs(i,j+1)
                
            if j - 1 >= 0 and grid[i][j-1] != "0":
                dfs(i,j-1)
                
            if i - 1 >= 0 and grid[i-1][j] != "0":
                dfs(i-1,j)
        
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] != "0":
                    # On island found
                    res += 1
                    # Clean adyacent land that is part of the same island
                    dfs(i,j)        
        return res
    
sol = Solution()
print(sol.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))