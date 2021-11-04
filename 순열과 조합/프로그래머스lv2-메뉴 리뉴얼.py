import itertools
from collections import defaultdict
def solution(orders, course):
    orders = sorted(orders, key = lambda x : len(x))
    max_length = orders[-1]
    # 경우의 수
    c = defaultdict(int)
    for order in orders:
        order = sorted(order)
        l = len(order)
        for i in range(2, l+1):
            temp = ""
            nCr = list(itertools.combinations(order, i))
            for t in nCr:
                r = "".join(t)
                c[r] += 1
    #print(c)
    numbers = []
    for i in course:
        _max = 0
        current = []
        for k in c.keys():
            l = len(k)
            if i == l and _max <= c[k]:
                _max = c[k]
        numbers.append(_max)
    
    result = []
    for i in range(len(course)):
        number = numbers[i]
        _course = course[i]
        for k in c.keys():
            if c[k] == number and len(k) == _course and c[k] != 1:
                result.append(k)
                
    result = sorted(result)
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.14ms, 10.3MB)
테스트 2 〉	통과 (0.09ms, 10.2MB)
테스트 3 〉	통과 (0.12ms, 10.3MB)
테스트 4 〉	통과 (0.12ms, 10.4MB)
테스트 5 〉	통과 (0.10ms, 10.3MB)
테스트 6 〉	통과 (0.27ms, 10.3MB)
테스트 7 〉	통과 (0.50ms, 10.3MB)
테스트 8 〉	통과 (3.80ms, 10.5MB)
테스트 9 〉	통과 (3.12ms, 10.5MB)
테스트 10 〉	통과 (4.87ms, 10.9MB)
테스트 11 〉	통과 (3.12ms, 10.6MB)
테스트 12 〉	통과 (2.85ms, 10.7MB)
테스트 13 〉	통과 (6.94ms, 10.9MB)
테스트 14 〉	통과 (8.34ms, 10.9MB)
테스트 15 〉	통과 (6.46ms, 11MB)
테스트 16 〉	통과 (3.44ms, 10.6MB)
테스트 17 〉	통과 (7.05ms, 10.9MB)
테스트 18 〉	통과 (8.07ms, 11MB)
테스트 19 〉	통과 (4.55ms, 10.6MB)
테스트 20 〉	통과 (8.64ms, 10.6MB)
"""