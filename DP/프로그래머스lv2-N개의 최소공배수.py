import math
def LCM(a:int, b:int)->int:
    if a > b:
        a, b = b, a
    gcd = math.gcd(a, b)
    if gcd == 1:
        return a * b
    if a//gcd == 1:
        return b
    else :
        return (a * b) // gcd

def solution(arr):
    n = len(arr)
    #메모이제이션
    array = [0] * (n + 1)
    array[0] = 1
    #print(array)
    for i in range(0, n):
        array[i + 1] = LCM( array[i], arr[i] )
        
    return array[-1]

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
"""