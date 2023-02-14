// 내장 메서드 사용, 64ms(84.99%), 42.3MB(82.83%)
// a, b의 길이가 최대 10^4 라는 점에서 그냥 `parseInt`로 해버리면 오버플로우가 발생해서 안됨.
/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function (a, b) {
  const aBin = `0b${a}`
  const bBin = `0b${b}`
  return (BigInt(aBin) + BigInt(bBin)).toString(2)
}

// 이진수 덧셈 구현 : 76ms(40.41%), 44.1MB(21.86%)
/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function (a, b) {
  const maxLen = a.length > b.length ? a.length : b.length

  a = "0".repeat(maxLen - a.length) + a
  b = "0".repeat(maxLen - b.length) + b

  let result = ""
  let carry = 0
  for (let i = maxLen - 1; i >= 0; i -= 1) {
    const binA = Number(a[i])
    const binB = Number(b[i])
    const x = binA ^ binB ^ carry
    result += String(x)
    carry = binA + binB + carry >= 2 ? 1 : 0
  }

  if (carry) {
    result += "1" // carry가 존재하면 carry는 1임.
  }

  return [...result].reverse().join("")
}
