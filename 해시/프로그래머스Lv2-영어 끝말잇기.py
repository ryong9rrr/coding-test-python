def solution(n, words):
    dic = {}
    result = [0, 0]
    
    for i in range(len(words)):
        if (i > 0 and words[i][0] != words[i - 1][-1]) or words[i] in dic:
            return [i % n + 1, i // n + 1]
        dic[words[i]] = True
        
    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (0.00ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.03ms, 9.98MB)
테스트 6 〉	통과 (0.01ms, 10MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 9.98MB)
테스트 11 〉	통과 (0.02ms, 10MB)
테스트 12 〉	통과 (0.01ms, 10.1MB)
테스트 13 〉	통과 (0.01ms, 9.96MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
테스트 15 〉	통과 (0.01ms, 10MB)
테스트 16 〉	통과 (0.01ms, 10.1MB)
테스트 17 〉	통과 (0.01ms, 9.98MB)
테스트 18 〉	통과 (0.01ms, 10.1MB)
테스트 19 〉	통과 (0.01ms, 10.1MB)
테스트 20 〉	통과 (0.03ms, 10.2MB)
"""