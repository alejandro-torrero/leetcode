class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        if nums == []:
            return []
        
        # The empty subset is always considered
        res = [[]]
        
        for n in nums:            
            subsets = []
            for current_subset in res:                       
                
                temp = current_subset.copy()
                
                if current_subset == []:
                    subsets.append([n])
                else:                
                    temp.append(n)                    
                    subsets.append(temp)
                                
            res +=subsets            
        return res
        
sol = Solution()
print(sol.subsets([1,2,3]))