def CountDigit(number, digit):
    numlist = list(str(number))
    dig = str(digit)
    count = numlist.count(dig)
    return count
