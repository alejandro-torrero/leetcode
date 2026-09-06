class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j= len(numbers)-1
        
        res = []
        
        while i<=len(numbers)-1:
            sumT = numbers[i]+numbers[j]
            if  sumT == target:
                res=[i+1,j+1]
                break    
            
            if sumT > target:
                j = j-1
                
            if sumT <target:
                i = i+1
            
        return res