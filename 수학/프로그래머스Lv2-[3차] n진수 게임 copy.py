def convert_number(number, k):
    MODS = "0123456789ABCDEF"
    result = ""
    while number > 0:
        result += MODS[number % k]
        number = number // k
    return result[::-1]
    

def solution(n, t, m, p):
    numbers = "0"
    for number in range(1, t * m + m):
        numbers += convert_number(number, n)
    
    result = ""
    index = p - 1
    while len(result) < t:
        result += numbers[index]
        index += m
    
    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.46ms, 10.2MB)
테스트 6 〉	통과 (0.47ms, 10.2MB)
테스트 7 〉	통과 (0.45ms, 10.3MB)
테스트 8 〉	통과 (0.36ms, 10.1MB)
테스트 9 〉	통과 (0.21ms, 10.2MB)
테스트 10 〉	통과 (0.24ms, 10.3MB)
테스트 11 〉	통과 (0.20ms, 10.1MB)
테스트 12 〉	통과 (0.19ms, 10.2MB)
테스트 13 〉	통과 (0.36ms, 10.3MB)
테스트 14 〉	통과 (70.31ms, 10.4MB)
테스트 15 〉	통과 (65.63ms, 10.3MB)
테스트 16 〉	통과 (94.80ms, 10.3MB)
테스트 17 〉	통과 (3.78ms, 10.2MB)
테스트 18 〉	통과 (4.82ms, 10.2MB)
테스트 19 〉	통과 (0.73ms, 10.2MB)
테스트 20 〉	통과 (2.06ms, 10.1MB)
테스트 21 〉	통과 (14.46ms, 10.2MB)
테스트 22 〉	통과 (8.67ms, 10.2MB)
테스트 23 〉	통과 (20.59ms, 10.4MB)
테스트 24 〉	통과 (68.38ms, 10.4MB)
테스트 25 〉	통과 (103.69ms, 10.6MB)
테스트 26 〉	통과 (14.31ms, 10.2MB)
"""