class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        m = len(arr1)
        n = len(arr2)
        
        res = 0
        
        for i in range(m):
            check = False
            for j in range(n):
                if abs(arr1[i]-arr2[j])<= d:
                    check=True
                    break
                
            if not check:
                res+=1
                
        return res        
    
sol = Solution()
print(sol.findTheDistanceValue([4,5,8],[10,9,1,8],2))