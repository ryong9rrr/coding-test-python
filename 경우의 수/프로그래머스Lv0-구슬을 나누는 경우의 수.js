function countCombinations(n, m) {
  let denominator = 1
  let numerator = 1
  for (let i = n; i > m; i--) {
    denominator *= i
  }
  for (let i = n - m; i > 0; i--) {
    numerator *= i
  }
  return parseInt(denominator / numerator, 10)
}

function solution(balls, share) {
  return countCombinations(balls, share)
}
