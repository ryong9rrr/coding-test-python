function solution(s) {
  return [...s].reduce((result, char, i) => {
    if (i === 0 || result[result.length - 1] === ' ') {
      result += char.toUpperCase()
    } else {
      result += char.toLowerCase()
    }
    return result
  }, '')
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.07ms, 33.4MB)
// 테스트 2 〉	통과 (0.09ms, 33.5MB)
// 테스트 3 〉	통과 (0.09ms, 33.4MB)
// 테스트 4 〉	통과 (0.09ms, 33.5MB)
// 테스트 5 〉	통과 (0.12ms, 33.4MB)
// 테스트 6 〉	통과 (0.10ms, 33.4MB)
// 테스트 7 〉	통과 (0.09ms, 33.4MB)
// 테스트 8 〉	통과 (0.07ms, 33.4MB)
// 테스트 9 〉	통과 (0.09ms, 33.4MB)
// 테스트 10 〉	통과 (0.05ms, 33.4MB)
// 테스트 11 〉	통과 (0.12ms, 33.4MB)
// 테스트 12 〉	통과 (0.08ms, 33.5MB)
// 테스트 13 〉	통과 (0.08ms, 33.4MB)
// 테스트 14 〉	통과 (0.09ms, 33.4MB)
// 테스트 15 〉	통과 (0.11ms, 33.5MB)
// 테스트 16 〉	통과 (0.07ms, 33.4MB)
// 테스트 17 〉	통과 (0.08ms, 33.4MB)
// 테스트 18 〉	통과 (0.05ms, 33.4MB)
