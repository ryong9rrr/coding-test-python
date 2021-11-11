# functools.cmp_to_key
import functools
def solution(numbers):
    def compare(a, b):
        if int(a + b) < int(b + a):
            return -1
        else:
            return 1
    
    s = sorted([str(x) for x in numbers], key= functools.cmp_to_key(compare), reverse=True)
    
    return str(int("".join(s)))

"""
정확성  테스트
테스트 1 〉	통과 (1190.50ms, 21.7MB)
테스트 2 〉	통과 (441.93ms, 16.6MB)
테스트 3 〉	통과 (1757.51ms, 25.2MB)
테스트 4 〉	통과 (8.95ms, 10.5MB)
테스트 5 〉	통과 (948.41ms, 20.4MB)
테스트 6 〉	통과 (802.85ms, 19.2MB)
테스트 7 〉	통과 (0.07ms, 10.4MB)
테스트 8 〉	통과 (0.04ms, 10.4MB)
테스트 9 〉	통과 (0.04ms, 10.4MB)
테스트 10 〉	통과 (0.06ms, 10.4MB)
테스트 11 〉	통과 (0.05ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.4MB)
테스트 13 〉	통과 (0.02ms, 10.4MB)
테스트 14 〉	통과 (0.03ms, 10.3MB)
테스트 15 〉	통과 (0.02ms, 10.4MB)
"""

# 기막힌 아이디어
def solution(numbers):
    s = sorted([str(x) for x in numbers], key= lambda x : x * 3, reverse=True)
    
    return str(int("".join(s)))

"""
정확성  테스트
테스트 1 〉	통과 (760.46ms, 23.9MB)
테스트 2 〉	통과 (265.23ms, 17.5MB)
테스트 3 〉	통과 (1281.54ms, 28.2MB)
테스트 4 〉	통과 (1.87ms, 10.5MB)
테스트 5 〉	통과 (632.93ms, 22.4MB)
테스트 6 〉	통과 (458.37ms, 20.7MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.4MB)
테스트 9 〉	통과 (0.04ms, 10.4MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
테스트 11 〉	통과 (0.05ms, 10.4MB)
테스트 12 〉	통과 (0.02ms, 10.3MB)
테스트 13 〉	통과 (0.02ms, 10.3MB)
테스트 14 〉	통과 (0.02ms, 10.4MB)
테스트 15 〉	통과 (0.02ms, 10.4MB)
"""