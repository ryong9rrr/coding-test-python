def solution(N, stages):
    k = len(stages)
    table = [0] * (N + 2)
    for stage in stages:
        table[stage] += 1
        
    failures = []
    for stage in range(1, N + 1):
        failure = table[stage] / k if table[stage] > 0 else 0
        failures.append((failure, stage))
        k -= table[stage]
    
    failures.sort(key=lambda x:x[0], reverse=True)
    return [x[1] for x in failures]
"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.1MB)
테스트 2 〉	통과 (0.07ms, 10.3MB)
테스트 3 〉	통과 (1.04ms, 10.5MB)
테스트 4 〉	통과 (6.36ms, 10.8MB)
테스트 5 〉	통과 (17.02ms, 14.9MB)
테스트 6 〉	통과 (0.11ms, 10.4MB)
테스트 7 〉	통과 (1.05ms, 10.4MB)
테스트 8 〉	통과 (7.08ms, 10.8MB)
테스트 9 〉	통과 (30.84ms, 15MB)
테스트 10 〉	통과 (9.08ms, 10.8MB)
테스트 11 〉	통과 (7.50ms, 10.7MB)
테스트 12 〉	통과 (10.42ms, 11.4MB)
테스트 13 〉	통과 (14.77ms, 11.4MB)
테스트 14 〉	통과 (0.04ms, 10.2MB)
테스트 15 〉	통과 (6.16ms, 10.5MB)
테스트 16 〉	통과 (4.26ms, 10.3MB)
테스트 17 〉	통과 (7.70ms, 10.7MB)
테스트 18 〉	통과 (2.25ms, 10.4MB)
테스트 19 〉	통과 (0.82ms, 10.2MB)
테스트 20 〉	통과 (3.03ms, 10.3MB)
테스트 21 〉	통과 (6.91ms, 10.8MB)
테스트 22 〉	통과 (23.75ms, 18.3MB)
테스트 23 〉	통과 (14.11ms, 11.6MB)
테스트 24 〉	통과 (13.03ms, 11.7MB)
테스트 25 〉	통과 (0.01ms, 10.4MB)
테스트 26 〉	통과 (0.01ms, 10.3MB)
테스트 27 〉	통과 (0.01ms, 10.1MB)
"""