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
def LCM(a:int, b:int)->int:
    gcd = math.gcd(a, b)
    return (a * b) // gcd

def solution(arr):
    arr.sort()
    n = len(arr)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n):
        dp[i + 1] = LCM(dp[i], arr[i])
        
    return dp[-1]

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.4MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
"""

"""js
function LCM(a, b){
    function GCD(a, b) {
      if (a % b === 0) return b;
      return GCD(b, a % b);
    }

    const gcd = GCD(a, b);
    return (a * b) / gcd
}

function solution(arr) {
    arr.sort();
    const dp = Array.from({length: arr.length + 1}, (v) => 0);
    dp[0] = 1;

    for (let i = 0; i < arr.length; i++){
        dp[i + 1] = LCM(dp[i], arr[i])
    }

    return dp[arr.length]
}

정확성  테스트
테스트 1 〉	통과 (0.11ms, 30.1MB)
테스트 2 〉	통과 (0.14ms, 30.1MB)
테스트 3 〉	통과 (0.10ms, 30MB)
테스트 4 〉	통과 (0.42ms, 29.9MB)
테스트 5 〉	통과 (0.28ms, 29.8MB)
테스트 6 〉	통과 (0.11ms, 30.2MB)
테스트 7 〉	통과 (0.28ms, 30.2MB)
테스트 8 〉	통과 (0.11ms, 30.1MB)
테스트 9 〉	통과 (0.13ms, 30.1MB)
테스트 10 〉	통과 (0.40ms, 29.7MB)
"""