class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:                
        
        # Number of rows
        n = len(grid)
        # Number of columns
        m = len(grid[0])
        
        self.lookup = {}
        
        path = n + m -1
        if path % 2:
            # There's not feasible path
             return False         
         
        return self.dfs(grid)
                       
    
    def dfs(self,grid: list[list[str]],op = 0,i = 0, j = 0):                                        
        print(f"Processing [{i}][{j}]: {grid[i][j]} op:{op}")        
        state = (i, j, op)
        
        if state in self.lookup:
            return self.lookup[(state)]        
        
        operation = 1 if grid[i][j] == "(" else -1
        op = op + operation
        
        n = len(grid) - 1 # Number of rows
        m = len(grid[0]) - 1 # Number of columns
        
        # Base cases                                        
                
        # If op is negative, it means we cannot take this path as it is an invalid parenthesis string
        if op < 0:
            self.lookup[state] = False 
            return False
        
        # Number of moves remaining after this position
        remaining = (n - i) + (m - j)
        
        if op > remaining:
            # There are not enough cells to complete a valid parenthesis string
            self.lookup[state] = False
            return False
        
        
        # We have reached the end
        if i == n and j == m:
            self.lookup[state] = op == 0
            return op == 0                    
        
        # Move forward on the grid
        
        result = False
        
        # Validate 2 possible moves: down, right        
        # Down
        if i < n and self.dfs(grid,op,i + 1, j):
            self.lookup[state] = True
            return True

        # Try moving right.
        if j < m and self.dfs(grid,op,i, j + 1):
            self.lookup[state] = True
            return True                         
        
        self.lookup[state] = False
        return False      
    
    
grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]

sol = Solution()
print(sol.hasValidPath(grid))