const getDivisors = (number) => {
  if (number <= 0) throw new Error('자연수가 아니에요.')
  const limit = Math.floor(Math.sqrt(number))
  const divisors = []
  for (let left = 1; left < limit + 1; left++) {
    if (number % left === 0) {
      const right = number / left
      divisors.push(left)
      if (left !== right) {
        divisors.push(right)
      }
    }
  }
  return divisors
}

function solution(n) {
  return getDivisors(n).filter((x) => x % 2 === 1).length
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.16ms, 33.6MB)
// 테스트 2 〉	통과 (0.18ms, 33.5MB)
// 테스트 3 〉	통과 (0.18ms, 33.5MB)
// 테스트 4 〉	통과 (0.12ms, 33.5MB)
// 테스트 5 〉	통과 (0.11ms, 33.4MB)
// 테스트 6 〉	통과 (0.16ms, 33.5MB)
// 테스트 7 〉	통과 (0.18ms, 33.5MB)
// 테스트 8 〉	통과 (0.16ms, 33.4MB)
// 테스트 9 〉	통과 (0.16ms, 33.5MB)
// 테스트 10 〉	통과 (0.11ms, 33.4MB)
// 테스트 11 〉	통과 (0.11ms, 33.4MB)
// 테스트 12 〉	통과 (0.17ms, 33.6MB)
// 테스트 13 〉	통과 (0.26ms, 33.5MB)
// 테스트 14 〉	통과 (0.17ms, 33.5MB)
// 테스트 15 〉	통과 (0.16ms, 33.6MB)
// 테스트 16 〉	통과 (0.19ms, 33.4MB)
// 테스트 17 〉	통과 (0.10ms, 33.5MB)
// 테스트 18 〉	통과 (0.15ms, 33.5MB)
// 효율성  테스트
// 테스트 1 〉	통과 (0.21ms, 33.4MB)
// 테스트 2 〉	통과 (0.19ms, 33.4MB)
// 테스트 3 〉	통과 (0.19ms, 33.5MB)
// 테스트 4 〉	통과 (0.25ms, 33.4MB)
// 테스트 5 〉	통과 (0.19ms, 33.4MB)
// 테스트 6 〉	통과 (0.20ms, 33.4MB)
