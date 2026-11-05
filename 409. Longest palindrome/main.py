class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}
        
        # Base case
        if len(s) == 1:
            return 1
        
        for i in range(len(s)):
            if s[i] in letters:
                letters[s[i]] +=1
            else:
                letters[s[i]]  = 1
                
        # We have two options, build a pailndrome of evenlenght or a palindrome of uneven length
        # To build a palindrome of even length we take every character that appears a multiple of 2 times
        
        # To build an uneven plindrome we can take those letters that appear a multiple of two and then one that appears one time or one that appears 3 times
        
        # Even lenght palindrome
        res = 0
        unevenMatch = False
        
        for letter in letters:                
            if letters[letter] %2 == 0:
                res += letters[letter]
            elif (letters[letter] - 1) % 2 == 0:
                unevenMatch = True
                # Pick the even value of a letter
                res += letters[letter]-1
            
            if letters[letter] == 1:
                unevenMatch=True
                                                     
        
        return res if not unevenMatch else res+1
    
sol = Solution()
print(sol.longestPalindrome("ccc"))