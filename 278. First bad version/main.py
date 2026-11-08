# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


def isBadVersion(n):
    return n >= 67483

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        
        lastBadVersion = -1
        start = 1
        end = n
        
        
        while start <= end:
            mid = start +(end-start)//2             
            
            if isBadVersion(mid):                
                lastBadVersion = mid
                end = mid - 1
            else:
                # Move forward on the left
                start = mid + 1
                
        return lastBadVersion


sol = Solution()
print(sol.firstBadVersion(1308394617183120))