# 파라메트릭 서치
# 최적화 전
def solution(n, times):
    sorted_times = sorted(times)
    # 심사위원 1명이 처리할 시간의 최솟값
    left = sorted_times[0]
    # 심사위원 1명이 처리할 시간의 최댓값
    right = sorted_times[-1] * n
    
    # 심사위원 모두가 n명을 처리할 수 있는 최적시간(중간값)을 찾는다.
    while left <= right:
        mid = (left + right) // 2
        total = sum([mid // time for time in times])
        
        if total < n:
            left = mid + 1
        else:
            right = mid - 1
    
    return left
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.15ms, 10.1MB)
테스트 3 〉	통과 (6.42ms, 10MB)
테스트 4 〉	통과 (260.02ms, 18.9MB)
테스트 5 〉	통과 (414.71ms, 18.8MB)
테스트 6 〉	통과 (295.48ms, 18.7MB)
테스트 7 〉	통과 (548.58ms, 19MB)
테스트 8 〉	통과 (580.06ms, 18.6MB)
테스트 9 〉	통과 (0.04ms, 9.98MB)
"""

# 최적화
def solution(n, times):
    sorted_times = sorted(times)
    # 심사위원 1명이 처리할 시간의 최솟값
    left = sorted_times[0]
    # 심사위원 1명이 처리할 시간의 최댓값
    right = sorted_times[-1] * n
    
    # 심사위원 모두가 n명을 처리할 수 있는 최적시간(중간값)을 찾는다.
    while left <= right:
        mid = (left + right) // 2
        total = 0
        for time in times:
            total += mid // time
            if total >= n:
                break
        
        if total < n:
            left = mid + 1
        else:
            right = mid - 1
    
    return left
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.16ms, 10.3MB)
테스트 3 〉	통과 (6.53ms, 10.3MB)
테스트 4 〉	통과 (204.83ms, 14.9MB)
테스트 5 〉	통과 (346.90ms, 14.8MB)
테스트 6 〉	통과 (212.87ms, 15.2MB)
테스트 7 〉	통과 (412.15ms, 14.9MB)
테스트 8 〉	통과 (509.35ms, 14.8MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
"""