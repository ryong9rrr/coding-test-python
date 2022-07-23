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

function solution(n) {
  const divisors = getDivisors(n)
  return divisors.reduce((a, b) => a + b)
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.11ms, 29.9MB)
// 테스트 2 〉	통과 (0.29ms, 30MB)
// 테스트 3 〉	통과 (0.15ms, 30MB)
// 테스트 4 〉	통과 (0.14ms, 30MB)
// 테스트 5 〉	통과 (0.15ms, 30.2MB)
// 테스트 6 〉	통과 (0.15ms, 30MB)
// 테스트 7 〉	통과 (0.29ms, 30MB)
// 테스트 8 〉	통과 (0.15ms, 29.7MB)
// 테스트 9 〉	통과 (0.15ms, 30.2MB)
// 테스트 10 〉	통과 (0.33ms, 30MB)
// 테스트 11 〉	통과 (0.15ms, 30MB)
// 테스트 12 〉	통과 (0.26ms, 29.9MB)
// 테스트 13 〉	통과 (0.27ms, 30MB)
// 테스트 14 〉	통과 (0.12ms, 29.8MB)
// 테스트 15 〉	통과 (0.15ms, 29.9MB)
// 테스트 16 〉	통과 (0.07ms, 29.7MB)
// 테스트 17 〉	통과 (0.15ms, 29.9MB)
