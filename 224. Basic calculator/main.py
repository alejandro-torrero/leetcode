class Solution:
    def calculate(self, s: str) -> int:
        # Remove every whitespace 
        
        s = "".join(s.split())

        if s == "":
            return 0                
        
        stack = []
        res = 0
        i = 0
        num = 0
        sign = 1
        
        while i < len(s):
            if s[i].isdigit():
                # Save number for next operation
                num = num * 10 + int(s[i])
            elif s[i] in "+-":
                # Push previous num into the stack
                res += num * sign
                sign = 1 if s[i] == "+" else -1
                num = 0
            elif s[i] == "(":
                # Recursive call
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1 
            elif s[i] == ")":
                # Finish and return
                res = res + num * sign
                num = 0 
                    
                res *=stack.pop() # Pop sign
                res += stack.pop() # Last result
            
            # Handel counter increase
            i += 1
                
        return res + num * sign
    
    
def evaluate(fn,expectedResult, *args):
    res = fn(*args)
    
    if res == expectedResult:
        print(f"Sucessful run. Result: {res}\n")
    else:
        print(f"Failed. Expected {expectedResult} but got {res} with args {args[0]}\n")
        
        
sol = Solution()

evaluate(sol.calculate,0,"  ")
evaluate(sol.calculate,2,"1 + 1")
evaluate(sol.calculate,0,"1 - 1")
evaluate(sol.calculate,3," 2-1 + 2 ")
evaluate(sol.calculate,16,"1 + (10 + 5- 2) + 2")
evaluate(sol.calculate,-10,"1 -11")
evaluate(sol.calculate,10,"5 +(5)")
evaluate(sol.calculate,-1,"-2 +1")
evaluate(sol.calculate,-2,"(6)-(8)-(7)+(1+(6))")
evaluate(sol.calculate,-15,"2-4-(8+2-6+(8+4-(1)+8-10))")
# evaluate(sol.calculate,23,"(1+(4+5+2)-3)+(6+8)")