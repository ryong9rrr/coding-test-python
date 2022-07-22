function makePrimeNumbers(n) {
  const primeNumbers = Array.from({ length: n + 1 }, (v) => true)
  primeNumbers.splice(0, 2, false, false)
  for (let num = 2; num < Math.floor(Math.sqrt(n)) + 1; num++) {
    if (primeNumbers[num]) {
      for (let i = num * num; i < n + 1; i += num) {
        primeNumbers[i] = false
      }
    }
  }
  return primeNumbers
}

function solution(n) {
  const primeNumbers = makePrimeNumbers(n)
  return primeNumbers.reduce((acc, num) => (num ? acc + num : acc), 0)
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.25ms, 30.3MB)
// 테스트 2 〉	통과 (0.18ms, 30.1MB)
// 테스트 3 〉	통과 (0.37ms, 30.3MB)
// 테스트 4 〉	통과 (0.30ms, 30.1MB)
// 테스트 5 〉	통과 (0.43ms, 30.1MB)
// 테스트 6 〉	통과 (1.86ms, 30.1MB)
// 테스트 7 〉	통과 (0.73ms, 30.2MB)
// 테스트 8 〉	통과 (1.33ms, 30.3MB)
// 테스트 9 〉	통과 (4.37ms, 30.1MB)
// 테스트 10 〉	통과 (58.00ms, 34.3MB)
// 테스트 11 〉	통과 (181.27ms, 38.9MB)
// 테스트 12 〉	통과 (49.86ms, 34.6MB)
// 효율성  테스트
// 테스트 1 〉	통과 (152.31ms, 39MB)
// 테스트 2 〉	통과 (144.37ms, 38.9MB)
// 테스트 3 〉	통과 (149.04ms, 39.1MB)
// 테스트 4 〉	통과 (139.24ms, 38.9MB)
