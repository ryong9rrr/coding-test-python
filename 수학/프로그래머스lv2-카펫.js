function solution(brown, yellow) {
  const total = brown + yellow

  for (let x = 2; x < Math.floor(total ** 0.5) + 1; x++) {
    const b = total / x
    if (b !== Math.floor(b)) {
      continue
    }
    const y = Math.floor(b)
    if ((x - 2) * (y - 2) === yellow) {
      return [x, y].sort((a, b) => b - a)
    }
  }
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.07ms, 33.4MB)
// 테스트 2 〉	통과 (0.07ms, 33.6MB)
// 테스트 3 〉	통과 (0.26ms, 33.5MB)
// 테스트 4 〉	통과 (0.07ms, 33.4MB)
// 테스트 5 〉	통과 (0.08ms, 33.5MB)
// 테스트 6 〉	통과 (0.21ms, 33.5MB)
// 테스트 7 〉	통과 (0.26ms, 33.5MB)
// 테스트 8 〉	통과 (0.27ms, 33.5MB)
// 테스트 9 〉	통과 (0.25ms, 33.5MB)
// 테스트 10 〉	통과 (0.29ms, 33.5MB)
// 테스트 11 〉	통과 (0.06ms, 33.4MB)
// 테스트 12 〉	통과 (0.06ms, 33.4MB)
// 테스트 13 〉	통과 (0.07ms, 33.5MB)
