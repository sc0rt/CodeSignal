def allLongestStrings(inputArray):
    longest = 0
    lst = []
    for element in inputArray:
        if len(element) > longest:
            longest = len(element)
    for element in inputArray:
        if len(element) == longest:
            lst.append(element)
    return lst
