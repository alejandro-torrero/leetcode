class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        res = 0
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        arrive_alice_month = int(arriveAlice.split("-")[0])
        arrive_alice_day = int(arriveAlice.split("-")[1])
        leave_alice_month = int(leaveAlice.split("-")[0])
        leave_alice_day = int(leaveAlice.split("-")[1])
                
        
        arrive_bob_month = int(arriveBob.split("-")[0])
        arrive_bob_day = int(arriveBob.split("-")[1])
        leave_bob_month = int(leaveBob.split("-")[0])
        leave_bob_day = int(leaveBob.split("-")[1])    
        
        is_alice_present = False       
        is_bob_present = False    
        
        for month in range(12):
            for day in range(1,days_per_month[month]+1): 
                print(month+1,day)               
                
                if month +1 == arrive_alice_month and day == arrive_alice_day:
                    # Allice arrived
                    is_alice_present = True
                
                if month +1 == arrive_bob_month and day == arrive_bob_day:
                    # Bob arrived
                    is_bob_present = True
                                                                    
                if is_alice_present and is_bob_present:
                    res +=1                    
                
                # Check if this was their last day
                
                if month +1 == leave_alice_month and day == leave_alice_day:
                    is_alice_present = False
                
                if month +1 == leave_bob_month and day == leave_bob_day:
                    is_bob_present = False
                
        return res

    
sol = Solution()
print(sol.countDaysTogether("08-15","08-18","08-16","08-19"))