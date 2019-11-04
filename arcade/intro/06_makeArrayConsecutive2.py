def makeArrayConsecutive2(statues):
    lst = list()
    for i in range(min(statues),max(statues)):
        if i not in statues:
            lst.append(i)
    return len(lst)
