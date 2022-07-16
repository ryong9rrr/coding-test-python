// 숫자를 인수로 받아 약수 배열을 반환하는 함수
const getDivisors = (number) => {
  const limit = Math.ceil(Math.sqrt(number))
  return Array.from({ length: limit }, (_, i) => i + 1).reduce((result, left) => {
    if (number % left === 0) {
      const right = number / left
      if (left === right) {
        return [...result, left]
      }
      return [...result, left, right]
    }
    return result
  }, [])
}
