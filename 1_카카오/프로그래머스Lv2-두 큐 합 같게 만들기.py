# 큐를 사용한 풀이
from collections import deque
def solution(queue1, queue2):
    LIMIT = len(queue1) * 4
    
    a_sum = sum(queue1)
    b_sum = sum(queue2)
    a_queue = deque(queue1)
    b_queue = deque(queue2)
    
    answer = 0
    
    # 현재 합이 더 큰 쪽에서 뺀다.
    while a_queue and b_queue and answer < LIMIT:   
        if a_sum < b_sum:
            x = b_queue.popleft()
            b_sum -= x
            a_queue.append(x)
            a_sum += x
            answer += 1
        elif a_sum > b_sum:
            x = a_queue.popleft()
            a_sum -= x
            b_queue.append(x)
            b_sum += x
            answer += 1
        else:
            return answer

    return -1
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 9.95MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.03ms, 10.1MB)
테스트 6 〉	통과 (0.03ms, 10.1MB)
테스트 7 〉	통과 (0.04ms, 10MB)
테스트 8 〉	통과 (0.04ms, 10.4MB)
테스트 9 〉	통과 (0.08ms, 10.1MB)
테스트 10 〉	통과 (0.19ms, 10.2MB)
테스트 11 〉	통과 (43.13ms, 14.6MB)
테스트 12 〉	통과 (10.14ms, 14.7MB)
테스트 13 〉	통과 (3.59ms, 12MB)
테스트 14 〉	통과 (2.53ms, 12.2MB)
테스트 15 〉	통과 (8.99ms, 18.1MB)
테스트 16 〉	통과 (3.34ms, 18.5MB)
테스트 17 〉	통과 (3.30ms, 17.6MB)
테스트 18 〉	통과 (10.01ms, 33MB)
테스트 19 〉	통과 (16.20ms, 37.5MB)
테스트 20 〉	통과 (27.47ms, 37.7MB)
테스트 21 〉	통과 (20.16ms, 37.8MB)
테스트 22 〉	통과 (62.80ms, 37.7MB)
테스트 23 〉	통과 (41.48ms, 37.7MB)
테스트 24 〉	통과 (95.77ms, 37.8MB)
테스트 25 〉	통과 (0.05ms, 10.1MB)
테스트 26 〉	통과 (0.02ms, 10.1MB)
테스트 27 〉	통과 (0.03ms, 10MB)
테스트 28 〉	통과 (81.67ms, 19.2MB)
테스트 29 〉	통과 (0.31ms, 11MB)
테스트 30 〉	통과 (44.23ms, 19MB)
"""

# 포인터 풀이
def solution(queue1, queue2):
    LIMIT = len(queue1) * 4
    
    a_sum = sum(queue1)
    b_sum = sum(queue2)
    a_index = b_index = 0
    
    answer = 0
    
    # 현재 합이 더 큰 쪽에서 뺀다.
    while a_index < len(queue1) and b_index < len(queue2) and answer < LIMIT:   
        if a_sum < b_sum:
            x = queue2[b_index]
            b_index += 1
            b_sum -= x
            queue1.append(x)
            a_sum += x
            answer += 1
        elif a_sum > b_sum:
            x = queue1[a_index]
            a_index += 1
            a_sum -= x
            queue2.append(x)
            b_sum += x
            answer += 1
        else:
            return answer
        
    return -1
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.4MB)
테스트 4 〉	통과 (0.01ms, 9.9MB)
테스트 5 〉	통과 (0.04ms, 10.1MB)
테스트 6 〉	통과 (0.04ms, 10.3MB)
테스트 7 〉	통과 (0.04ms, 10.4MB)
테스트 8 〉	통과 (0.02ms, 10.1MB)
테스트 9 〉	통과 (0.04ms, 10.2MB)
테스트 10 〉	통과 (0.21ms, 10.2MB)
테스트 11 〉	통과 (90.57ms, 15.1MB)
테스트 12 〉	통과 (15.15ms, 13.7MB)
테스트 13 〉	통과 (1.39ms, 11.1MB)
테스트 14 〉	통과 (0.88ms, 11.3MB)
테스트 15 〉	통과 (4.77ms, 16.8MB)
테스트 16 〉	통과 (1.45ms, 17.4MB)
테스트 17 〉	통과 (1.09ms, 16.5MB)
테스트 18 〉	통과 (3.49ms, 29.8MB)
테스트 19 〉	통과 (6.56ms, 34.3MB)
테스트 20 〉	통과 (47.28ms, 34.4MB)
테스트 21 〉	통과 (14.26ms, 34.8MB)
테스트 22 〉	통과 (72.29ms, 35MB)
테스트 23 〉	통과 (55.08ms, 35.8MB)
테스트 24 〉	통과 (105.76ms, 35.8MB)
테스트 25 〉	통과 (0.06ms, 10.2MB)
테스트 26 〉	통과 (0.03ms, 9.9MB)
테스트 27 〉	통과 (0.03ms, 10.2MB)
테스트 28 〉	통과 (128.53ms, 20.7MB)
테스트 29 〉	통과 (0.12ms, 10.8MB)
테스트 30 〉	통과 (69.48ms, 19.2MB)
"""