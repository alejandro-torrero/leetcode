import math

# For any two positive integers a and b, the identity a×b=gcd(a,b)×lcm(a,b) always holds.
# Therefore, every subarray of length 2 is automatically product-equivalent

class Solution:
    def maxLength(self, nums: list[int]) -> int:        
        res = 0
        j = len(nums)-1
        
        for i in range(len(nums)):
            prod = nums[i]
            gcd = nums[i]
            lcm = nums[i]
            
            for j in range(i+1,len(nums)):
                prod = prod * nums[j]
                gcd = math.gcd(gcd,nums[j])
                lcm = math.lcm(lcm,nums[j])
                
                
                if prod > gcd * lcm:
                    break;
                if prod == gcd * lcm:
                    res = max(res,j-i+1)
                
        return res
    
sol = Solution()
print(sol.maxLength([1,2,1,2,1,1,1]))