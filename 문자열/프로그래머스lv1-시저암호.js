// String.prototype.charCodeAt(index) : string을 아스키넘버로 바꾼다. (index 디폴트는 0)
// String.fromCharCode(number) : number를 아스키문자로 바꾼다.
const pushedString = (string, standard, n) => {
  const stdAscii = standard.charCodeAt()
  const ascii = string.charCodeAt()
  const formattedNumber = ((ascii + n - stdAscii) % 26) + stdAscii
  return String.fromCharCode(formattedNumber)
}

const isUpper = (string) => {
  return 'A' <= string && string <= 'Z'
}

const pushString = (string, n) => {
  if (string === ' ') return string
  if (isUpper(string)) return pushedString(string, 'A', n)
  return pushedString(string, 'a', n)
}

function solution(s, n) {
  return [...s].map((string) => pushString(string, n)).join('')
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.16ms, 29.9MB)
// 테스트 2 〉	통과 (0.13ms, 30MB)
// 테스트 3 〉	통과 (0.10ms, 30MB)
// 테스트 4 〉	통과 (0.14ms, 30MB)
// 테스트 5 〉	통과 (0.12ms, 30MB)
// 테스트 6 〉	통과 (0.10ms, 30MB)
// 테스트 7 〉	통과 (0.17ms, 30.1MB)
// 테스트 8 〉	통과 (0.12ms, 30.2MB)
// 테스트 9 〉	통과 (0.14ms, 30MB)
// 테스트 10 〉	통과 (0.12ms, 30MB)
// 테스트 11 〉	통과 (0.15ms, 30MB)
// 테스트 12 〉	통과 (0.14ms, 30.1MB)
// 테스트 13 〉	통과 (21.31ms, 33.2MB)
