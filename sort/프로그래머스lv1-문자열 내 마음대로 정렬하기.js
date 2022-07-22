const compare = (a, b, n) => {
  if (a[n] === b[n]) {
    return (a > b) - (a < b)
  }
  return (a[n] > b[n]) - (a[n] < b[n])
}

function solution(strings, n) {
  return strings.sort((a, b) => compare(a, b, n))
}
/*
정확성  테스트
테스트 1 〉	통과 (0.06ms, 29.9MB)
테스트 2 〉	통과 (0.10ms, 30.1MB)
테스트 3 〉	통과 (0.15ms, 30.1MB)
테스트 4 〉	통과 (0.09ms, 30MB)
테스트 5 〉	통과 (0.08ms, 30.2MB)
테스트 6 〉	통과 (0.13ms, 30.2MB)
테스트 7 〉	통과 (0.06ms, 30.3MB)
테스트 8 〉	통과 (0.08ms, 30.1MB)
테스트 9 〉	통과 (0.07ms, 29.9MB)
테스트 10 〉	통과 (0.15ms, 29.9MB)
테스트 11 〉	통과 (0.08ms, 29.9MB)
테스트 12 〉	통과 (0.10ms, 30.1MB)
*/

// string.prototype.localCompare() 사용
// alert('a'.localeCompare('b')); // -1
// alert('b'.localeCompare('a')); // 1
// alert('b'.localeCompare('b')); // 0
function solution(strings, n) {
  return strings.sort((a, b) => (a[n] == b[n] ? a.localeCompare(b) : a[n].localeCompare(b[n])))
}
// 정확성  테스트
// 테스트 1 〉	통과 (8.45ms, 31MB)
// 테스트 2 〉	통과 (16.07ms, 31MB)
// 테스트 3 〉	통과 (10.15ms, 30.9MB)
// 테스트 4 〉	통과 (13.73ms, 31.1MB)
// 테스트 5 〉	통과 (0.39ms, 31MB)
// 테스트 6 〉	통과 (0.42ms, 31MB)
// 테스트 7 〉	통과 (0.23ms, 31.1MB)
// 테스트 8 〉	통과 (0.25ms, 30.9MB)
// 테스트 9 〉	통과 (0.28ms, 30.9MB)
// 테스트 10 〉	통과 (0.27ms, 30.8MB)
// 테스트 11 〉	통과 (0.40ms, 31.1MB)
// 테스트 12 〉	통과 (0.42ms, 30.9MB)
