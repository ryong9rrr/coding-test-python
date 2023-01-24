def solution(elements):
    numbers = elements * 2
    
    result = set()
    
    for size in range(1, len(elements) + 1):
        for i in range(len(elements)):
            result.add(sum(numbers[i:i + size]))
            
    return len(result)
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (46.44ms, 13.1MB)
테스트 3 〉	통과 (136.19ms, 14.2MB)
테스트 4 〉	통과 (301.04ms, 18.3MB)
테스트 5 〉	통과 (532.12ms, 26.9MB)
테스트 6 〉	통과 (1013.81ms, 27MB)
테스트 7 〉	통과 (1434.92ms, 26.9MB)
테스트 8 〉	통과 (2060.03ms, 27.8MB)
테스트 9 〉	통과 (2898.86ms, 43.7MB)
테스트 10 〉	통과 (3736.48ms, 43.6MB)
테스트 11 〉	통과 (692.66ms, 27MB)
테스트 12 〉	통과 (829.26ms, 26.9MB)
테스트 13 〉	통과 (1312.15ms, 26.9MB)
테스트 14 〉	통과 (1271.97ms, 27MB)
테스트 15 〉	통과 (1536.19ms, 26.9MB)
테스트 16 〉	통과 (1847.47ms, 43.8MB)
테스트 17 〉	통과 (2153.33ms, 43.8MB)
테스트 18 〉	통과 (2535.09ms, 43.8MB)
테스트 19 〉	통과 (3081.87ms, 43.6MB)
테스트 20 〉	통과 (3599.99ms, 43.7MB)
"""