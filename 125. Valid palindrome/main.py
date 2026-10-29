class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Set lower cases
        s = s.lower()
        
        # Remove non alpha numeric characters
        s = ''.join([i for i in s if i.isalpha() or i in ['0','1','2','3','4','5','6','7','8','9']])
        # Validate palindrome         
  
        if len(s) == 0:
            return True
        
        i = 0
        j = len(s)-1
        
        while i < j:            
            if s[i] != s[j]:
                return False
            j -= 1
            i += 1
         
        return True
    
    
sol = Solution()
# print(sol.isPalindrome("A man, a plan, a canal: Panama"))
# print(sol.isPalindrome(" "))
print(sol.isPalindrome("0P"))