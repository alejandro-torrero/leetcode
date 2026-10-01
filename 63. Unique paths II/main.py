class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        self.m = len(obstacleGrid)
        self.n = len(obstacleGrid[0])
                
        return self.path(obstacleGrid)
    
    def path(self,grid: list[list[int]], i = 0, j = 0, lookup = None):
        
        lookup = {} if lookup is None else lookup
        
        if (i,j) in lookup:
            return lookup[(i,j)]
        
        if grid[i][j]:
            # Obstacle found
            return 0
        
        if i == self.m -1 and j == self.n -1:
            # We got to the end
            return 1
        
        
        # Decide how to move
        
        res = 0
        if i < self.m -1:
            res += self.path(grid,i+1,j,lookup)
        
        if j < self.n -1:
            res += self.path(grid,i,j+1,lookup)
        
        lookup[(i,j)] = res
        return res
        



grid = [[0,0,0],[0,1,0],[0,0,0]]    
sol = Solution()
print(sol.uniquePathsWithObstacles(grid))