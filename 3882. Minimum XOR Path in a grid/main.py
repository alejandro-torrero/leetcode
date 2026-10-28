class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid) # i - rows
        n = len(grid[0]) # j - columns        
        lookup = {}
        
        # Recursive function to move trhough the grid
        def move(i:int, j: int,):                        
            if (i,j) in lookup:
                return lookup[(i,j)]
            
            if i == m -1 and j == n -1:                
                return {grid[i][j]}
            
            # Move. There are only two movements: right or down            
            results = set()
            
            # Evaluate down
            if i+1 < m:
                for value in move(i + 1, j):
                    results.add(grid[i][j] ^ value)
            
            # Evaluate right
            if j + 1 < n:
                for value in move(i, j + 1):
                    results.add(grid[i][j] ^ value)
                
            lookup[(i,j)] = results            
            return lookup[(i,j)]
                                       
        return min(move(0, 0))
    
sol = Solution()
print(sol.minCost([[11,10,4],[19,9,13]]))