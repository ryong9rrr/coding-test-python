def solution(lines):
    table = [set([]) for _ in range(200)]
    for index, line in enumerate(lines):
        a, b = line
        for i in range(a, b):
            table[i + 100].add(index)
    
    count = 0
    for line in table:
        if len(line) > 1:
            count += 1
    
    return count
"""
정확성  테스트
테스트 1 〉	통과 (0.08ms, 10.3MB)
테스트 2 〉	통과 (0.08ms, 10.2MB)
테스트 3 〉	통과 (0.06ms, 10.2MB)
테스트 4 〉	통과 (0.15ms, 10.2MB)
테스트 5 〉	통과 (0.06ms, 10.3MB)
테스트 6 〉	통과 (0.07ms, 10.2MB)
테스트 7 〉	통과 (0.09ms, 10.3MB)
테스트 8 〉	통과 (0.09ms, 10.3MB)
테스트 9 〉	통과 (0.06ms, 10.4MB)
테스트 10 〉	통과 (0.06ms, 10.2MB)
"""