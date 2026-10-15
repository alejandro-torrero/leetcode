class Solution:
    def grayCode(self, n: int) -> list[int]:
        result = []
        total_numbers = 1 << n
        print(total_numbers)

        for i in range(total_numbers):  
            result.append(i ^ (i >> 1))

        return result
    
sol = Solution()

print(sol.grayCode(2))