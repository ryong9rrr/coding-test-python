def solution(absolutes, signs):
    SIZE = len(absolutes)
    result = 0
    
    for i in range(SIZE):
        if signs[i]:
            result += absolutes[i]
        else:
            result -= absolutes[i]
    
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.15ms, 9.96MB)
테스트 2 〉	통과 (0.08ms, 10.4MB)
테스트 3 〉	통과 (0.08ms, 10.1MB)
테스트 4 〉	통과 (0.08ms, 10.3MB)
테스트 5 〉	통과 (0.08ms, 10.1MB)
테스트 6 〉	통과 (0.07ms, 10.3MB)
테스트 7 〉	통과 (0.07ms, 10.2MB)
테스트 8 〉	통과 (0.08ms, 10.2MB)
테스트 9 〉	통과 (0.09ms, 10.3MB)
"""

def solution(absolutes, signs):
    result = 0
    
    for absolute, sign in zip(absolutes, signs):
        if sign:
            result += absolute
        else:
            result -= absolute
    
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.2MB)
테스트 2 〉	통과 (0.05ms, 10.3MB)
테스트 3 〉	통과 (0.06ms, 10.3MB)
테스트 4 〉	통과 (0.05ms, 10.2MB)
테스트 5 〉	통과 (0.05ms, 10.1MB)
테스트 6 〉	통과 (0.10ms, 10.2MB)
테스트 7 〉	통과 (0.05ms, 10.2MB)
테스트 8 〉	통과 (0.06ms, 10.3MB)
테스트 9 〉	통과 (0.05ms, 10.2MB)
"""

"""
js // reduce를 이용한 풀이

function solution(absolutes, signs) {
    return absolutes.reduce((acc, cur, i) => signs[i] ? acc + cur : acc - cur, 0)
}

정확성  테스트
테스트 1 〉	통과 (0.09ms, 29.8MB)
테스트 2 〉	통과 (0.09ms, 29.9MB)
테스트 3 〉	통과 (0.10ms, 30.1MB)
테스트 4 〉	통과 (0.11ms, 30.1MB)
테스트 5 〉	통과 (0.09ms, 30.2MB)
테스트 6 〉	통과 (0.09ms, 30MB)
테스트 7 〉	통과 (0.09ms, 30.1MB)
테스트 8 〉	통과 (0.10ms, 30MB)
테스트 9 〉	통과 (0.17ms, 30.1MB)
"""