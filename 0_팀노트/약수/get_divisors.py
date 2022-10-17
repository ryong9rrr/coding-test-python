import math
def get_divisor(number):
    if number <= 0:
        raise Exception("자연수가 아니에요.")
    limit = math.floor(math.sqrt(number))
    divisors = []
    for left in range(1, limit + 1):
        if number % left == 0:
            right = number // left
            divisors.append(left)
            if left != right:
                divisors.append(right)
    return divisors