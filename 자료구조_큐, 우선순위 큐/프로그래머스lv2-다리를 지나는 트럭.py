# 두 개의 큐를 사용
from collections import deque
def solution(bridge_length, weight, truck_weights):
    queue = deque()
    bridge = deque()
    
    for truck in truck_weights:
        queue.append(truck)
    
    time = 0
    while queue or bridge:
        time += 1
        if bridge and bridge[0][1] + bridge_length == time:
            bridge.popleft()
            
        current_weights = sum([x[0] for x in bridge])
        
        if queue and current_weights + queue[0] <= weight:
            bridge.append((queue.popleft(), time))
        
    
    return time

"""
정확성  테스트
테스트 1 〉	통과 (1.12ms, 10.3MB)
테스트 2 〉	통과 (31.29ms, 10.3MB)
테스트 3 〉	통과 (0.08ms, 10.3MB)
테스트 4 〉	통과 (35.34ms, 10.2MB)
테스트 5 〉	통과 (298.59ms, 10.1MB)
테스트 6 〉	통과 (101.64ms, 10.1MB)
테스트 7 〉	통과 (0.88ms, 10.2MB)
테스트 8 〉	통과 (0.36ms, 10.3MB)
테스트 9 〉	통과 (4.50ms, 10.1MB)
테스트 10 〉	통과 (0.44ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.1MB)
테스트 12 〉	통과 (0.44ms, 10.3MB)
테스트 13 〉	통과 (1.28ms, 10.2MB)
테스트 14 〉	통과 (0.04ms, 10.1MB)
"""

# 하나의 큐만 사용 + sum() 사용 x
from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque()
    
    time = 0
    total = 0
    while truck_weights or bridge:
        time += 1
        if bridge and bridge[0][1] + bridge_length == time:
            total -= bridge[0][0]
            bridge.popleft()
        
        if truck_weights and total + truck_weights[-1] <= weight:
            total += truck_weights[-1]
            bridge.append((truck_weights.pop(), time))
        
    
    return time

"""
정확성  테스트
테스트 1 〉	통과 (0.61ms, 9.95MB)
테스트 2 〉	통과 (8.89ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (6.57ms, 10.2MB)
테스트 5 〉	통과 (54.94ms, 10.2MB)
테스트 6 〉	통과 (16.09ms, 10.3MB)
테스트 7 〉	통과 (0.33ms, 10.3MB)
테스트 8 〉	통과 (0.07ms, 10.2MB)
테스트 9 〉	통과 (2.34ms, 10.2MB)
테스트 10 〉	통과 (0.08ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
테스트 12 〉	통과 (0.14ms, 10.2MB)
테스트 13 〉	통과 (0.49ms, 10.1MB)
테스트 14 〉	통과 (0.03ms, 10.2MB)
"""