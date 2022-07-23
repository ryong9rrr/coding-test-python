def pushed_string(string, standard, n):
    return chr((ord(string) - ord(standard) + n) % 26 + ord(standard))

def push_string(string, n):
    if not string.isalpha():
        return string
    if string.isupper():
        return pushed_string(string, "A", n)
    return pushed_string(string, "a", n)

def solution(s, n):
    return "".join([ push_string(string, n) for string in list(s) ])
"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.03ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (2.13ms, 10.4MB)
"""