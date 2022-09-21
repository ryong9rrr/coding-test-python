# 그리디 + 투포인터
def solution(people, limit):
    people.sort()
    
    left = 0
    right = len(people) - 1
    
    count = 0
    
    while left <= right:
        weight = people[left] + people[right]
        if weight > limit:
            right -= 1
        else:
            left += 1
            right -= 1
        count += 1
            
    return count
"""
정확성  테스트
테스트 1 〉	통과 (0.81ms, 10.3MB)
테스트 2 〉	통과 (0.80ms, 10.1MB)
테스트 3 〉	통과 (0.58ms, 10.2MB)
테스트 4 〉	통과 (0.52ms, 10.2MB)
테스트 5 〉	통과 (0.31ms, 10.1MB)
테스트 6 〉	통과 (0.28ms, 10.1MB)
테스트 7 〉	통과 (0.46ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.1MB)
테스트 9 〉	통과 (0.05ms, 10.2MB)
테스트 10 〉	통과 (0.56ms, 10.1MB)
테스트 11 〉	통과 (0.47ms, 10.3MB)
테스트 12 〉	통과 (0.43ms, 10.2MB)
테스트 13 〉	통과 (0.57ms, 10.1MB)
테스트 14 〉	통과 (0.84ms, 10.1MB)
테스트 15 〉	통과 (0.11ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (8.66ms, 10.6MB)
테스트 2 〉	통과 (9.97ms, 10.6MB)
테스트 3 〉	통과 (8.51ms, 10.5MB)
테스트 4 〉	통과 (9.62ms, 10.5MB)
테스트 5 〉	통과 (8.68ms, 10.5MB)
"""