// 숫자를 인수로 받아 약수 배열을 반환하는 함수
const getDivisors = (number) => {
  if (number < 0) throw new Error('숫자는 0 이상의 정수여야합니다.')
  if (number === 0) return [0]
  const limit = Math.floor(Math.sqrt(number))
  const iters = Array.from({ length: limit }, (_, i) => i + 1)
  return iters.reduce((divisors, left) => {
    if (number % left === 0) {
      const right = number / left
      if (left === right) {
        divisors.push(left)
        return divisors
      }
      divisors.push(left)
      divisors.push(right)
      return divisors
    }
    return divisors
  }, [])
}
