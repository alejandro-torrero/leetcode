class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        res = ["#" for _ in range(len(s))]
        
        for i in range(len(indices)):
            idx = indices[i]
            res[idx] = s[i]
            
        return "".join(res)
    
    
sol = Solution()
print(sol.restoreString("codeleet",[4,5,6,7,0,2,1,3]))