function solution(phone_number) {
  const stars = '*'.repeat(phone_number.length - 4)
  return stars + phone_number.slice(-4)
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.03ms, 30.2MB)
// 테스트 2 〉	통과 (0.04ms, 30.2MB)
// 테스트 3 〉	통과 (0.03ms, 30MB)
// 테스트 4 〉	통과 (0.03ms, 30.1MB)
// 테스트 5 〉	통과 (0.03ms, 30.1MB)
// 테스트 6 〉	통과 (0.11ms, 29.8MB)
// 테스트 7 〉	통과 (0.04ms, 30MB)
// 테스트 8 〉	통과 (0.03ms, 29.8MB)
// 테스트 9 〉	통과 (0.07ms, 29.9MB)
// 테스트 10 〉	통과 (0.03ms, 30.2MB)
// 테스트 11 〉	통과 (0.04ms, 30.1MB)
// 테스트 12 〉	통과 (0.03ms, 30.1MB)
// 테스트 13 〉	통과 (0.06ms, 30MB)
