def solution(left, right):
    def measure(number) :
        nums = []
        c = int(number ** 0.5)
        for i in range(1, c+1) :
            if number % i == 0 :
                if i == number//i :
                    nums.append(i)
                else :
                    nums.append(i)
                    nums.append(number//i)
        
        return len(nums)
    
    result = 0
    for num in range(left, right+1) :
        r = measure(num)
        if r % 2 == 0 :
            result += num
        else :
            result -= num
    
    return result

"""
정확성  테스트
테스트 1 〉	통과 (2.22ms, 10.3MB)
테스트 2 〉	통과 (0.91ms, 10.3MB)
테스트 3 〉	통과 (2.13ms, 10.3MB)
테스트 4 〉	통과 (0.22ms, 10.3MB)
테스트 5 〉	통과 (2.23ms, 10.3MB)
테스트 6 〉	통과 (0.25ms, 10.2MB)
테스트 7 〉	통과 (0.16ms, 10.2MB)
"""

def solution(left, right):
    #약수의 개수를 반환하는 함수
    def get_divisor_number(x:int)->int:
        result = 0
        for i in range(1, int(x**0.5) + 1):
            if x % i == 0:
                if i == x**0.5:
                    result += 1
                else:
                    result += 2
        return result
    
    result = 0                    
    for i in range(left, right + 1):
        x = get_divisor_number(i)
        if x % 2 == 0:
            result += i
        else:
            result -= i
    
    return result

"""
정확성  테스트
테스트 1 〉	통과 (1.93ms, 10.3MB)
테스트 2 〉	통과 (0.51ms, 10.3MB)
테스트 3 〉	통과 (0.70ms, 10.3MB)
테스트 4 〉	통과 (0.13ms, 10.3MB)
테스트 5 〉	통과 (1.61ms, 10.3MB)
테스트 6 〉	통과 (0.15ms, 10.3MB)
테스트 7 〉	통과 (0.09ms, 10.4MB)
"""

def solution(left, right):
    #제곱수를 가지면 무조건 약수의 개수는 홀수임
    result = 0
    for i in range(left, right + 1):
        if int(i ** 0.5) == i ** 0.5:
            result -= i
        else:
            result += i
    
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.44ms, 10.3MB)
테스트 2 〉	통과 (0.21ms, 10.3MB)
테스트 3 〉	통과 (0.17ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.30ms, 10.3MB)
테스트 6 〉	통과 (0.05ms, 10.3MB)
테스트 7 〉	통과 (0.04ms, 10.3MB)
"""