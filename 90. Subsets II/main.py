class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        if nums == []:
            return []
        
        nums.sort()
        
        # The empty subset is always considered
        res = [[]]
        
        for n in nums:            
            subsets = []
            for current_subset in res:                       
                
                temp = current_subset.copy()
                
                if current_subset == []:
                    if [n] in res: continue
                    subsets.append([n])
                else:
                    temp.append(n)                 
                    if temp in res: continue
                    subsets.append(temp)
                                
            res +=subsets            
        return res
        
sol = Solution()
print(sol.subsetsWithDup([4,4,4,1,4]))