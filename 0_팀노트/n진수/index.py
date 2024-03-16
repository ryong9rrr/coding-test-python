# number를 k진법으로
def convert(number, k):
    FIX_TABLE = ["0", "1", "2", "3", "4", "5", "6",
                 "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    result = ""
    while number >= k:
        result += FIX_TABLE[(number % k)]
        number = number // k
    result += FIX_TABLE[number]
    return "".join(list(result)[::-1])
