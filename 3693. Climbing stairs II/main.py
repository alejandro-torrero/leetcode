class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        res = float('inf')
        lookup = {}
        def climb(i,j):
            # print('Climbing', i,j)
            cost = costs[j-1] +(j-i)**2
            tpl = (i,j)
            
            if tpl in lookup:
                return lookup[tpl]
            
            if j == n:
                # We are at the end      
                lookup[tpl] = cost  
                return cost
            
            internalCost = float('inf')
            
            # Evaluate next climb
            if j + 1 <= n:
                internalCost = min(internalCost,cost+climb(j,j+1))                
                
            if j + 2 <= n:
                internalCost = min(internalCost,cost+climb(j,j+2))
                            
            if j + 3 <= n:
                internalCost = min(internalCost,cost+climb(j,j+3))
            
            lookup[tpl] = internalCost
            return internalCost
        
        for i in range(1,4):
            # Test the climb to every 3 possible jump            
            # Starting at i = 0, you can decide to jump in 3 options            
            if i <= n:
                res = min(res,climb(0,i))
            
        return res
    
    
sol = Solution()
print(sol.climbStairs(4,[1,2,3,4]))