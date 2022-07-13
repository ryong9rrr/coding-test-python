# n은 범위
def make_prime_numbers(n:int)->list:
    prime_numbers = [True] * (n + 1)
    prime_numbers[0:2] = [False, False]
    for num in range(2, int(n * 0.5) + 1):
        if prime_numbers[num]:
            for i in range(num ** 2, n + 1, num):
                prime_numbers[i] = False
    return prime_numbers