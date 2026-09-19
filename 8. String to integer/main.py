class Solution:
    def myAtoi(self, s: str) -> int:
        res=0
        sign = 1        
        i = 0
        n = len(s)
        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
                
        # Ignore tralingin zeros
        while i < n and s[i] == " ":
            i = i+1
        
        print(i)
        
        # Validate if we are at the end of the string
        if i  == n:
            return res
        
        # Detect the sign
        if s[i] == "+":
            i = i+1
        elif s[i] == "-":
            sign = -1
            i = i+1
            
        # Detect numbers
        while i < n and s[i].isdigit():
            digit = int(s[i])
            res = res * 10 + digit
            
            if sign * res <= INT_MIN:
                return INT_MIN
            if sign * res >= INT_MAX:
                return INT_MAX
            
            i += 1
                         
        return res * sign
    
    
def evaluate(fn, expectedResult, *args):
    res = fn(*args)
    if res == expectedResult:
        print("Sucess run")
    else:
        print(f"Failed run. Expected {expectedResult} but recieved {res}")
        
        
sol = Solution()

evaluate(sol.myAtoi,0,"   ")
evaluate(sol.myAtoi,42,"42")
evaluate(sol.myAtoi,-42,"   -042")
evaluate(sol.myAtoi,1337,"1337c0d3")
evaluate(sol.myAtoi,0,"0-1")
evaluate(sol.myAtoi,0,"words and 987")
