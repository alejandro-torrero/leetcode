class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        auxGrid = [["#" for _ in range(n)] for _ in range(m)]
        
        i, j = 0,0   
        auxGrid[i][j] = "."
        
        def move(i,j, order):
            auxGrid[i][j] = "."
            
            if i == m -1 and j == n-1:                
                return                                        
                
            if order == 1:
                # Move j
                if j+1 < n:
                    move(i,j+1,0)
                elif i + 1 < m:
                    move(i+1,j,1)                    
            else:
                # Move i                
                if i+1 <m:
                    move(i+1,j,1)
                elif j+1 < n:
                    move(i,j+1,0)                                    
                    
                # Start by moving i
        
        move(i,j,0)         
        
        return [ "".join(r) for r in auxGrid]


    
    
sol = Solution()
print(sol.createGrid(14,1))