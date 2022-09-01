function compare(a, b) {
  return Number(a + b) < Number(b + a) ? -1 : 1
}

function solution(numbers) {
  const result = numbers
    .map((n) => n.toString())
    .sort(compare)
    .reverse()
  return result[0] === '0' ? '0' : result.join('')
}
// 정확성  테스트
// 테스트 1 〉	통과 (124.67ms, 39.4MB)
// 테스트 2 〉	통과 (67.38ms, 36.8MB)
// 테스트 3 〉	통과 (150.39ms, 45.9MB)
// 테스트 4 〉	통과 (4.33ms, 32.3MB)
// 테스트 5 〉	통과 (100.77ms, 38.2MB)
// 테스트 6 〉	통과 (91.87ms, 38.6MB)
// 테스트 7 〉	통과 (0.18ms, 29.9MB)
// 테스트 8 〉	통과 (0.11ms, 30MB)
// 테스트 9 〉	통과 (0.10ms, 30MB)
// 테스트 10 〉	통과 (0.08ms, 30MB)
// 테스트 11 〉	통과 (0.11ms, 29.9MB)
// 테스트 12 〉	통과 (0.07ms, 30MB)
// 테스트 13 〉	통과 (0.07ms, 30MB)
// 테스트 14 〉	통과 (0.11ms, 29.9MB)
// 테스트 15 〉	통과 (0.07ms, 30.1MB)
