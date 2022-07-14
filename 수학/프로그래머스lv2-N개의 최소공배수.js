function LCM(a, b) {
  function GCD(a, b) {
    if (a % b === 0) return b
    return GCD(b, a % b)
  }

  const gcd = GCD(a, b)
  return (a * b) / gcd
}

function solution(arr) {
  arr.sort()
  const dp = Array.from({ length: arr.length + 1 }, (v) => 0)
  dp[0] = 1

  for (let i = 0; i < arr.length; i++) {
    dp[i + 1] = LCM(dp[i], arr[i])
  }

  return dp[arr.length]
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.11ms, 30.1MB)
// 테스트 2 〉	통과 (0.14ms, 30.1MB)
// 테스트 3 〉	통과 (0.10ms, 30MB)
// 테스트 4 〉	통과 (0.42ms, 29.9MB)
// 테스트 5 〉	통과 (0.28ms, 29.8MB)
// 테스트 6 〉	통과 (0.11ms, 30.2MB)
// 테스트 7 〉	통과 (0.28ms, 30.2MB)
// 테스트 8 〉	통과 (0.11ms, 30.1MB)
// 테스트 9 〉	통과 (0.13ms, 30.1MB)
// 테스트 10 〉	통과 (0.40ms, 29.7MB)
