class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        arr1 = []
        arr2 = []
        
        for val in nums:
            
            if len(arr1) == 0:
                arr1.append(val)
                continue
            
            if len(arr2) == 0:
                arr2.append(val)
                continue
            
            if arr1[-1] > arr2[-1]:
                arr1.append(val)
            else:
                arr2.append(val)
            
        return arr1 + arr2
            
            
            
sol = Solution()
print(sol.resultArray([5,4,3,8]))