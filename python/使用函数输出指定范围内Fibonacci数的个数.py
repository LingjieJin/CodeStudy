def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        i = 2
        a = 1
        b = 1
        while i <= n:
            a, b = b, a + b
            i = i + 1
        return b


def PrintFN(m, n):
    fiblist = []
    a = 1
    b = 1
    while a <= n:
        if a >= m:
            fiblist.append(a)
        a, b = b, a + b
    return fiblist