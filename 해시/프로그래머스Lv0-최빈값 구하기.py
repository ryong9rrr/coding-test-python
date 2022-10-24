"""
[1, 1, 1, 1...] 이런 케이스가 있을 수도 있으므로
처음부터 얼리리턴을 하지 말고 일단 counter 한 뒤 리턴
"""
from collections import Counter
def solution(array):
    counter = Counter(array).most_common(2)
    
    if len(counter) == 1:
        return counter[0][0]
    
    a, b = counter
    
    if a[1] == b[1]:
        return -1
    return a[0]
"""
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.08ms, 10.2MB)
테스트 3 〉	통과 (0.06ms, 10MB)
테스트 4 〉	통과 (0.04ms, 10.2MB)
테스트 5 〉	통과 (0.05ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.1MB)
테스트 7 〉	통과 (0.04ms, 10.4MB)
테스트 8 〉	통과 (0.05ms, 10.3MB)
테스트 9 〉	통과 (0.03ms, 10.3MB)
테스트 10 〉	통과 (0.05ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.3MB)
테스트 12 〉	통과 (0.06ms, 10.1MB)
테스트 13 〉	통과 (0.05ms, 10.3MB)
테스트 14 〉	통과 (0.06ms, 10.1MB)
테스트 15 〉	통과 (0.07ms, 10.4MB)
테스트 16 〉	통과 (0.03ms, 10.1MB)
"""