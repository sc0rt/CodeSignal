def alternatingSums(a):
    sumodd = 0
    sumeven = 0
    for i in range(len(a)):
        if i%2 != 0:
            sumodd = sumodd + a[i]
        else:
            sumeven = sumeven + a[i]
    return [sumeven,sumodd]
