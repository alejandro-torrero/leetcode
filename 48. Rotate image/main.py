class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        print(matrix)
        m = len(matrix)
        n = len(matrix[0])
        
        # Transpose matrix  
        for i in range(m):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]        
        
        # Reverse
        for i in range(m):
            matrix[i].reverse()


m = [[1,2,3],[4,5,6],[7,8,9]]

sol = Solution()
print(sol.rotate(m))