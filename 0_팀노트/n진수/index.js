// number를 k진법으로 변환하는 함수
const toFix = (number, k) => {
  const FIX_TABLE = '0123456789ABCDEF'
  let result = ''
  while (number >= k) {
    result += FIX_TABLE[number % k]
    number = Math.floor(number / k)
  }
  result += FIX_TABLE[number]
  return [...result].reverse().join('')
}
