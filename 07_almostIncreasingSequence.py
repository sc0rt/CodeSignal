def almostIncreasingSequence(sequence):
    def increasing(test):
            for i in range(0, len(test) - 1):
                if test[i] >= test[i+1]:
                    return False
            return True
    for i in range(0, len(sequence) - 1):
        if sequence[i] >= sequence[i+1]:
            test1 = sequence[:i] + sequence[i+1:]
            test2 = sequence[:i+1] + sequence[i+2:]
            if increasing(test1) == True:
                return True
            elif increasing(test2) == True:
                return True
            else:
                return False
