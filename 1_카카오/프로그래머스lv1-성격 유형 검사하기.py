def solution(survey, choices):
    N = len(survey)
    match_kind = {
        "R": "T",
        "C": "F",
        "J": "M",
        "A": "N"
    }
    
    score = {
        "R": 0,
        "T": 0,
        "C": 0,
        "F": 0,
        "J": 0,
        "M": 0,
        "A": 0,
        "N": 0,
    }
    
    for i in range(N):
        x, y = list(survey[i])
        choice = choices[i]
        if 1 <= choice <= 3:
            score[x] += (4 - choice)
        elif 4 <= choice <= 7:
            score[y] += (choice - 4)
    
    result = ""
    
    for kind in ["R", "C", "J", "A"]:
        a = kind
        b = match_kind[kind]
        if score[a] > score[b]:
            result += a
        elif score[a] < score[b]:
            result += b
        else:
            result += min(a, b)
    
    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.4MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.03ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.2MB)
테스트 11 〉	통과 (0.03ms, 10.3MB)
테스트 12 〉	통과 (0.07ms, 10.3MB)
테스트 13 〉	통과 (0.12ms, 10.2MB)
테스트 14 〉	통과 (0.19ms, 10.2MB)
테스트 15 〉	통과 (0.22ms, 10.2MB)
테스트 16 〉	통과 (0.24ms, 10.3MB)
테스트 17 〉	통과 (0.24ms, 10.4MB)
테스트 18 〉	통과 (0.24ms, 10.3MB)
테스트 19 〉	통과 (0.24ms, 10.4MB)
테스트 20 〉	통과 (0.24ms, 10.3MB)
"""