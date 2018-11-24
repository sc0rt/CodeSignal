def centuryFromYear(year):
    mod = year % 100
    if mod > 0:
        return int(year/100) + 1
    else:
        return int(year/100)
