// string.prototype.slice()
// 참고) slice는 array.prototype, string.prototype 둘다 지원한다.
function solution(s) {
  const mid = parseInt(s.length / 2)
  return s.length % 2 == 0 ? s.slice(mid - 1, mid + 1) : s[mid]
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.04ms, 30.2MB)
// 테스트 2 〉	통과 (0.04ms, 30.2MB)
// 테스트 3 〉	통과 (0.04ms, 30.1MB)
// 테스트 4 〉	통과 (0.04ms, 29.8MB)
// 테스트 5 〉	통과 (0.05ms, 30MB)
// 테스트 6 〉	통과 (0.04ms, 30.1MB)
// 테스트 7 〉	통과 (0.04ms, 30.1MB)
// 테스트 8 〉	통과 (0.04ms, 29.6MB)
// 테스트 9 〉	통과 (0.05ms, 30.2MB)
// 테스트 10 〉	통과 (0.08ms, 30.1MB)
// 테스트 11 〉	통과 (0.04ms, 30.2MB)
// 테스트 12 〉	통과 (0.06ms, 30.2MB)
// 테스트 13 〉	통과 (0.04ms, 30.2MB)
// 테스트 14 〉	통과 (0.04ms, 30.2MB)
// 테스트 15 〉	통과 (0.03ms, 30.2MB)
// 테스트 16 〉	통과 (0.04ms, 30.1MB)

// string.prototype.substring()
function solution(s) {
  const isEven = s.length % 2 === 0
  const mid = Math.floor(s.length / 2)
  return isEven ? s.substring(mid - 1, mid + 1) : s.substring(mid, mid + 1)
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.04ms, 30MB)
// 테스트 2 〉	통과 (0.04ms, 30.1MB)
// 테스트 3 〉	통과 (0.04ms, 30MB)
// 테스트 4 〉	통과 (0.08ms, 30MB)
// 테스트 5 〉	통과 (0.04ms, 30.1MB)
// 테스트 6 〉	통과 (0.04ms, 30.1MB)
// 테스트 7 〉	통과 (0.04ms, 30.2MB)
// 테스트 8 〉	통과 (0.04ms, 29.5MB)
// 테스트 9 〉	통과 (0.04ms, 29.8MB)
// 테스트 10 〉	통과 (0.04ms, 30.2MB)
// 테스트 11 〉	통과 (0.04ms, 30.1MB)
// 테스트 12 〉	통과 (0.04ms, 30MB)
// 테스트 13 〉	통과 (0.04ms, 30MB)
// 테스트 14 〉	통과 (0.04ms, 30MB)
// 테스트 15 〉	통과 (0.04ms, 30MB)
// 테스트 16 〉	통과 (0.07ms, 30MB)
