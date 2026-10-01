class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m is the number of rows
        # n is the number of columns
        return self.path(m,n)
    
    def path(self,m:int, n:int,i = 0 , j = 0, lookup = None):                
        # i tracks the movmenet of rows, down
        # j tracks the movement of columns, right
        
        lookup = {} if lookup is None else lookup                
        
        if (i,j) in lookup:
            return lookup[(i,j)]
        
        if i == m-1 and j == n -1:
            # One path found
            return 1
                        
        res = 0
        
        # move down
        if i < m -1:
            res += self.path(m,n,i+1,j,lookup)
        
        # move right
        if j < n-1:
            res += self.path(m,n,i,j+1,lookup)
        
        lookup[(i,j)] = res
        return res
            
    
sol = Solution()
print(sol.uniquePaths(3,7))