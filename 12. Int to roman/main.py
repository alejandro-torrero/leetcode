class Solution:
    def intToRoman(self, num: int) -> str:
        numStr = f'{num}'.rjust(4,'0')
        
        res =''
        
        for i in range(len(numStr)):
            if i == 0 and numStr[i] != 0:
                # 1000
                res += 'M' * int(numStr[i])
                pass
                
            if i == 1 and numStr[i] != 0:
                # 100
                res += self.substract(int(numStr[i])*100)
                pass
            
            if i == 2 and numStr[i] != 0:
                # 10
                res += self.substract(int(numStr[i])*10)
                pass
                
            if i == 3:
                # 1
                res += self.substract(int(numStr[i]))
                pass
             
        
        return res
    
    # Helper function to determine what nmumbers we need to substract
    def substract(self,num: int):        
        availableNumbers = [1000,500,100,50,10,5,1]
        rommanAvailableNumbers = ['M','D','C','L','X','V','I']
        numbers = ''        
        
        while num >0:
            if num == 4 or num == 9:
                numbers += 'I'
                num=num+1
                
            if num == 40 or num == 90:
                numbers += 'X'
                num = num +10
            
            if num == 400 or num == 900:
                numbers += 'C'
                num = num + 100
                
            for i in range(len(availableNumbers)):
                if num >= availableNumbers[i]:
                    num = num - availableNumbers[i]
                    numbers += rommanAvailableNumbers[i]
                    break            
        return numbers
    
    
sol = Solution()
print(sol.substract(900))
# print(sol.intToRoman(3749))
# print(sol.intToRoman(3749))
# print(sol.intToRoman(1994))