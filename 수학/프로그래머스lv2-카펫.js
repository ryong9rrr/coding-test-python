function solution(brown, yellow) {
  const sum = brown + yellow

  for (let i = 3; i < Math.floor(Math.sqrt(sum)) + 1; i++) {
    if (sum / i === Math.floor(sum / i)) {
      let x = i
      let y = sum / i

      if ((x - 2) * (y - 2) === yellow) return [y, x]
    }
  }

  return console.log('입력 값이 올바르지 않아요.')
}
