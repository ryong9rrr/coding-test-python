# 파라메트릭 서치(파라메트릭 서치는 반복문이 좀 더 편함)
# 최적화 전
def solution(n, times):
    sorted_times = sorted(times)
    # 심사위원 1명이 처리할 시간의 최솟값
    left = sorted_times[0]
    # 심사위원 1명이 처리할 시간의 최댓값
    right = sorted_times[-1] * n
    
    # 심사위원 모두가 n명을 처리할 수 있는 최적시간(중간값)을 찾는다. (등호는 반드시 =를 포함해야함.)
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
    times.sort()
    left, right = times[0], times[-1] * n
    
    def is_enough(mid):
        acc = 0
        for t in times:
            acc += (mid // t)
            if acc >= n:
                return True
        return False
    
    while left < right:
        mid = int((left / 2) + (right / 2))
        if is_enough(mid):
            right = mid
        else:
            left = mid + 1
    
    return left
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.07ms, 10.1MB)
테스트 3 〉	통과 (3.57ms, 10.2MB)
테스트 4 〉	통과 (126.37ms, 14.4MB)
테스트 5 〉	통과 (395.99ms, 14.1MB)
테스트 6 〉	통과 (231.79ms, 14.3MB)
테스트 7 〉	통과 (529.11ms, 14.3MB)
테스트 8 〉	통과 (589.53ms, 14.4MB)
테스트 9 〉	통과 (0.03ms, 10.1MB)
"""