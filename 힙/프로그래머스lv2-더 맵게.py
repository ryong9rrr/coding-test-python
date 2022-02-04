import heapq
def solution(scoville, K):
    heap = scoville[:]
    heapq.heapify(heap)
    
    count = 0
    while heap[0] < K:
        if len(heap) < 2:
            return -1
        first, second = heapq.heappop(heap), heapq.heappop(heap)
        new = first + 2 * second
        count += 1
        heapq.heappush(heap, new)
        
    return count

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.79ms, 10.3MB)
테스트 7 〉	통과 (0.60ms, 10.2MB)
테스트 8 〉	통과 (0.05ms, 10.3MB)
테스트 9 〉	통과 (0.07ms, 10.2MB)
테스트 10 〉	통과 (0.36ms, 10.2MB)
테스트 11 〉	통과 (0.20ms, 10.2MB)
테스트 12 〉	통과 (1.32ms, 10.2MB)
테스트 13 〉	통과 (0.68ms, 10.2MB)
테스트 14 〉	통과 (0.02ms, 10.2MB)
테스트 15 〉	통과 (0.59ms, 10.4MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (162.28ms, 18.2MB)
테스트 2 〉	통과 (376.33ms, 25.6MB)
테스트 3 〉	통과 (1795.25ms, 62.1MB)
테스트 4 〉	통과 (138.14ms, 16.7MB)
테스트 5 〉	통과 (1944.68ms, 64.8MB)
"""