def lcsFn(s1,s2,i=0,j=0,lookup=None):
    lookup = {} if lookup is None else lookup
    
    if (i,j) in lookup:
        return lookup[(i,j)]
    
    if i>= len(s1) or j>= len(s2):
        return 0
    
    if s1[i] == s2[j]:
        lookup[(i,j)] = 1 + lcsFn(s1,s2,i+1,j+1,lookup)
        return lookup[(i,j)]
    
    lookup[(i,j)] = max(lcsFn(s1,s2,i+1,j,lookup),lcsFn(s1,s2,i,j+1,lookup))
    
    return lookup[(i,j)]

def lcs(s1, s2):
    return lcsFn(s1,s2)
    


print(lcs("ylqpejqbalahwr","yrkzavgdmdgtqpg"))