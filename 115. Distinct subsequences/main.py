import time

class Solution:
    def numDistinct(self, s: str, t: str) -> int:        
        return self.countSub(s,t)
    
    # t is the goal subsequence to get to
    def countSub(self,s:str, t:str,currentStr = "", i: int = 0, lookup = None):
        lookup = {} if lookup is None else lookup
        
        if (currentStr,i) in lookup:
            return lookup[currentStr,i]
        
        if currentStr == t:            
            return 1
        
        # First base case, when we reach the end of the array
        if i == len(s):
            return 0
        
        # We have two options, to take or not a specific char
        # But we should evaluate if this currentStr is atleast some what similar
        
        if not t.startswith(currentStr):
            print(f"{s} does not starts with {currentStr} ignored")
            return 0
        
        lookup[(currentStr,i)] = self.countSub(s,t,currentStr+s[i],i+1,lookup) + self.countSub(s,t,currentStr,i+1,lookup)
        return lookup[(currentStr,i)]
    
    
sol = Solution()
start = time.time()
print(sol.numDistinct("rabbbit","rabbit"))
print(f"It took {time.time()-start} seconds.")

# 0.0002422332763671875
# 0.00022029876708984375