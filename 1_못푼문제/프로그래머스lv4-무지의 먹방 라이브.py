import heapq
def solution(food_times, k):
    n = len(food_times)
    q = []
    for i in range(n):
        heapq.heappush(q, (food_times[i], i))
    
    total = prev = 0
    
    while q and total + ((q[0][0] - prev) * n) <= k:
        time = heapq.heappop(q)[0]
        total += (time - prev) * n
        n -= 1
        prev = time
        #print(q, total, prev, n)
    
    result = sorted(q, key = lambda x: x[1])
    if n <= 0:
        return -1
    return result[(k - total) % n][1] + 1

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.4MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.02ms, 10.2MB)
테스트 15 〉	통과 (0.02ms, 10.2MB)
테스트 16 〉	통과 (0.02ms, 10.2MB)
테스트 17 〉	통과 (0.03ms, 10.2MB)
테스트 18 〉	통과 (0.02ms, 10.4MB)
테스트 19 〉	통과 (0.02ms, 10.2MB)
테스트 20 〉	통과 (0.02ms, 10.2MB)
테스트 21 〉	통과 (0.10ms, 10.4MB)
테스트 22 〉	통과 (0.10ms, 10.2MB)
테스트 23 〉	통과 (0.09ms, 10.1MB)
테스트 24 〉	통과 (0.73ms, 10.3MB)
테스트 25 〉	통과 (0.79ms, 10.4MB)
테스트 26 〉	통과 (1.22ms, 10.5MB)
테스트 27 〉	통과 (1.06ms, 10.4MB)
테스트 28 〉	통과 (0.01ms, 10.3MB)
테스트 29 〉	통과 (0.02ms, 10.3MB)
테스트 30 〉	통과 (0.01ms, 10.3MB)
테스트 31 〉	통과 (0.01ms, 10.3MB)
테스트 32 〉	통과 (0.02ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (251.49ms, 42.6MB)
테스트 2 〉	통과 (71.55ms, 42.3MB)
테스트 3 〉	통과 (344.77ms, 39.2MB)
테스트 4 〉	통과 (370.63ms, 39.3MB)
테스트 5 〉	통과 (261.13ms, 42.6MB)
테스트 6 〉	통과 (212.97ms, 42.9MB)
테스트 7 〉	통과 (287.51ms, 42.1MB)
테스트 8 〉	통과 (187.12ms, 43.4MB)
"""

import heapq
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i, time in enumerate(food_times):
        heapq.heappush(q, (time, i + 1))
    
    total = prev = 0
    n = len(food_times)
    
    while q and total + ((q[0][0] - prev) * n) <= k:
        time, i = heapq.heappop(q)
        total += (time - prev) * n
        n -= 1
        prev = time
    
    result = sorted(q, key = lambda x: x[1])
    
    return result[(k - total) % n][1]