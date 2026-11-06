class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        m = len(g)
        n = len(s)
        
        # Sort arrays so that we can try to satisfy the gridiest first
        g.sort(reverse=True)
        s.sort(reverse=True)

        i,j = 0,0
        res = 0
        
        while i < m and j < n:
            # Compare current kid greed to the biggest cookie
            if s[j] >= g[i]:
                # We can satisfy this kid, advance on both pointers
                res +=1
                i += 1
                j += 1
            else:
                # We cannot content this kid, lets try to give this cookie to the next kid
                i+=1
        
        return res
        
    
    
sol = Solution()
print(sol.findContentChildren([1,2,3],[1,1]))
print(sol.findContentChildren([1,2],[1,2,3]))