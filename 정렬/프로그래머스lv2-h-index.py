def solution(citations):
    citations.sort(reverse = True)
    N = len(citations)
    
    for h_index, v in enumerate(citations):
        if h_index >= v: 
            return h_index      
    return N
"""
정확성  테스트
테스트 1 〉	통과 (0.06ms, 10.1MB)
테스트 2 〉	통과 (0.09ms, 10.3MB)
테스트 3 〉	통과 (0.09ms, 10.3MB)
테스트 4 〉	통과 (0.07ms, 10.2MB)
테스트 5 〉	통과 (0.09ms, 10.1MB)
테스트 6 〉	통과 (0.10ms, 10.2MB)
테스트 7 〉	통과 (0.04ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.05ms, 10.2MB)
테스트 11 〉	통과 (0.11ms, 10.2MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.10ms, 10.1MB)
테스트 14 〉	통과 (0.10ms, 10.3MB)
테스트 15 〉	통과 (0.17ms, 10.2MB)
테스트 16 〉	통과 (0.00ms, 10.2MB)
"""