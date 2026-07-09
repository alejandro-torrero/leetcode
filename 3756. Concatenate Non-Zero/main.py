# Not efficient enough

class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res = []
        for i in range (len(queries)):
            ## Go through every query interval
            
            bLimit = queries[i][0]
            tLimit = queries[i][1]+1            
            
            substring = s[bLimit:tLimit]
            
            x=""
            sum=0
            for j in range(len(substring)):
                if substring[j] != "0":
                    x += substring[j]
                    sum += int(substring[j])
            
            res.append((int(x or 0)*sum) % (10**9 +7))
        
        return res
            

sol= Solution()
print(sol.sumAndMultiply("10203004",[[0,7],[1,3],[4,6]]))
print(sol.sumAndMultiply("1000",[[0,3],[1,1]]))
print(sol.sumAndMultiply("9876543210",[[0,9]]))