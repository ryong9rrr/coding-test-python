// number를 k진수로 변환시키는 함수
// number.toString(k) 와 같다.
function convertNumber(number, k) {
  let string = ''
  while (number > 0) {
    string = String(number % k) + string
    number = Math.floor(number / k)
  }
  return string
}
