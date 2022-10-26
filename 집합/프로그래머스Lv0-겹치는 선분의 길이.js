function solution(lines) {
  const table = Array.from({ length: 200 }, () => new Set())
  lines.forEach(([a, b], index) => {
    for (let i = a; i < b; i++) {
      table[i + 100].add(index)
    }
  })

  let count = 0
  table.forEach((line) => {
    if ([...line].length > 1) count++
  })
  return count
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.26ms, 33.6MB)
// 테스트 2 〉	통과 (0.28ms, 33.6MB)
// 테스트 3 〉	통과 (0.25ms, 33.6MB)
// 테스트 4 〉	통과 (0.26ms, 33.6MB)
// 테스트 5 〉	통과 (0.42ms, 33.5MB)
// 테스트 6 〉	통과 (0.26ms, 33.5MB)
// 테스트 7 〉	통과 (0.22ms, 33.5MB)
// 테스트 8 〉	통과 (0.27ms, 33.6MB)
// 테스트 9 〉	통과 (0.39ms, 33.5MB)
// 테스트 10 〉	통과 (0.23ms, 33.5MB)
