function solution(s) {
  let removedZero = 0
  let count = 0

  const change = (binary) => {
    if (binary === '1') return
    count++
    const prevN = binary.length
    const nextN = [...binary].filter((v) => v === '1').length
    removedZero += prevN - nextN
    change(nextN.toString(2))
  }

  change(s)

  return [count, removedZero]
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.08ms, 33.4MB)
// 테스트 2 〉	통과 (4.56ms, 36.9MB)
// 테스트 3 〉	통과 (0.08ms, 33.5MB)
// 테스트 4 〉	통과 (0.07ms, 33.4MB)
// 테스트 5 〉	통과 (0.07ms, 33.5MB)
// 테스트 6 〉	통과 (0.12ms, 33.6MB)
// 테스트 7 〉	통과 (0.15ms, 33.5MB)
// 테스트 8 〉	통과 (0.10ms, 33.4MB)
// 테스트 9 〉	통과 (4.99ms, 37.9MB)
// 테스트 10 〉	통과 (10.51ms, 38.2MB)
// 테스트 11 〉	통과 (4.29ms, 37.1MB)

// 엥 왜 while문이 더 오래걸리지
function solution(s) {
  let removedZero = 0
  let count = 0

  while (s !== '1') {
    count++
    const prevN = s.length
    const nextN = [...s].filter((v) => v === '1').length
    removedZero += prevN - nextN
    s = nextN.toString(2)
  }

  return [count, removedZero]
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.07ms, 33MB)
// 테스트 2 〉	통과 (22.46ms, 36.4MB)
// 테스트 3 〉	통과 (0.06ms, 33MB)
// 테스트 4 〉	통과 (0.06ms, 33MB)
// 테스트 5 〉	통과 (0.05ms, 33.4MB)
// 테스트 6 〉	통과 (0.10ms, 33.4MB)
// 테스트 7 〉	통과 (0.21ms, 33.4MB)
// 테스트 8 〉	통과 (0.09ms, 33.4MB)
// 테스트 9 〉	통과 (25.26ms, 37.6MB)
// 테스트 10 〉	통과 (24.53ms, 38.2MB)
// 테스트 11 〉	통과 (24.79ms, 37MB)
