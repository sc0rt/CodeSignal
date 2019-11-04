def areSimilar(a, b):
    swap = list()
    if a == b:
        return True
    if sorted(a) == sorted(b):
        for i in range(len(a)):
            if a[i] != b[i]:
                swap.append(a[i])
        if len(swap) == 2:
            return True
        else: 
            return False
    else:
        return False
