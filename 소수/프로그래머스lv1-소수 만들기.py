def solution(nums):
    n = int(sum(nums))
    sosu = [True] * (n+1)
    sosu[0:2] = [False, False]
    for num in range(2, int(n**0.5)+1) :
        if sosu[num] :
            for i in range(num*num, n+1, num) :
                sosu[i] = False
    #print(f"sosu : {sosu}")
    
    result = 0
    leng = len(nums)
    for i in range(0, leng-2) :
        for j in range(i+1, leng-1) :
            for k in range(j+1, leng) :
                print(i,j,k)
                if sosu[nums[i]+nums[j]+nums[k]] :
                    result += 1
    
    return result

"""
정확성  테스트
테스트 1 〉	통과 (2.99ms, 10.4MB)
테스트 2 〉	통과 (4.31ms, 10.4MB)
테스트 3 〉	통과 (0.74ms, 10.5MB)
테스트 4 〉	통과 (0.59ms, 10.5MB)
테스트 5 〉	통과 (4.27ms, 10.5MB)
테스트 6 〉	통과 (5.65ms, 10.5MB)
테스트 7 〉	통과 (0.28ms, 10.3MB)
테스트 8 〉	통과 (13.92ms, 10.5MB)
테스트 9 〉	통과 (1.32ms, 10.4MB)
테스트 10 〉	통과 (12.36ms, 10.5MB)
테스트 11 〉	통과 (0.14ms, 10.3MB)
테스트 12 〉	통과 (0.07ms, 10.3MB)
테스트 13 〉	통과 (0.31ms, 10.3MB)
테스트 14 〉	통과 (0.07ms, 10.3MB)
테스트 15 〉	통과 (0.07ms, 10.3MB)
테스트 16 〉	통과 (13.87ms, 10.5MB)
테스트 17 〉	통과 (19.66ms, 10.5MB)
테스트 18 〉	통과 (0.45ms, 10.3MB)
테스트 19 〉	통과 (0.33ms, 10.4MB)
테스트 20 〉	통과 (20.60ms, 10.5MB)
테스트 21 〉	통과 (16.75ms, 10.5MB)
테스트 22 〉	통과 (3.89ms, 10.5MB)
테스트 23 〉	통과 (0.02ms, 10.3MB)
테스트 24 〉	통과 (13.90ms, 10.5MB)
테스트 25 〉	통과 (14.27ms, 10.5MB)
테스트 26 〉	통과 (0.02ms, 10.3MB)
"""

import itertools
def solution(nums):
    n = sum(sorted(nums)[-3:])
    sosu = [True] * (n + 1)
    
    #sosu array 만들기
    for i in range(2, int(n*0.5) + 1):
        if sosu[i]:
            for j in range(i**2, n + 1, i):
                sosu[j] = False
    
    #조합찾기
    nCr = list(itertools.combinations(nums, 3))
    result = 0
    for i in nCr:
        if sosu[sum(i)]:
            result += 1
            
    return result
            
"""
정확성  테스트
테스트 1 〉	통과 (0.70ms, 10.3MB)
테스트 2 〉	통과 (0.91ms, 10.4MB)
테스트 3 〉	통과 (0.17ms, 10.3MB)
테스트 4 〉	통과 (0.26ms, 10.2MB)
테스트 5 〉	통과 (0.99ms, 10.4MB)
테스트 6 〉	통과 (1.44ms, 10.4MB)
테스트 7 〉	통과 (0.14ms, 10.3MB)
테스트 8 〉	통과 (3.63ms, 11.1MB)
테스트 9 〉	통과 (0.32ms, 10.3MB)
테스트 10 〉	통과 (3.23ms, 10.9MB)
테스트 11 〉	통과 (0.03ms, 10.3MB)
테스트 12 〉	통과 (0.04ms, 10.2MB)
테스트 13 〉	통과 (0.04ms, 10.2MB)
테스트 14 〉	통과 (0.03ms, 10.3MB)
테스트 15 〉	통과 (0.02ms, 10.2MB)
테스트 16 〉	통과 (3.76ms, 11MB)
테스트 17 〉	통과 (4.59ms, 11.3MB)
테스트 18 〉	통과 (0.30ms, 10.3MB)
테스트 19 〉	통과 (0.32ms, 10.3MB)
테스트 20 〉	통과 (4.57ms, 11.3MB)
테스트 21 〉	통과 (4.32ms, 11.3MB)
테스트 22 〉	통과 (0.99ms, 10.3MB)
테스트 23 〉	통과 (0.01ms, 10.3MB)
테스트 24 〉	통과 (3.76ms, 11MB)
테스트 25 〉	통과 (3.49ms, 11MB)
테스트 26 〉	통과 (0.01ms, 10.2MB)
"""