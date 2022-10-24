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

function solution(a, b) {
  const numerator = makePrimeFactorization(a)
  const denominator = makePrimeFactorization(b)

  for (const [key, value] of Object.entries(numerator)) {
    if (key in denominator) {
      denominator[key] = Math.max(0, denominator[key] - value)
    }
  }

  for (const [key, value] of Object.entries(denominator)) {
    if (key === '2' || key === '5') continue
    if (value > 0) return 2
  }
  return 1
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.43ms, 33.2MB)
// 테스트 2 〉	통과 (0.55ms, 33.4MB)
// 테스트 3 〉	통과 (0.33ms, 33.5MB)
// 테스트 4 〉	통과 (0.39ms, 33.4MB)
// 테스트 5 〉	통과 (0.41ms, 33.4MB)
// 테스트 6 〉	통과 (0.36ms, 33.5MB)
// 테스트 7 〉	통과 (0.52ms, 33.5MB)
// 테스트 8 〉	통과 (0.47ms, 33.6MB)
// 테스트 9 〉	통과 (0.37ms, 33.4MB)
// 테스트 10 〉	통과 (0.66ms, 33.5MB)
// 테스트 11 〉	통과 (0.35ms, 33.4MB)
// 테스트 12 〉	통과 (0.48ms, 33.4MB)
// 테스트 13 〉	통과 (0.28ms, 33.4MB)
// 테스트 14 〉	통과 (0.30ms, 33.4MB)
// 테스트 15 〉	통과 (0.30ms, 33.5MB)
