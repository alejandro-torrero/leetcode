class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1

        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        # Extract the answer simbol
        isPositive = (
            True
            if ((dividend > 0 and divisor > 0) or dividend < 0 and divisor < 0)
            else False
        )

        a = abs(dividend)
        b = abs(divisor)

        res = 0

        while a >= b:
            q = 0
            while a > (b << q + 1):
                q += 1

            res += 1 << q
            a = a - (b << q)

        if res > INT_MAX and isPositive:
            return INT_MAX

        if res < INT_MIN and not isPositive:
            return INT_MIN

        return res if isPositive else -res

    
sol = Solution()
print(sol.divide(58,5))