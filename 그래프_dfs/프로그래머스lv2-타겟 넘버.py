# dfs로 풀기
def solution(numbers, target):
    count = 0
    
    def dfs(index, total):
        nonlocal count
        if index == len(numbers):
            if total == target:
                count += 1
            return
        dfs(index + 1, total + numbers[index])
        dfs(index + 1, total - numbers[index])
    
    dfs(0, 0)
    return count
"""
정확성  테스트
테스트 1 〉	통과 (361.14ms, 10.1MB)
테스트 2 〉	통과 (354.83ms, 10.1MB)
테스트 3 〉	통과 (0.35ms, 10.1MB)
테스트 4 〉	통과 (2.27ms, 10.1MB)
테스트 5 〉	통과 (11.15ms, 10.1MB)
테스트 6 〉	통과 (0.76ms, 10.2MB)
테스트 7 〉	통과 (0.36ms, 10MB)
테스트 8 〉	통과 (3.54ms, 10.2MB)
"""

# itertools.product 순열 구해서 풀기
from itertools import product
def solution(numbers, target):
    nums = [(x, -x) for x in numbers]
    p = list(product(*nums))
    return [sum(arr) for arr in p].count(target)

"""
정확성  테스트
테스트 1 〉	통과 (607.69ms, 258MB)
테스트 2 〉	통과 (619.32ms, 258MB)
테스트 3 〉	통과 (0.45ms, 10.3MB)
테스트 4 〉	통과 (2.39ms, 10.8MB)
테스트 5 〉	통과 (14.93ms, 16.4MB)
테스트 6 〉	통과 (0.78ms, 10.3MB)
테스트 7 〉	통과 (0.37ms, 10.3MB)
테스트 8 〉	통과 (3.58ms, 11.5MB)
"""