def arrayChange(a):
    counter = 0
    for i in range(len(a)-1):
        if a[i] >= a[i+1]:
            diff = a[i] - a[i+1]
            a[i+1] = a[i+1] + diff + 1
            counter = counter + diff + 1
    return counter
