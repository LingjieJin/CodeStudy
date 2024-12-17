def prime(p):
    if p <= 1:
        return False
    for i in range(2, int(p**0.5) + 1):
        if p % i == 0:
            return False
    return True

def PrimeSum(m, n):
       prime_sum = 0
       for num in range(m, n + 1):
           if prime(num):
               prime_sum += num
       return prime_sum