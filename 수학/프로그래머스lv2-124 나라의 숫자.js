const REMAINDER = ['4', '1', '2']

const divide = (number, result) => {
  if (number === 0) return result

  const a = Math.floor(number / 3)
  const b = number % 3

  if (b === 0) {
    return divide(a - 1, REMAINDER[b] + result)
  }
  return divide(a, REMAINDER[b] + result)
}

function solution(n) {
  return divide(n, '')
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.05ms, 30.2MB)
// 테스트 2 〉	통과 (0.07ms, 30MB)
// 테스트 3 〉	통과 (0.05ms, 29.7MB)
// 테스트 4 〉	통과 (0.05ms, 30.1MB)
// 테스트 5 〉	통과 (0.05ms, 30MB)
// 테스트 6 〉	통과 (0.06ms, 30MB)
// 테스트 7 〉	통과 (0.05ms, 30MB)
// 테스트 8 〉	통과 (0.05ms, 30.2MB)
// 테스트 9 〉	통과 (0.05ms, 29.8MB)
// 테스트 10 〉	통과 (0.07ms, 30.2MB)
// 테스트 11 〉	통과 (0.05ms, 29.9MB)
// 테스트 12 〉	통과 (0.06ms, 29.9MB)
// 테스트 13 〉	통과 (0.08ms, 30MB)
// 테스트 14 〉	통과 (0.07ms, 30.2MB)
// 효율성  테스트
// 테스트 1 〉	통과 (0.07ms, 30MB)
// 테스트 2 〉	통과 (0.05ms, 30.1MB)
// 테스트 3 〉	통과 (0.06ms, 30MB)
// 테스트 4 〉	통과 (0.05ms, 30MB)
// 테스트 5 〉	통과 (0.05ms, 30MB)
// 테스트 6 〉	통과 (0.08ms, 29.9MB)
