import heapq
def solution(n, works):
    if sum(works) <= n :
        return 0
    
    heap = []
    for work in works:
        heapq.heappush(heap, -work) # 최소힙 구성을 위해 음수처리
    
    while n:
        x = heapq.heappop(heap)
        x += 1 # 최소힙을 구성하기 위해 음수처리 한 것이므로
        heapq.heappush(heap, x)
        n -= 1
        
    ans = 0
    while heap:
        x = heapq.heappop(heap)
        ans += (-x) ** 2
        
    return ans
"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (0.03ms, 9.98MB)
테스트 4 〉	통과 (0.05ms, 10.1MB)
테스트 5 〉	통과 (0.05ms, 10.1MB)
테스트 6 〉	통과 (0.02ms, 10MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.57ms, 10.2MB)
테스트 9 〉	통과 (1.39ms, 9.99MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.1MB)
테스트 13 〉	통과 (0.00ms, 9.98MB)
효율성  테스트
테스트 1 〉	통과 (395.70ms, 10.3MB)
테스트 2 〉	통과 (370.85ms, 10.3MB)
"""