function solution(n, m) {
  let x, y
  if (n <= m) {
    x = n
    y = m
  } else {
    x = m
    y = n
  }

  const nums = [1]
  let num = 2
  while (num <= x) {
    if (x % num == 0 && y % num == 0) {
      nums.push(num)
      x /= num
      y /= num
    } else {
      num++
    }
  }
  const GCD = nums.reduce((a, b) => a * b)
  const LCM = GCD * x * y
  return [GCD, LCM]
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.07ms, 29.9MB)
// 테스트 2 〉	통과 (0.09ms, 29.9MB)
// 테스트 3 〉	통과 (0.07ms, 29.9MB)
// 테스트 4 〉	통과 (0.07ms, 29.9MB)
// 테스트 5 〉	통과 (0.07ms, 29.8MB)
// 테스트 6 〉	통과 (0.08ms, 30MB)
// 테스트 7 〉	통과 (0.07ms, 30MB)
// 테스트 8 〉	통과 (0.07ms, 30MB)
// 테스트 9 〉	통과 (0.10ms, 29.9MB)
// 테스트 10 〉	통과 (0.07ms, 29.7MB)
// 테스트 11 〉	통과 (0.10ms, 30MB)
// 테스트 12 〉	통과 (0.13ms, 30.1MB)
// 테스트 13 〉	통과 (0.10ms, 30MB)
// 테스트 14 〉	통과 (0.11ms, 30.1MB)
// 테스트 15 〉	통과 (0.08ms, 30MB)
// 테스트 16 〉	통과 (0.11ms, 29.8MB)

function GCD(a, b) {
  if (a % b === 0) return b
  return GCD(b, a % b)
}

function solution(n, m) {
  const gcd = GCD(n, m)
  const lcm = (n * m) / gcd
  return [gcd, lcm]
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.04ms, 30.1MB)
// 테스트 2 〉	통과 (0.04ms, 30.1MB)
// 테스트 3 〉	통과 (0.08ms, 29.9MB)
// 테스트 4 〉	통과 (0.04ms, 30.1MB)
// 테스트 5 〉	통과 (0.04ms, 29.9MB)
// 테스트 6 〉	통과 (0.06ms, 29.9MB)
// 테스트 7 〉	통과 (0.04ms, 30MB)
// 테스트 8 〉	통과 (0.07ms, 29.9MB)
// 테스트 9 〉	통과 (0.04ms, 29.8MB)
// 테스트 10 〉	통과 (0.04ms, 30MB)
// 테스트 11 〉	통과 (0.04ms, 30MB)
// 테스트 12 〉	통과 (0.05ms, 29.7MB)
// 테스트 13 〉	통과 (0.06ms, 30.1MB)
// 테스트 14 〉	통과 (0.05ms, 30.1MB)
// 테스트 15 〉	통과 (0.04ms, 30MB)
// 테스트 16 〉	통과 (0.12ms, 30MB)
