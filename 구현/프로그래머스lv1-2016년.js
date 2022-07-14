function solution(a, b) {
  const month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  const week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

  const days = a > 1 ? month.slice(0, a - 1).reduce((a, b) => a + b) + b - 1 : b - 1
  const answer = days % 7
  return week[answer]
}
