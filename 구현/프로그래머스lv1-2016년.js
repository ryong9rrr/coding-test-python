// "FRI"가 0번째 인덱스면 안된다. 이렇게 풀면 답은 맞지만 별로 안좋음.
function solution(a, b) {
  const month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  const week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

  const days = a > 1 ? month.slice(0, a - 1).reduce((a, b) => a + b) + b - 1 : b - 1
  const answer = days % 7
  return week[answer]
}

// 이렇게 "FRI"를 1번째 인덱스로 보내줘야 깔끔함.
function solution(a, b) {
  const MONTH_DAYS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  const WEEKS = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']

  const days = MONTH_DAYS.slice(0, a - 1).reduce((a, b) => a + b, 0) + b

  return WEEKS[days % 7]
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.12ms, 30.1MB)
// 테스트 2 〉	통과 (0.04ms, 30.1MB)
// 테스트 3 〉	통과 (0.05ms, 29.7MB)
// 테스트 4 〉	통과 (0.06ms, 29.7MB)
// 테스트 5 〉	통과 (0.06ms, 30MB)
// 테스트 6 〉	통과 (0.06ms, 29.9MB)
// 테스트 7 〉	통과 (0.11ms, 29.7MB)
// 테스트 8 〉	통과 (0.06ms, 30MB)
// 테스트 9 〉	통과 (0.08ms, 30MB)
// 테스트 10 〉	통과 (0.06ms, 29.8MB)
// 테스트 11 〉	통과 (0.06ms, 30.1MB)
// 테스트 12 〉	통과 (0.06ms, 30MB)
// 테스트 13 〉	통과 (0.06ms, 30MB)
// 테스트 14 〉	통과 (0.06ms, 30MB)
