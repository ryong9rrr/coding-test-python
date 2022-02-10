// a: number, b: number => number
function getGcd(a, b) {
  if (a % b === 0) return b;
  return getGcd(b, a % b);
}

let gcd = getGcd(15, 20); // 5
