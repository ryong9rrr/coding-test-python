from collections import defaultdict
import copy
def is_diff_one(a, b):
    flag = False
    for i in range(len(a)):
        if a[i] != b[i]:
            if flag:
                return False
            flag = True
    return True

def solution(begin, target, words):
    if target not in words:
        return 0
    INF = float('inf')
    result = INF
    
    def dfs(cur, visited, count):
        nonlocal result
        if cur == target:
            result = min(result, count)
            return
        
        for word in words:
            if not visited[word] and is_diff_one(cur, word):
                visited[word] = True
                dfs(word, copy.deepcopy(visited), count + 1)
    
    visited = defaultdict(bool)
    visited[begin] = True
    
    dfs(begin, visited, 0)
    
    if result == INF:
        return 0
    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.5MB)
테스트 2 〉	통과 (0.10ms, 10.2MB)
테스트 3 〉	통과 (0.34ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
"""