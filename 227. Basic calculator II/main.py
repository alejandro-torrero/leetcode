class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        num = 0
        op = None

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)

            elif c in "+-*/":
                if op == "*":
                    num = stack.pop() * num
                    op = None

                elif op == "/":
                    num = int(stack.pop() / num)
                    op = None

                if c in "+-":
                    stack.append(num * sign)
                    sign = 1 if c == "+" else -1

                else:
                    stack.append(num * sign)
                    sign = 1
                    op = c

                num = 0

        if op == "*":
            num = stack.pop() * num
        elif op == "/":
            num = int(stack.pop() / num)

        stack.append(num * sign)

        return sum(stack)
    
sol = Solution()
print(sol.calculate("14-3/2"))