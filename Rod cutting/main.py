# Parameters:
#  prices: List[int]
#  n: int

# Return type: int


def rod(prices, n, lookup=None):
    lookup = {} if lookup is None else lookup

    if n in lookup:
        return lookup[n]

    maxPrice = 0
    for i in range(1, n + 1):        
            maxPrice = max(maxPrice, prices[i] + rod(prices, n - i, lookup))
            
    lookup[n] = maxPrice
    return maxPrice
 

print(rod([0, 1, 3, 5, 6, 7, 9, 10, 11], 8))
