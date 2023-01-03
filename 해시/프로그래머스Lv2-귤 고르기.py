from collections import Counter

def solution(k, tangerine):
    counter = sorted(Counter(tangerine).values(), reverse = True)
    
    result = 0
    for count in counter:
        if k <= 0:
            return result
        k -= count
        result += 1
    return result
"""
정확성  테스트
테스트 1 〉	통과 (8.92ms, 13.1MB)
테스트 2 〉	통과 (5.37ms, 13.1MB)
테스트 3 〉	통과 (8.75ms, 13.4MB)
테스트 4 〉	통과 (7.57ms, 13.1MB)
테스트 5 〉	통과 (8.10ms, 11.1MB)
테스트 6 〉	통과 (9.08ms, 11.2MB)
테스트 7 〉	통과 (6.00ms, 12.6MB)
테스트 8 〉	통과 (5.76ms, 11.8MB)
테스트 9 〉	통과 (9.54ms, 11.6MB)
테스트 10 〉	통과 (6.68ms, 12.9MB)
테스트 11 〉	통과 (0.04ms, 10.1MB)
테스트 12 〉	통과 (0.02ms, 10.1MB)
테스트 13 〉	통과 (0.04ms, 10.3MB)
테스트 14 〉	통과 (0.02ms, 10.1MB)
테스트 15 〉	통과 (0.02ms, 10.2MB)
테스트 16 〉	통과 (0.03ms, 10.2MB)
테스트 17 〉	통과 (0.03ms, 10.1MB)
테스트 18 〉	통과 (0.04ms, 10.2MB)
테스트 19 〉	통과 (0.03ms, 10.3MB)
테스트 20 〉	통과 (0.03ms, 10.2MB)
테스트 21 〉	통과 (0.06ms, 10MB)
테스트 22 〉	통과 (0.12ms, 10.4MB)
테스트 23 〉	통과 (0.24ms, 10.1MB)
테스트 24 〉	통과 (0.14ms, 10.3MB)
테스트 25 〉	통과 (2.35ms, 11MB)
테스트 26 〉	통과 (2.21ms, 11.7MB)
테스트 27 〉	통과 (23.52ms, 21.9MB)
테스트 28 〉	통과 (15.87ms, 16.3MB)
테스트 29 〉	통과 (31.68ms, 18.1MB)
테스트 30 〉	통과 (31.07ms, 21.8MB)
테스트 31 〉	통과 (6.48ms, 12.7MB)
테스트 32 〉	통과 (7.70ms, 13.6MB)
테스트 33 〉	통과 (27.27ms, 18MB)
테스트 34 〉	통과 (14.08ms, 18MB)
"""