def solution(citations):
    citations.sort(reverse = True)

    for i in range(len(citations)):
        if i + 1 > citations[i]: return i
    return len(citations)

"""
정확성  테스트
테스트 1 〉	통과 (0.11ms, 9.97MB)
테스트 2 〉	통과 (0.11ms, 10.2MB)
테스트 3 〉	통과 (0.10ms, 10.1MB)
테스트 4 〉	통과 (0.14ms, 10.2MB)
테스트 5 〉	통과 (0.13ms, 10.3MB)
테스트 6 〉	통과 (0.20ms, 10.2MB)
테스트 7 〉	통과 (0.04ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.02ms, 10MB)
테스트 10 〉	통과 (0.05ms, 10.2MB)
테스트 11 〉	통과 (0.15ms, 10.1MB)
테스트 12 〉	통과 (0.02ms, 10.1MB)
테스트 13 〉	통과 (0.12ms, 10.2MB)
테스트 14 〉	통과 (0.12ms, 10MB)
테스트 15 〉	통과 (0.20ms, 10MB)
테스트 16 〉	통과 (0.00ms, 10.1MB)
"""


"""js
function solution(citations) {
    citations.sort((a, b) => b - a);

    for (let i = 0;  i < citations.length; i++){
        if (i + 1 > citations[i]) return i
    }
    return citations.length
}

정확성  테스트
테스트 1 〉	통과 (0.23ms, 30.2MB)
테스트 2 〉	통과 (0.34ms, 30.1MB)
테스트 3 〉	통과 (0.26ms, 30.1MB)
테스트 4 〉	통과 (0.23ms, 29.9MB)
테스트 5 〉	통과 (0.28ms, 30.2MB)
테스트 6 〉	통과 (0.32ms, 30.1MB)
테스트 7 〉	통과 (0.19ms, 30.1MB)
테스트 8 〉	통과 (0.11ms, 30.2MB)
테스트 9 〉	통과 (0.08ms, 30.1MB)
테스트 10 〉	통과 (0.18ms, 30.1MB)
테스트 11 〉	통과 (0.34ms, 30.1MB)
테스트 12 〉	통과 (0.12ms, 30.2MB)
테스트 13 〉	통과 (0.34ms, 30.1MB)
테스트 14 〉	통과 (0.30ms, 30.1MB)
테스트 15 〉	통과 (0.31ms, 30MB)
테스트 16 〉	통과 (0.09ms, 29.9MB)
"""