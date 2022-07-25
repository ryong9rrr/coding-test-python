function solution(s) {
  return s
    .split(' ')
    .map((word) => {
      return [...word].reduce((newWord, string, i) => {
        if (i % 2 === 0) {
          return newWord + string.toUpperCase()
        }
        return newWord + string.toLowerCase()
      }, '')
    })
    .join(' ')
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.13ms, 30.2MB)
// 테스트 2 〉	통과 (0.16ms, 30.2MB)
// 테스트 3 〉	통과 (0.08ms, 30.1MB)
// 테스트 4 〉	통과 (0.13ms, 30MB)
// 테스트 5 〉	통과 (0.13ms, 30MB)
// 테스트 6 〉	통과 (0.27ms, 30.1MB)
// 테스트 7 〉	통과 (0.13ms, 30MB)
// 테스트 8 〉	통과 (0.33ms, 30.1MB)
// 테스트 9 〉	통과 (0.09ms, 30MB)
// 테스트 10 〉	통과 (0.14ms, 30.1MB)
// 테스트 11 〉	통과 (0.13ms, 30.2MB)
// 테스트 12 〉	통과 (0.13ms, 30.1MB)
// 테스트 13 〉	통과 (0.14ms, 30.2MB)
// 테스트 14 〉	통과 (0.11ms, 30.1MB)
// 테스트 15 〉	통과 (0.12ms, 29.9MB)
// 테스트 16 〉	통과 (0.14ms, 29.8MB)
