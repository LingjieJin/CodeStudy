def fn(a, n):
    result = 0
    current_term = 0
    for i in range(1, n + 1):
        current_term = current_term * 10 + a
        result += current_term
    return result