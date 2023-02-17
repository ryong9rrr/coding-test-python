from collections import Counter
def solution(topping):
    b = Counter(topping)
    b_set = set(topping)
    a_set = set()
    
    result = 0
    for x in topping:
        a_set.add(x)
        b[x] -= 1
        if b[x] == 0:
            b_set.remove(x)
            
        if len(a_set) == len(b_set):
            result += 1

    return result
"""
정확성  테스트
테스트 1 〉	통과 (4.74ms, 10.5MB)
테스트 2 〉	통과 (55.50ms, 15.5MB)
테스트 3 〉	통과 (42.99ms, 10.8MB)
테스트 4 〉	통과 (42.80ms, 10.8MB)
테스트 5 〉	통과 (398.36ms, 18.5MB)
테스트 6 〉	통과 (570.39ms, 51.2MB)
테스트 7 〉	통과 (576.42ms, 51.4MB)
테스트 8 〉	통과 (588.36ms, 51.4MB)
테스트 9 〉	통과 (586.40ms, 50.5MB)
테스트 10 〉	통과 (513.99ms, 50.6MB)
테스트 11 〉	통과 (39.73ms, 10.8MB)
테스트 12 〉	통과 (7.62ms, 11.8MB)
테스트 13 〉	통과 (557.96ms, 50.5MB)
테스트 14 〉	통과 (713.47ms, 50.6MB)
테스트 15 〉	통과 (605.66ms, 50.6MB)
테스트 16 〉	통과 (558.74ms, 50.5MB)
테스트 17 〉	통과 (544.84ms, 50.5MB)
테스트 18 〉	통과 (560.58ms, 51.2MB)
테스트 19 〉	통과 (591.57ms, 51.4MB)
테스트 20 〉	통과 (593.56ms, 51.2MB)
"""

# 최적화
from collections import Counter
def solution(topping):
    b = Counter(topping)
    
    a_set = set()
    a_length = 0
    b_length = len(set(topping)) 
    
    result = 0
    for x in topping:
        if x not in a_set:
            a_set.add(x)
            a_length += 1
        
        b[x] -= 1
        if b[x] == 0:
            b_length -= 1
        
        if a_length > b_length:
            break
        
        if a_length == b_length:
            result += 1

    return result
"""
정확성  테스트
테스트 1 〉	통과 (2.33ms, 10.4MB)
테스트 2 〉	통과 (26.58ms, 14.7MB)
테스트 3 〉	통과 (34.95ms, 10.8MB)
테스트 4 〉	통과 (35.02ms, 10.9MB)
테스트 5 〉	통과 (324.16ms, 18.7MB)
테스트 6 〉	통과 (307.18ms, 51.3MB)
테스트 7 〉	통과 (276.15ms, 51.2MB)
테스트 8 〉	통과 (440.26ms, 51.4MB)
테스트 9 〉	통과 (80.18ms, 50.5MB)
테스트 10 〉	통과 (81.66ms, 50.6MB)
테스트 11 〉	통과 (15.87ms, 10.8MB)
테스트 12 〉	통과 (3.13ms, 11.4MB)
테스트 13 〉	통과 (428.67ms, 50.5MB)
테스트 14 〉	통과 (432.64ms, 50.5MB)
테스트 15 〉	통과 (413.17ms, 50.5MB)
테스트 16 〉	통과 (343.16ms, 50.4MB)
테스트 17 〉	통과 (327.05ms, 50.7MB)
테스트 18 〉	통과 (307.15ms, 51.3MB)
테스트 19 〉	통과 (180.34ms, 51.2MB)
테스트 20 〉	통과 (152.53ms, 51.3MB)
"""