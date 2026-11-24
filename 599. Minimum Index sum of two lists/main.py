class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        res = []
        leastIndexSum = float('inf')
        map1 = {}
        
        for i in range(len(list1)):
            map1[list1[i]] = i
                    
        
        for j in range(len(list2)):
            if list2[j] in map1:
                if map1[list2[j]] + j < leastIndexSum:
                    leastIndexSum = map1[list2[j]] +j
                    res = [list2[j]]                
                elif map1[list2[j]] + j == leastIndexSum:
                    res.append(list2[j])                

        return res
    
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
        
sol = Solution()
print(sol.findRestaurant(list1,list2))
