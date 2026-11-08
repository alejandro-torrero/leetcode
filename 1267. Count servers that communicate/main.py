class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        res = 0
        m = len(grid)       # Rows i
        n = len(grid[0])    # columns j
        
        rows = [0 for _ in range(m)]
        columns = [0 for _ in range(n)]
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    rows[i] += 1
                    columns[j] += 1                
        
        for i in range(m):
            row = grid[i]
            for j in range(n):
                server = grid[i][j]
                if server and rows[i] + columns[j] >2:
                    res +=1                
        return res
    
sol = Solution()
print(sol.countServers([[1,0],[0,1]]))
print("---")
print(sol.countServers([[1,0],[1,1]]))
print("---")
print(sol.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))
print("---")
print(sol.countServers([[1,0,0,1,0],[0,0,0,0,0],[0,0,0,1,0]]))