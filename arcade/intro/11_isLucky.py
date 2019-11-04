def isLucky(n):
    half = len(str(n)) / 2
    first = str(n)[:int(half)]
    second = str(n)[int(half):]
    
    if sum(int(number) for number in first) == sum(int(number) for number in second):
        return True
    else:
        return False
