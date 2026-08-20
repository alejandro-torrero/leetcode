class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0 # First pointer        
        j = len(height)-1 # Last pointer
        
        maxArea = 0
        
        # Height length will always be > 2, so there´s no use in validating its length
        
        while i < j:
            p1 = height[i]
            p2 = height[j]
            
            area= self.calculateArea(i+1,0,j+1,min(p1,p2))            
            
            maxArea = max(maxArea,area)
            
            if p1 > p2:
                # Adanvce on j
                j=j-1
            else:
                i=i+1
            
            pass
        
        return maxArea
        
    def calculateArea(self,x1,y1,x2,y2)->int:
        area = abs(x2-x1) * abs(y2-y1)
        return area
         


sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
print(sol.maxArea([1,1]))