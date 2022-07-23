// n은 범위

function makePrimeNumbers(n) {
  const primeNumbers = Array.from({ length: n + 1 }, (v) => true);
  primeNumbers.splice(0, 2, false, false);
  for (let num = 2; num < Math.floor(Math.sqrt(n)) + 1; num++) {
    if (primeNumbers[num]) {
      for (let i = num * num; i < n + 1; i += num) {
        primeNumbers[i] = false;
      }
    }
  }
  return primeNumbers;
}

console.log(makePrimeNumbers(20)); // [false, false, true, true, false ....]
