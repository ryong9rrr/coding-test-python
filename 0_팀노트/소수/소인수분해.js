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
