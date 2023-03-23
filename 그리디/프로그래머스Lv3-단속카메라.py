def solution(routes):
    # 빠져나간 시점 순으로 정렬
    routes = sorted(routes, key = lambda x : x[1])
    
    # 설치된 카메라 위치
    cameras = []
    
    # 카메라를 만났는지
    def meet(i, j):
        for x in cameras:
            if i <= x and x <= j:
                return True
        return False
    
    for i, j in routes:
        if meet(i, j):
            continue
        # 카메라를 만나지 않았다면 빠져나가는 시점에 설치
        cameras.append(j)
    
    return len(cameras)
"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.1MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.06ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.06ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (1.36ms, 10.5MB)
테스트 2 〉	통과 (0.89ms, 10.4MB)
테스트 3 〉	통과 (3.55ms, 10.6MB)
테스트 4 〉	통과 (0.15ms, 10.1MB)
테스트 5 〉	통과 (4.13ms, 10.8MB)
"""