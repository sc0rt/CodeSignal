def checkPalindrome(inputString):
    lst = list()
    for letter in inputString :
        lst.append(letter)
    rev = lst[::-1]

    if str(lst) == str(rev) :
        return True
    else :
        return False
