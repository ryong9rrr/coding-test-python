// a: number, b: number => number
function GCD(a, b) {
  if (a % b === 0) return b
  return GCD(b, a % b)
}

function solution(w, h) {
  const gcd = GCD(w, h)
  const total = w * h
  const a = w / gcd
  const b = h / gcd
  const cut = gcd * (a + b - 1)
  return total - cut
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.05ms, 29.8MB)
// 테스트 2 〉	통과 (0.05ms, 30.2MB)
// 테스트 3 〉	통과 (0.04ms, 30.1MB)
// 테스트 4 〉	통과 (0.05ms, 29.8MB)
// 테스트 5 〉	통과 (0.06ms, 30.1MB)
// 테스트 6 〉	통과 (0.05ms, 30.1MB)
// 테스트 7 〉	통과 (0.05ms, 29.8MB)
// 테스트 8 〉	통과 (0.04ms, 30MB)
// 테스트 9 〉	통과 (0.05ms, 30.2MB)
// 테스트 10 〉	통과 (0.04ms, 30.1MB)
// 테스트 11 〉	통과 (0.04ms, 30MB)
// 테스트 12 〉	통과 (0.05ms, 30MB)
// 테스트 13 〉	통과 (0.08ms, 30MB)
// 테스트 14 〉	통과 (0.05ms, 30.1MB)
// 테스트 15 〉	통과 (0.05ms, 30MB)
// 테스트 16 〉	통과 (0.08ms, 30.1MB)
// 테스트 17 〉	통과 (0.05ms, 30MB)
// 테스트 18 〉	통과 (0.05ms, 30.1MB)
