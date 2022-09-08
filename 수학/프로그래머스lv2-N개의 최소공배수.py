import math
def LCM(a:int, b:int)->int:
    if a > b:
        a, b = b, a
    gcd = math.gcd(a, b)
    if gcd == 1:
        return a * b
    if a // gcd == 1:
        return b
    else :
        return (a * b) // gcd

def solution(arr):
    arr.sort()
    n = len(arr)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n):
        dp[i + 1] = LCM(dp[i], arr[i])
        
    return dp[-1]

# 근데 사실 최소공배수는 그냥 (두 수의 곱 / 두 수의 최대공약수)임...
import math
def solution(arr):
    N = len(arr)
    arr.sort()
    
    DP = [0] * N
    DP[0] = arr[0]
    
    for i in range(1, N):
        a, b = DP[i - 1], arr[i]
        gcd = math.gcd(a, b)
        lcm = a * b // gcd
        DP[i] = lcm
    
    return DP[-1]
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.4MB)
테스트 5 〉	통과 (0.01ms, 10.4MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
"""