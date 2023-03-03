import heapq
from collections import defaultdict

def solution(operations):
    max_heap = []
    min_heap = []
    
    counter = defaultdict(int)

    for operation in operations:
        command, x = operation.split(" ")
        
        # 힙에 원소 삽입
        if command == "I":
            number = int(x)
            heapq.heappush(max_heap, -number)
            heapq.heappush(min_heap, number)
            counter[number] += 1
            continue
        
        # 최대값 삭제
        if x == "1" and max_heap:
            max_number = -heapq.heappop(max_heap)
            counter[max_number] -= 1
        
        # 최소값 삭제
        if x == "-1" and min_heap:
            min_number = heapq.heappop(min_heap)
            counter[min_number] -= 1
        
        # 최대힙의 top이 제거된 원소라면 계속 제거
        while max_heap and counter[-max_heap[0]] <= 0:
            heapq.heappop(max_heap)
        
        # 최소힙의 top이 제거된 원소라면 계속 제거
        while min_heap and counter[min_heap[0]] <= 0:
            heapq.heappop(min_heap)

    max_number = -max_heap[0] if max_heap else 0
    min_number = min_heap[0] if min_heap else 0

    return [max_number, min_number]
"""
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.04ms, 10.4MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.03ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
"""