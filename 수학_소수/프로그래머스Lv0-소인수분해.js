function makePrimes(n) {
  const primes = Array.from({ length: n + 1 }, (v) => true)
  primes.splice(0, 2, false, false)
  for (let num = 2; num < Math.floor(Math.sqrt(n)) + 1; num++) {
    if (primes[num]) {
      for (let i = num * num; i < n + 1; i += num) {
        primes[i] = false
      }
    }
  }
  return primes
}

function solution(n) {
  const primes = makePrimes(n)
  const primeNumbers = []
  for (let i = 2; i < n + 1; i++) {
    if (primes[i]) primeNumbers.push(i)
  }
  const result = []
  for (const number of primeNumbers) {
    if (n % number === 0) {
      result.push(number)
    }
    while (n > 1 && n % number === 0) {
      n /= number
    }
    if (n == 1) {
      break
    }
  }
  return result
}
// 정확성  테스트
// 테스트 1 〉	통과 (2.32ms, 33.6MB)
// 테스트 2 〉	통과 (0.11ms, 33.6MB)
// 테스트 3 〉	통과 (0.27ms, 33.5MB)
// 테스트 4 〉	통과 (0.34ms, 33.4MB)
// 테스트 5 〉	통과 (1.38ms, 33.7MB)
// 테스트 6 〉	통과 (0.39ms, 33.6MB)
// 테스트 7 〉	통과 (0.30ms, 33.5MB)
// 테스트 8 〉	통과 (0.33ms, 33.5MB)
// 테스트 9 〉	통과 (1.78ms, 33.6MB)
// 테스트 10 〉	통과 (0.51ms, 33.4MB)
// 테스트 11 〉	통과 (1.83ms, 33.6MB)
// 테스트 12 〉	통과 (1.67ms, 33.5MB)
// 테스트 13 〉	통과 (1.40ms, 33.6MB)
// 테스트 14 〉	통과 (1.65ms, 33.5MB)
// 테스트 15 〉	통과 (1.25ms, 33.5MB)
// 테스트 16 〉	통과 (1.27ms, 33.7MB)
// 테스트 17 〉	통과 (0.14ms, 33.5MB)
// 테스트 18 〉	통과 (0.12ms, 33.6MB)
// 테스트 19 〉	통과 (0.11ms, 33.4MB)
// 테스트 20 〉	통과 (0.15ms, 33.4MB)
// 테스트 21 〉	통과 (0.11ms, 33.5MB)
// 테스트 22 〉	통과 (0.19ms, 33.5MB)
// 테스트 23 〉	통과 (0.23ms, 33.5MB)
// 테스트 24 〉	통과 (0.83ms, 33.5MB)
