class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digitSum = 0
        digitProd = 1

        for num in str(n):
            digitSum += int(num)
            digitProd *= int(num)
            
        print(digitProd,type(digitProd))
        print(digitSum,type(digitSum))
        return n%(digitSum + digitProd)==0
    
    
sol = Solution()
print(sol.checkDivisibility(99))