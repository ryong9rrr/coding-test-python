#과거풀이
def solution(n):
    def return_thr(n) :
        ans = []
        while(n>2) :
            ans.append(n%3)
            n = n//3
        ans.append(n)
        return ans #[0,0,2,1]
    
    def return_ten(arr) :
        arr = list(reversed(arr))
        sum = 0
        for i in range(0, len(arr)) :
            sum = sum + (3**i)*arr[i]
        return sum
    
    return return_ten(return_thr(n))

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.1MB)
"""

import math
def solution(n):
    c = int(math.log(n, 3))
    d = 3 ** c
    # three는 c + 1의 자릿수를 가짐
    three = ""
    while n > 0:
        three += str(n // d)
        n %= d
        d //= 3
        
    if len(three) < (c + 1):
        three += "0" * (c + 1 - len(three))
    
    result = 0
    for i, number in enumerate(three):
        p = 3 ** i
        result += int(number) * p
        
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.02ms, 10.4MB)
테스트 5 〉	통과 (0.02ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
테스트 7 〉	통과 (0.03ms, 10.4MB)
테스트 8 〉	통과 (0.03ms, 10.4MB)
테스트 9 〉	통과 (0.03ms, 10.4MB)
테스트 10 〉	통과 (0.03ms, 10.4MB)
"""

# 더 스마트한 풀이
def solution(n):
    three = ""
    while n:
        three += str(n % 3)
        n //= 3
        
    return int(three, 3)

"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.5MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.4MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.4MB)
테스트 7 〉	통과 (0.02ms, 10.4MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
"""

def number_to_three(number):
    result = ""
    while number > 2:
        result = str(number % 3) + result
        number //= 3
    result = str(number % 3) + result
    return result
    
def solution(n):
    result = 0
    for i, s in enumerate(number_to_three(n)):
        result += 3 ** i * int(s)
    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.03ms, 10.3MB)
테스트 9 〉	통과 (0.03ms, 10.1MB)
테스트 10 〉	통과 (0.04ms, 10.3MB)
"""