def divide(n, i, j, arr):
    if n <= 1:
        return str(arr[i][j])
    mid = n // 2
    a = divide(mid, i, j, arr)
    b = divide(mid, i, j + mid, arr)
    c = divide(mid, i + mid, j, arr)
    d = divide(mid, i + mid, j + mid, arr)

    if len(a) == 1 and a == b == c == d:
        return a
    return f"({a + b + c + d})"

def solution(arr):
    result = divide(len(arr), 0, 0, arr)

    count_zero = count_one = 0

    for x in result:
        if x == "0":
            count_zero += 1
        elif x == "1":
            count_one += 1

    return [count_zero, count_one]
"""
정확성  테스트
테스트 1 〉	통과 (0.43ms, 10.2MB)
테스트 2 〉	통과 (0.41ms, 10.2MB)
테스트 3 〉	통과 (0.39ms, 10.3MB)
테스트 4 〉	통과 (0.16ms, 10.3MB)
테스트 5 〉	통과 (138.52ms, 13.4MB)
테스트 6 〉	통과 (97.00ms, 12.3MB)
테스트 7 〉	통과 (122.93ms, 12.1MB)
테스트 8 〉	통과 (92.01ms, 12.1MB)
테스트 9 〉	통과 (113.21ms, 12.2MB)
테스트 10 〉	통과 (373.38ms, 19.1MB)
테스트 11 〉	통과 (0.17ms, 10.3MB)
테스트 12 〉	통과 (0.15ms, 10.2MB)
테스트 13 〉	통과 (90.14ms, 12.3MB)
테스트 14 〉	통과 (383.50ms, 19.2MB)
테스트 15 〉	통과 (325.28ms, 19.1MB)
테스트 16 〉	통과 (86.28ms, 12.3MB)
"""