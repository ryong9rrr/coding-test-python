# 보면 알겠지만 k는 16이하여야 함.
def convert_number(number, k):
    MODS = "0123456789ABCDEF"
    result = ""
    while number > 0:
        result += MODS[number % k]
        number = number // k
    return result[::-1]