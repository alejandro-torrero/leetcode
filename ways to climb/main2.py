def waysFn(n,jumps):
    # Array of zeros
    dp= [0]*(n+1)
    
    dp[0] = 1
    
    for i in range (1,n+1):
        for jump in jumps:
            if (i-jump)>=0:
                dp[i] += dp[i-jump]
    
    return dp[n]

def ways(n, jumps):
    return waysFn(n,jumps)

print(ways(10,[2,4,5,8]))