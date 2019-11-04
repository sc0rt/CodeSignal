def adjacentElementsProduct(inputArray):
    lst = list()
    for i in range(0,(len(inputArray) - 1),1):
        prod = inputArray[i] * inputArray[i+1]
        lst.append(prod)
    return max(lst)
