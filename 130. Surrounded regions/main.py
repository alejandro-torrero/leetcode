class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        def dfs(i: int, j: int) -> None:
            if (i < 0 or i >= m or j < 0 or j >= n
                    or board[i][j] != "O"):
                return

            # Mark cell as visited and safe
            board[i][j] = "S"

            for di, dj in directions:
                dfs(i + di, j + dj)          
        
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)
        
        # If a cell stood on S, then it didnt got updated at the end
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"
    
sol = Solution()
board= [["X","O","O","X","X","X","O","X","O","O"],
        ["X","O","X","X","X","X","X","X","X","X"],
        ["X","X","X","X","O","X","X","X","X","X"],
        ["X","O","X","X","X","O","X","X","X","O"],
        ["O","X","X","X","O","X","O","X","O","X"],
        ["X","X","O","X","X","O","O","X","X","X"],
        ["O","X","X","O","O","X","O","X","X","O"],
        ["O","X","X","X","X","X","O","X","X","X"],
        ["X","O","O","X","X","O","X","X","O","O"],
        ["X","X","X","O","O","X","O","X","X","O"]]
print(sol.solve(board))
print(board)