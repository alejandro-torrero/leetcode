class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        j = 0
        
        while i < len(nums):
            n = nums[i]
            
            if n != val:
                nums[j]=n
                i+=1
                j+=1
                continue
            i+=1
            
        return j           
    

def evaluate(fn,expectedResult,*args):
    res = fn(*args)
    
    if res == expectedResult:
        print("Success run")
    else:
        print(f"Failed. Expected {expectedResult} but recieved {res}")
        
sol = Solution()

evaluate(sol.minMoves,2,[3,2,2,3],3)
evaluate(sol.minMoves,5,[0,1,2,2,3,0,4,2],2)