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