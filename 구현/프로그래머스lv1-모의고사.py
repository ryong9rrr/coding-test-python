def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    a_i = 0
    b_i = 0
    c_i = 0
    for i, answer in enumerate(answers):
        if answer == a[a_i]:
            score[0] += 1
        if answer == b[b_i]:
            score[1] += 1
        if answer == c[c_i]:
            score[2] += 1
        
        a_i += 1
        b_i += 1
        c_i += 1
            
        if a_i == 5:
            a_i = 0
        if b_i == 8:
            b_i = 0
        if c_i == 10:
            c_i = 0
        
    _max = max(score)
    result = []
    for i in range(3):
        if score[i] == _max:
            result.append(i + 1)
    
    return result

"""
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.4MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.4MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (1.61ms, 10.3MB)
테스트 8 〉	통과 (0.45ms, 10.2MB)
테스트 9 〉	통과 (2.32ms, 10.3MB)
테스트 10 〉	통과 (1.10ms, 10.3MB)
테스트 11 〉	통과 (2.45ms, 10.4MB)
테스트 12 〉	통과 (2.55ms, 10.3MB)
테스트 13 〉	통과 (0.14ms, 10.3MB)
테스트 14 〉	통과 (2.49ms, 10.3MB)
"""

# 조금 더 smart한 방법
def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    for i, answer in enumerate(answers):
        if answer == a[i % 5]:
            score[0] += 1
        if answer == b[i % 8]:
            score[1] += 1
        if answer == c[i % 10]:
            score[2] += 1
        
    _max = max(score)
    result = []
    for i in range(3):
        if score[i] == _max:
            result.append(i + 1)
    
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (1.09ms, 10.4MB)
테스트 8 〉	통과 (0.35ms, 10.2MB)
테스트 9 〉	통과 (2.00ms, 10.3MB)
테스트 10 〉	통과 (0.90ms, 10.3MB)
테스트 11 〉	통과 (2.17ms, 10.3MB)
테스트 12 〉	통과 (1.77ms, 10.3MB)
테스트 13 〉	통과 (0.12ms, 10.3MB)
테스트 14 〉	통과 (2.38ms, 10.3MB)
"""