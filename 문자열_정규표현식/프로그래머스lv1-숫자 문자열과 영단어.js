function solution(s) {
  const NUMBERS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

  NUMBERS.forEach((number, i) => {
    const re = new RegExp(number, 'g')
    s = s.replace(re, String(i))
  })

  return Number(s)
}
// 정확성 테스트
// 테스트 1 〉 통과 (0.10ms, 30.2MB)
// 테스트 2 〉 통과 (0.10ms, 30.2MB)
// 테스트 3 〉 통과 (0.08ms, 30.2MB)
// 테스트 4 〉 통과 (0.08ms, 29.9MB)
// 테스트 5 〉 통과 (0.08ms, 30.1MB)
// 테스트 6 〉 통과 (0.08ms, 29.9MB)
// 테스트 7 〉 통과 (0.08ms, 30.1MB)
// 테스트 8 〉 통과 (0.10ms, 30MB)
// 테스트 9 〉 통과 (0.08ms, 30.1MB)
// 테스트 10 〉 통과 (0.08ms, 30.4MB)
