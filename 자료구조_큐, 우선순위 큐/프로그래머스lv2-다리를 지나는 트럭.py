from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque(truck_weights)
    bridge = deque()
    
    bridge_weight = 0
    time = 0
    while q or bridge:
        time += 1
        if bridge and bridge[0][1] + bridge_length == time:
            bridge_weight -= bridge[0][0]
            bridge.popleft()
        
        if q and q[0] + bridge_weight <= weight:
            truck = q.popleft()
            bridge_weight += truck
            bridge.append((truck, time))
    
    return time

"""
정확성  테스트
테스트 1 〉	통과 (0.77ms, 10MB)
테스트 2 〉	통과 (12.88ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (6.05ms, 10.1MB)
테스트 5 〉	통과 (86.62ms, 10.3MB)
테스트 6 〉	통과 (26.21ms, 10MB)
테스트 7 〉	통과 (0.60ms, 10MB)
테스트 8 〉	통과 (0.11ms, 10.4MB)
테스트 9 〉	통과 (3.87ms, 10.2MB)
테스트 10 〉	통과 (0.09ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.23ms, 10.1MB)
테스트 13 〉	통과 (0.53ms, 10.3MB)
테스트 14 〉	통과 (0.03ms, 10.3MB)
"""