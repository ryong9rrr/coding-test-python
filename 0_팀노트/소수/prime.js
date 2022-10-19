// 에라토스테네스의 체
// n은 범위
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

console.log(makePrimes(20)) // [false, false, true, true, false ....]

// 에라토스테네스의 체가 아닌 소수판별 알고리즘
function isPrime(number) {
  if (number <= 1) {
    return false
  }
  let i = 2
  while (i * i <= number) {
    if (number % i === 0) {
      return false
    }
    i++
  }
  return true
}
