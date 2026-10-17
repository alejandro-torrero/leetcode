class Solution:
    def trap(self, height: list[int]) -> int:
        i = 0
        j = len(height) -1
        
        lMax = 0
        rMax = 0
        
        res = 0
        
        while i< j:
            lMax = max(lMax,height[i])
            rMax = max(rMax,height[j])
            print(res)
            if lMax < rMax:
                res += lMax-height[i]
                i += 1
            else:
                res = rMax-height[j]
                j -=1
            print(i,j)
        return res
    
    
sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))