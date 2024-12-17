import math


def funcos(eps, x):
    i = 0
    s = 0
    flag = 1
    while True:
        item = x ** (2 * i + 1) / math.factorial(2 * i + 1)
        if abs(item) < eps:
            break
        s = s + flag * item
        flag = -flag
        i = i + 2
    return s

