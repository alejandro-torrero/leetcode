""" mineArr = [
   [3, 2, 12, 15, 10],
   [6, 19, 7, 11, 17],
   [8, 5, 12, 32, 21],
   [3, 20, 2, 9, 7]
] """

mineArr=[[0], [24], [22], [20], [22], [44]]

def getGold(mine,i,j,lookup=None):
    lookup ={} if lookup is None else lookup
    n = len(mine)
    m = len(mine[0])
    
    if (i,j) in lookup:
        return lookup[(i,j)]
    
    if i >= n:
        # There are no more rows to go downward
        return 0
    
    if j < 0 or j>=m:
        # j is out of bounds, theres nothing to consider
        return 0
    
    lookup[(i,j)] = mine[i][j] + max(getGold(mine,i+1,j-1,lookup),getGold(mine,i+1,j,lookup),getGold(mine,i+1,j+1,lookup))       
    return lookup[(i,j)]

def gold(mine):
    lookup = {}
    return max(getGold(mine,0, j,lookup) for j in range(len(mine[0])))
    

print(gold(mineArr))