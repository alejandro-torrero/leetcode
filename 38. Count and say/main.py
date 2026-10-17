class Solution:
    def countAndSay(self, n: int,iteration = 1, rle = "") -> str:        
        if n+1 == iteration:
            return rle
        
        if rle == "":
            # First iteration
            return self.countAndSay(n,iteration+1,"1")
                
        current_num=""
        current_num_count = 0
        local_rle = ""
        for i in range(len(rle)):            
            if current_num == "":
                # First number
                current_num = rle[i]
                current_num_count =1
                # Skip following logic
                continue            
            
            if current_num != rle[i]:
                # Detected a new number, fill RLE
                local_rle += str(current_num_count)+current_num                
                # Reset counters
                current_num = rle[i]
                current_num_count= 1
                continue
            
            if current_num == rle[i]:
                current_num_count +=1
        
        if current_num != "":                    
            local_rle+= str(current_num_count)+ current_num            
            
        return self.countAndSay(n, iteration+1,local_rle)
    
    
sol = Solution()
print(sol.countAndSay(3))