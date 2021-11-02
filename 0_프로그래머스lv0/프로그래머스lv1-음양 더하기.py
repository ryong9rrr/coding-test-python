def solution(absolutes, signs):
    result = 0
    idx = len(absolutes)
    for i in range(0, idx) :
        if signs[i] :
            result += absolutes[i]
        else :
            result -= absolutes[i]
            
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.13ms, 10.2MB)
테스트 2 〉	통과 (0.14ms, 10MB)
테스트 3 〉	통과 (0.12ms, 10.2MB)
테스트 4 〉	통과 (0.13ms, 10.2MB)
테스트 5 〉	통과 (0.14ms, 10.3MB)
테스트 6 〉	통과 (0.12ms, 10.2MB)
테스트 7 〉	통과 (0.13ms, 10.1MB)
테스트 8 〉	통과 (0.08ms, 10.1MB)
테스트 9 〉	통과 (0.14ms, 10.2MB)
"""

def solution(absolutes, signs):
    result = 0
    for i, sign in enumerate(signs):
        if sign:
            result += absolutes[i]
        else:
            result -= absolutes[i]
            
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.07ms, 10.3MB)
테스트 2 〉	통과 (0.07ms, 10.3MB)
테스트 3 〉	통과 (0.07ms, 10.2MB)
테스트 4 〉	통과 (0.08ms, 10.2MB)
테스트 5 〉	통과 (0.08ms, 10.4MB)
테스트 6 〉	통과 (0.07ms, 10.3MB)
테스트 7 〉	통과 (0.08ms, 10.3MB)
테스트 8 〉	통과 (0.08ms, 10.3MB)
테스트 9 〉	통과 (0.08ms, 10.3MB)
"""