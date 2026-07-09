
def waysFn(n, jumps,lookup = None):
    lookup = {} if lookup is None else lookup
    
    if n in lookup:
        return lookup[n]
     
    if n == 0:
        return 1    
    
    numWays = 0
    
    for jump in jumps:
        if n-jump >= 0:
            # Avoid calling recursive functions that wont work
            numWays += ways(n-jump,jumps)
    lookup[n] = numWays
    return numWays    


def ways(n, jumps):
    return waysFn(n,jumps)

print(ways(10,[2,4,5,8]))