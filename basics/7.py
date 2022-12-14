def myFunc(n):
    return lambda a: a*n
mydoubler = myFunc(2)
print(mydoubler(11))
