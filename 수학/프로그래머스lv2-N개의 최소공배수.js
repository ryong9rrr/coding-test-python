function GCD(a, b) {
  if (a % b === 0) return b
  return GCD(b, a % b)
}

function solution(arr) {
  const N = arr.length
  const sortedArr = arr.sort((a, b) => b - a)
  const DP = Array.from({ length: N }, (v, i) => 0)
  DP[0] = sortedArr[0]

  for (let i = 1; i < N; i++) {
    const a = DP[i - 1]
    const b = arr[i]
    const gcd = GCD(a, b)
    const lcm = (a * b) / gcd
    DP[i] = lcm
  }

  return DP[DP.length - 1]
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.16ms, 33.4MB)
// 테스트 2 〉	통과 (0.09ms, 33.5MB)
// 테스트 3 〉	통과 (0.09ms, 33.4MB)
// 테스트 4 〉	통과 (0.09ms, 33.4MB)
// 테스트 5 〉	통과 (0.09ms, 33.2MB)
// 테스트 6 〉	통과 (0.16ms, 33.4MB)
// 테스트 7 〉	통과 (0.16ms, 33.5MB)
// 테스트 8 〉	통과 (0.16ms, 33.1MB)
// 테스트 9 〉	통과 (0.17ms, 33.4MB)
// 테스트 10 〉	통과 (0.18ms, 33.4MB)
