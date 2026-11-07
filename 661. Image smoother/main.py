import math
class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        m = len(img) # Rows i
        n = len(img[0]) # columns j
        smothedImage = [[0 for _ in range(n)] for _ in range(m)]
        
        print(smothedImage)
        
        # Helper function to get the smothed result
        def smoothCell(i,j):
            # Every cell position that surrounds the cell
            positions = [
                (0,-1), # Left cell
                (0,1), # Right cell
                (-1,0), # Top cell
                (1,0),  # Bottom cell
                (-1,-1), # top left cell
                (-1,1), # top right cell
                (1,-1), # bottom left cell
                (1,1), # bottom right cell
            ]
            
            sum = img[i][j]
            availableCells = 1
            
            for k,l in positions:
                if (i+k) >= 0 and (i+k)<m and (j+l) >=0 and (j+l) < n:
                    # Valid cell found
                    sum += img[i+k][j+l]
                    availableCells +=1
                
            return math.floor(sum/availableCells)
        
        for i in range(m):
            for j in range(n):
                result = smoothCell(i,j)
                smothedImage[i][j] = result
                
        return smothedImage
    
sol = Solution()
print(sol.imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))