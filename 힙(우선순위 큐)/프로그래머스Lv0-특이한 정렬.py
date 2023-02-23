import heapq
def find_standard_index(numlist, n):
    index = 0
    for i, number in enumerate(numlist):
        if abs(number - n) < abs(numlist[index] - n):
            index = i
    return index

def solution(numlist, n):
    heap = []
    index = find_standard_index(numlist, n)
    
    for i, number in enumerate(numlist):
        heapq.heappush(heap, (abs(number - n), -number))
    
    result = []
    while heap:
        diff, opposite_number = heapq.heappop(heap)
        result.append(-opposite_number)
    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.2MB)
테스트 2 〉	통과 (0.07ms, 10.3MB)
테스트 3 〉	통과 (0.05ms, 10.3MB)
테스트 4 〉	통과 (0.04ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 10.4MB)
"""

# 근데 걍 정렬로 풀면 됨;;
def solution(numlist, n):
    return sorted(numlist, key = lambda x: (abs(x - n), -x))
"""
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.05ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 10.2MB)
"""