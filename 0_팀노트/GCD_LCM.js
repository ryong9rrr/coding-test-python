// 최대공약수
// a: number, b: number => number
function GCD(a, b) {
  if (a % b === 0) return b
  return GCD(b, a % b)
}

let gcd = GCD(15, 20) // 5

// 최소공배수
function LCM(a, b) {
  function GCD(a, b) {
    if (a % b === 0) return b
    return GCD(b, a % b)
  }

  const gcd = GCD(a, b)
  return (a * b) / gcd
}
