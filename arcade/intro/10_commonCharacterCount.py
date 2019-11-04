def commonCharacterCount(s1, s2):
    dic1 = {}
    dic2 = {}
    sums = 0
    for letter in s1:
        dic1[letter] = dic1.get(letter,0) + 1
    for letter in s2:
        dic2[letter] = dic2.get(letter,0) + 1
    for letter in dic1:
        if letter in dic2:
            sums = sums + min(dic1[letter],dic2[letter])
    return sums
