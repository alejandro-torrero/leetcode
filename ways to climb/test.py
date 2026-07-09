def test():
    res = 0
    for jump in [2,4,5,8]:
        if(7-jump >= 0):
           res += 7-jump
    return res


print(test())