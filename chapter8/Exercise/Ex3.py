def sumOfnatural(n):
    if(n == 0):
        return 0
    
    return n + sumOfnatural(n-1)

g = sumOfnatural(5)
print(g)