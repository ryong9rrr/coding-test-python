def solution(numbers):
    result = set()
    for i in range(0, len(numbers)) :
        for j in range(i+1, len(numbers)) :
            result.add(numbers[i]+numbers[j])
            
    return sorted(list(result))

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.05ms, 10.2MB)
테스트 7 〉	통과 (0.74ms, 10.1MB)
테스트 8 〉	통과 (0.80ms, 10.2MB)
테스트 9 〉	통과 (0.77ms, 10.2MB)
"""

import itertools
def solution(numbers):
    nCr = itertools.combinations(numbers, 2)
    result = set([])
    for i in nCr:
        result.add(sum(i))
        
    return sorted(result)

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.05ms, 10.2MB)
테스트 7 〉	통과 (0.78ms, 10.2MB)
테스트 8 〉	통과 (0.71ms, 10.2MB)
테스트 9 〉	통과 (0.87ms, 10.2MB)
"""