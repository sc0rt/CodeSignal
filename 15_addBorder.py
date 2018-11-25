def addBorder(picture):
    framed = list()
    framed.append('*'*(len(picture[0]) + 2))
    for element in picture:
        bordered = '*' + element + '*'
        framed.append(bordered)
    framed.append('*'*(len(picture[0]) + 2))
    return framed
