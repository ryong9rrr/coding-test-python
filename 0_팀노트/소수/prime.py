def is_prime(n):
    if n <= 1:
      return False
    i = 2
    while i * i <= n:
        if n % i == 0: 
          return False
        i += 1
    return True

# n은 범위
def make_primes(n:int)->list:
    primes = [True] * (n + 1)
    primes[0:2] = [False, False]
    for num in range(2, int(n * 0.5) + 1):
        if primes[num]:
            for i in range(num ** 2, n + 1, num):
                primes[i] = False
    return primes