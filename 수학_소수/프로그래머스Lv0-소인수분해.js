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

function makePrimeFactorization(n) {
  const primes = makePrimes(n)
  const primeNumbers = Array.from({ length: n + 1 }, (v, i) => i).filter((x) => primes[x])
  const result = {}
  for (const number of primeNumbers) {
    if (n % number === 0) {
      result[number] = 0
    }
    while (n % number === 0 && n > 1) {
      result[number]++
      n /= number
    }
    if (n === 1) break
  }
  return result
}

function solution(n) {
  const primeFactorization = makePrimeFactorization(n)
  return Object.keys(primeFactorization)
    .map((x) => Number(x)) // 자바스크립트 key는 문자열이다.
    .sort((a, b) => a - b)
}
// 정확성  테스트
// 테스트 1 〉	통과 (2.44ms, 33.7MB)
// 테스트 2 〉	통과 (0.15ms, 33.4MB)
// 테스트 3 〉	통과 (0.29ms, 33.4MB)
// 테스트 4 〉	통과 (0.28ms, 33.4MB)
// 테스트 5 〉	통과 (1.53ms, 33.7MB)
// 테스트 6 〉	통과 (0.56ms, 33.6MB)
// 테스트 7 〉	통과 (0.28ms, 33.4MB)
// 테스트 8 〉	통과 (0.43ms, 33.6MB)
// 테스트 9 〉	통과 (2.46ms, 33.6MB)
// 테스트 10 〉	통과 (0.78ms, 33.5MB)
// 테스트 11 〉	통과 (2.11ms, 33.6MB)
// 테스트 12 〉	통과 (1.64ms, 33.6MB)
// 테스트 13 〉	통과 (2.05ms, 33.8MB)
// 테스트 14 〉	통과 (2.36ms, 33.7MB)
// 테스트 15 〉	통과 (2.01ms, 33.8MB)
// 테스트 16 〉	통과 (1.91ms, 33.7MB)
// 테스트 17 〉	통과 (0.17ms, 33.5MB)
// 테스트 18 〉	통과 (0.16ms, 33.5MB)
// 테스트 19 〉	통과 (0.16ms, 33.6MB)
// 테스트 20 〉	통과 (0.35ms, 33.5MB)
// 테스트 21 〉	통과 (0.16ms, 33.5MB)
// 테스트 22 〉	통과 (0.28ms, 33.4MB)
// 테스트 23 〉	통과 (0.29ms, 33.5MB)
// 테스트 24 〉	통과 (1.50ms, 33.5MB)
