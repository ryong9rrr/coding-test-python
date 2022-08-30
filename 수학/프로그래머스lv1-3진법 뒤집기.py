def solution(n):
    rev_three = ""
    while n > 2:
        a, b = divmod(n, 3)
        rev_three += str(b)
        n = a
    rev_three += str(n)

    result = 0
    for i, v in enumerate(str(int(rev_three[::-1]))):
        result += 3 ** i * int(v)
    
    return result
"""
정확성 테스트
테스트 1 〉 통과 (0.02ms, 10.5MB)
테스트 2 〉 통과 (0.05ms, 10.3MB)
테스트 3 〉 통과 (0.03ms, 10.3MB)
테스트 4 〉 통과 (0.03ms, 10.4MB)
테스트 5 〉 통과 (0.02ms, 10.3MB)
테스트 6 〉 통과 (0.03ms, 10.3MB)
테스트 7 〉 통과 (0.02ms, 10.4MB)
테스트 8 〉 통과 (0.03ms, 10.4MB)
테스트 9 〉 통과 (0.03ms, 10.5MB)
테스트 10 〉 통과 (0.03ms, 10.3MB)
"""

# int는 이렇게 사용할 수도 있다.
def solution(n):
    rev_three = ""
    while n > 2:
        a, b = divmod(n, 3)
        rev_three += str(b)
        n = a
    rev_three += str(n)

    return int(rev_three, 3)
"""
정확성 테스트
테스트 1 〉 통과 (0.02ms, 10.2MB)
테스트 2 〉 통과 (0.02ms, 10.4MB)
테스트 3 〉 통과 (0.02ms, 10.2MB)
테스트 4 〉 통과 (0.02ms, 10.3MB)
테스트 5 〉 통과 (0.02ms, 10.2MB)
테스트 6 〉 통과 (0.02ms, 10.2MB)
테스트 7 〉 통과 (0.02ms, 10.2MB)
테스트 8 〉 통과 (0.02ms, 10.4MB)
테스트 9 〉 통과 (0.02ms, 10.2MB)
테스트 10 〉 통과 (0.03ms, 10.3MB)

"""