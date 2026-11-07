class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res=0        
        i = 0 # buy pointer
        j = 1 # sell pointer
        
        while j < len(prices):
            # print(i,j, res)
            gains = prices[j] - prices[i]
            
            if prices[i] < prices[j]:
                res = max(gains,res)
            else:
                i = j                                                
            j +=1
                            
        return res
    
sol = Solution()
print(sol.maxProfit([2,1,2,1,0,1,2]))