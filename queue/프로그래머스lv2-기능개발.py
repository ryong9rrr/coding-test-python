from collections import deque
import math
def solution(progresses, speeds):
    n = len(progresses)
    # 완료가 되기까지 걸릴 시간
    q = deque()
    for i in range(n):
        x = math.ceil((100 - progresses[i]) / speeds[i])
        q.append(x)
    
    _max = q.popleft()
    result = [1]
    while q:
        x = q.popleft()    
        if _max >= x:
            result[-1] += 1
        else:
            _max = x
            result.append(1)
            
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.4MB)
테스트 7 〉	통과 (0.05ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
"""