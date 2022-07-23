import math
def get_divisor(number):
    if number < 0:
        raise Exception("숫자는 0 이상의 정수여아합니다.")
    if number == 0:
        return [0]
    divisors = []
    limit = math.floor(math.sqrt(number))
    for left in range(1, limit + 1):
        if number % left == 0:
            right = number // left
            if left == right:
                divisors.append(left)
            else:
                divisors.append(left)
                divisors.append(right)
    return divisors