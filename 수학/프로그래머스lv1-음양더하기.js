// reduce를 이용한 풀이

function solution(absolutes, signs) {
  return absolutes.reduce((acc, cur, i) => (signs[i] ? acc + cur : acc - cur), 0)
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.09ms, 29.8MB)
// 테스트 2 〉	통과 (0.09ms, 29.9MB)
// 테스트 3 〉	통과 (0.10ms, 30.1MB)
// 테스트 4 〉	통과 (0.11ms, 30.1MB)
// 테스트 5 〉	통과 (0.09ms, 30.2MB)
// 테스트 6 〉	통과 (0.09ms, 30MB)
// 테스트 7 〉	통과 (0.09ms, 30.1MB)
// 테스트 8 〉	통과 (0.10ms, 30MB)
// 테스트 9 〉	통과 (0.17ms, 30.1MB)
