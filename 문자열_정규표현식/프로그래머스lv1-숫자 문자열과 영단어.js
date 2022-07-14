function solution(s) {
  const NUMBER_TABLE = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
  ]

  let result = s

  NUMBER_TABLE.forEach((numberStr, index) => {
    const reg = new RegExp(numberStr, 'g')
    result = result.replace(reg, index.toString())
  })

  return parseInt(result, 10)
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.10ms, 30.1MB)
// 테스트 2 〉	통과 (0.11ms, 30.2MB)
// 테스트 3 〉	통과 (0.10ms, 30.2MB)
// 테스트 4 〉	통과 (0.08ms, 30MB)
// 테스트 5 〉	통과 (0.09ms, 29.9MB)
// 테스트 6 〉	통과 (0.12ms, 30.1MB)
// 테스트 7 〉	통과 (0.12ms, 30MB)
// 테스트 8 〉	통과 (0.10ms, 30MB)
// 테스트 9 〉	통과 (0.17ms, 29.9MB)
// 테스트 10 〉	통과 (0.11ms, 30.2MB)
