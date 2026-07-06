def rob (arr, i=0,lookup = None):
    
    lookup ={} if lookup is None else lookup
    
    if i in lookup:
        return lookup[i]
    
    if i >= len(arr):
        return 0
    
    lookup[i] = max(arr[i]+rob(arr,i+2,lookup),rob(arr,i+1,lookup))
    return lookup[i]


print(rob([2,10,3,6,8,1,7]))