class Solution:
    def minimumSum(self, nums: list[int]) -> int:
        sum = float('inf')
        
        for i in range(len(nums)):
            a = nums[i]
            for j in range(i+1,len(nums)):
                b = nums[j]
                for k in range(j+1,len(nums)):
                    c = nums[k]
                    print("Processing",[i,j,k],a+b+c)
                    if i < j and j < k and a<b and c<b:
                        sum = min(sum,a+b+c)
        
        if sum == float('inf'):
            return -1
        else:
            return sum
    
sol = Solution()

print(sol.minimumSum([5,4,8,7,10,2]))