import time

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        
        for i,a in enumerate(nums):            
            if i > 0 and a == nums[i-1]:
                # Skipp repeated execution
                continue
            
            l=i+1
            
            r = len(nums)-1
            
            while l < r:
                sumT = a+nums[l]+nums[r]
                
                if  sumT == 0:
                    res.append([a,nums[l],nums[r]])
                    l =l +1
                    while nums[l] == nums[l-1] and l < r:
                        l +=1        
                
                if sumT > 0:
                    r = r-1
                    
                if sumT < 0:
                    l = l+1
                
        return res
            
    


def evaluate (fn,expected_result,*args):
    start = time.time()
    res = fn(*args)
    
    if res != expected_result:
        print(f"Run failed. Expected {expected_result} but got {res}. t: {(time.time()-start):.5f}s")
    else:
        print("Sucessful run!!")
        

sol = Solution()
evaluate(sol.threeSum,[[-1,-1,2],[-1,0,1]],[-1,0,1,2,-1,-4])