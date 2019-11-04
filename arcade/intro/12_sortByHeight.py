def sortByHeight(a):
    heights = []
    for element in a:
        if element != -1:
            heights.append(element)
    j = 0
    for i in range(0,len(a)):
        if a[i] != -1:
            a[i] = sorted(heights)[j]
            j = j + 1 
    return a
