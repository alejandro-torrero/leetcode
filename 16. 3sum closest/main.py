class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        res = float('inf')
        nums.sort()
        print(nums)
        
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i -1]:
                # Skip repeated number
                continue
            # print("Processing for: ",n)
            left = i+1
            right = len(nums)-1
            
            while left < right:
                totalSum = n + nums[left] + nums[right]
                print(f"Subrpocessing l:{left} r:{right} totalSum: ", totalSum)         
                
                # 1. The sum is the exact value of target, there's no need to keep searching
                if totalSum == target:
                    res = totalSum
                    break;                     
                
                # 2. Validate if the actual totalSum is closer to abs than the gloab response
                if abs(target - totalSum) < abs(target-res):
                    # print("Setting totalsum", totalSum)
                    res = totalSum
                
                # 3. Move index
                # if totalSum is zero we dont really have a hint to know where to move, so we check if target is
                # more positive or more negative
                if totalSum == 0 and target > 0:
                    left = left +1
                    continue
                elif totalSum == 0 and target < 0:
                    right = right -1
                    continue
                
                if totalSum < target:
                    # Move left counter
                    left = left+1
                
                if totalSum > target:
                    right = right-1
        
        return res
    

def evaluate(fn, expectedResult, *args):
    res = fn(*args)
    
    if res == expectedResult:
        print("Sucessful run")
    else:
        print(f"Failed run. Expected {expectedResult} but recieved {res}")

        
sol = Solution()

# evaluate(sol.threeSumClosest,2,[-1,2,1,-4],1)
# evaluate(sol.threeSumClosest,0,[0,0,0],1)
# evaluate(sol.threeSumClosest,1,[1,1,-1,3,1,4,5,1,2],1)
evaluate(sol.threeSumClosest,1,[4,0,5,-5,3,3,0,-4,-5],-2)