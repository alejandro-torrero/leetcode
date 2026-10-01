class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        self.m = len(grid) # Number of rows
        self.n = len(grid[0]) # Number of columns
        
        return self.path(grid)
    
    def path(self,grid:list[list[int]], i = 0, j = 0, lookup = None):
        lookup = {} if lookup is None else lookup
        
        if (i,j) in lookup:
            return lookup[(i,j)]
        
        if i == self.m - 1 and j == self.n - 1:
            # He have reached the end
            return grid[i][j]
        
        # Decide where to move
        
        res = float('inf')
        
        if i < self.m -1:
            # Move down
            res = min(res,grid[i][j]+self.path(grid,i+1,j,lookup))
        
        if j < self.n -1:
            # Move right
            res = min(res,grid[i][j]+self.path(grid,i,j+1,lookup))
        
        lookup[(i,j)] = res
        return res
    
    
sol = Solution()
print(sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))