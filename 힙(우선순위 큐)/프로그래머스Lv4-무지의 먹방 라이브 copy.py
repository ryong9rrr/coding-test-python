# Heap으로 풀기
import heapq
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    heap = []
    for i, time in enumerate(food_times):
        heapq.heappush(heap, [time, i + 1])
    
    prev = 0
    while heap and k >= 0:
        time = heap[0][0]
        # cycle = len(heap)
        # acc = time * cycle - prev * cycle
        acc = (time - prev) * len(heap)
        if k < acc:
            break
        heapq.heappop(heap)
        k -= acc
        prev = time
    
    result = [x[1] for x in sorted(heap, key = lambda x: x[1])]
    return result[k % len(result)]
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.1MB)
테스트 6 〉	통과 (0.02ms, 10.1MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.1MB)
테스트 10 〉	통과 (0.02ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.1MB)
테스트 12 〉	통과 (0.02ms, 10.1MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.02ms, 10.1MB)
테스트 15 〉	통과 (0.02ms, 10.2MB)
테스트 16 〉	통과 (0.00ms, 10.2MB)
테스트 17 〉	통과 (0.02ms, 10.2MB)
테스트 18 〉	통과 (0.02ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.1MB)
테스트 20 〉	통과 (0.00ms, 10.1MB)
테스트 21 〉	통과 (0.10ms, 10.2MB)
테스트 22 〉	통과 (0.11ms, 10.2MB)
테스트 23 〉	통과 (0.00ms, 10.2MB)
테스트 24 〉	통과 (1.05ms, 10.2MB)
테스트 25 〉	통과 (0.93ms, 10.3MB)
테스트 26 〉	통과 (1.46ms, 10.4MB)
테스트 27 〉	통과 (1.19ms, 10.4MB)
테스트 28 〉	통과 (0.02ms, 10.3MB)
테스트 29 〉	통과 (0.02ms, 10.2MB)
테스트 30 〉	통과 (0.01ms, 10.2MB)
테스트 31 〉	통과 (0.01ms, 10.2MB)
테스트 32 〉	통과 (0.02ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (256.41ms, 44.5MB)
테스트 2 〉	통과 (104.16ms, 44.5MB)
테스트 3 〉	통과 (419.86ms, 41.8MB)
테스트 4 〉	통과 (404.98ms, 42.9MB)
테스트 5 〉	통과 (251.88ms, 44.6MB)
테스트 6 〉	통과 (283.45ms, 45.5MB)
테스트 7 〉	통과 (396.32ms, 44.3MB)
테스트 8 〉	통과 (244.29ms, 46.1MB)
"""

# Queue로 풀기
from collections import deque
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    # queue 구성
    temp = []
    for i, time in enumerate(food_times):
        temp.append([time, i + 1])
    temp.sort(key = lambda x:x[0])
    q = deque(temp)
    
    prev = 0
    while q and k >= 0:
        time = q[0][0]
        acc = (time - prev) * len(q)
        if k < acc:
            break
        q.popleft()
        k -= acc
        prev = time
    
    result = [x[1] for x in sorted(q, key = lambda x:x[1])]
    return result[k % len(result)]
"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.1MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.1MB)
테스트 10 〉	통과 (0.02ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.1MB)
테스트 14 〉	통과 (0.02ms, 10.2MB)
테스트 15 〉	통과 (0.02ms, 10.3MB)
테스트 16 〉	통과 (0.00ms, 10.3MB)
테스트 17 〉	통과 (0.02ms, 10.1MB)
테스트 18 〉	통과 (0.02ms, 10.1MB)
테스트 19 〉	통과 (0.00ms, 10.1MB)
테스트 20 〉	통과 (0.00ms, 10.3MB)
테스트 21 〉	통과 (0.07ms, 10.2MB)
테스트 22 〉	통과 (0.09ms, 10.4MB)
테스트 23 〉	통과 (0.00ms, 10.2MB)
테스트 24 〉	통과 (0.80ms, 10.4MB)
테스트 25 〉	통과 (1.05ms, 10.2MB)
테스트 26 〉	통과 (1.17ms, 10.3MB)
테스트 27 〉	통과 (1.29ms, 10.5MB)
테스트 28 〉	통과 (0.02ms, 10.3MB)
테스트 29 〉	통과 (0.02ms, 10.3MB)
테스트 30 〉	통과 (0.01ms, 10.1MB)
테스트 31 〉	통과 (0.01ms, 10.2MB)
테스트 32 〉	통과 (0.03ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (219.55ms, 45.6MB)
테스트 2 〉	통과 (111.78ms, 45.3MB)
테스트 3 〉	통과 (242.18ms, 45MB)
테스트 4 〉	통과 (210.81ms, 45.1MB)
테스트 5 〉	통과 (291.78ms, 45.6MB)
테스트 6 〉	통과 (220.31ms, 45.8MB)
테스트 7 〉	통과 (279.38ms, 45.3MB)
테스트 8 〉	통과 (266.17ms, 46.6MB)
"""