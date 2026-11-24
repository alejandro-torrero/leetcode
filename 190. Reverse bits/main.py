class Solution:
    def reverseBits(self, n: int) -> int:        
        res = 0
        
        # Go thrugh all 32 bits of the numebr
        for _ in range(32):
            # Left shift to the response to add a number
            res <<= 1
            
            # If current bit of n is 1
            if (n & 1) == 1:
                res |= 1
                
            # Right shift of the response
            n >>= 1
            
        return res
                

sol = Solution()
print(sol.reverseBits(43261596))