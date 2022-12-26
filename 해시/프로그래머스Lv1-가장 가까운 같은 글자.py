def solution(s):
    table = {}
    
    result = []
    
    for index in range(len(s)):
        char = s[index]
        if not char in table:
            table[char] = index
            result.append(-1)
            continue
        interval = index - table[char]
        table[char] = index
        result.append(interval)
        
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (0.28ms, 10.3MB)
테스트 5 〉	통과 (1.39ms, 11.1MB)
테스트 6 〉	통과 (0.58ms, 10.4MB)
테스트 7 〉	통과 (2.67ms, 11MB)
테스트 8 〉	통과 (0.45ms, 10.4MB)
테스트 9 〉	통과 (2.51ms, 10.8MB)
테스트 10 〉	통과 (0.57ms, 10.3MB)
테스트 11 〉	통과 (1.26ms, 10.8MB)
테스트 12 〉	통과 (0.00ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (0.07ms, 10.4MB)
테스트 15 〉	통과 (0.01ms, 10.1MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (0.02ms, 10.3MB)
테스트 18 〉	통과 (0.52ms, 10.3MB)
테스트 19 〉	통과 (0.30ms, 10.5MB)
테스트 20 〉	통과 (0.11ms, 10.2MB)
테스트 21 〉	통과 (0.02ms, 10.2MB)
테스트 22 〉	통과 (0.85ms, 10.3MB)
테스트 23 〉	통과 (0.14ms, 10.3MB)
테스트 24 〉	통과 (0.08ms, 10.3MB)
테스트 25 〉	통과 (0.22ms, 10.3MB)
테스트 26 〉	통과 (0.03ms, 10.3MB)
테스트 27 〉	통과 (0.11ms, 10.2MB)
테스트 28 〉	통과 (0.19ms, 10.2MB)
테스트 29 〉	통과 (0.00ms, 10.1MB)
테스트 30 〉	통과 (2.55ms, 11.1MB)
"""