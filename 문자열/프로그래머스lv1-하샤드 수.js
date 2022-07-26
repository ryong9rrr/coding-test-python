const isHarshad = (number) => {
  const sum = [...String(number)].reduce((total, number) => {
    return total + parseInt(number, 10)
  }, 0)
  return number % sum === 0
}

function solution(x) {
  return isHarshad(x)
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.06ms, 29.9MB)
// 테스트 2 〉	통과 (0.08ms, 30.1MB)
// 테스트 3 〉	통과 (0.06ms, 29.9MB)
// 테스트 4 〉	통과 (0.12ms, 30.1MB)
// 테스트 5 〉	통과 (0.06ms, 30.1MB)
// 테스트 6 〉	통과 (0.06ms, 29.8MB)
// 테스트 7 〉	통과 (0.06ms, 30MB)
// 테스트 8 〉	통과 (0.06ms, 30.1MB)
// 테스트 9 〉	통과 (0.06ms, 30.1MB)
// 테스트 10 〉	통과 (0.06ms, 29.8MB)
// 테스트 11 〉	통과 (0.06ms, 30.2MB)
// 테스트 12 〉	통과 (0.08ms, 30.1MB)
// 테스트 13 〉	통과 (0.06ms, 30MB)
// 테스트 14 〉	통과 (0.14ms, 30.1MB)
// 테스트 15 〉	통과 (0.09ms, 30.1MB)
// 테스트 16 〉	통과 (0.06ms, 30.1MB)
// 테스트 17 〉	통과 (0.06ms, 30.1MB)
