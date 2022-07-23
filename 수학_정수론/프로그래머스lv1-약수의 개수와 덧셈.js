function solution(left, right) {
  function measure(number) {
    let nums = []
    const c = Math.sqrt(number)
    for (var i = 1; i < c; i++) {
      if (number % i == 0) {
        nums.push(i)
        nums.push(number / i)
      }
    }
    if (number % c == 0) {
      nums.push(c)
    }

    return nums.length
  }
  let result = 0
  for (var num = left; num <= right; num++) {
    let r = measure(num)
    r % 2 == 0 ? (result += num) : (result -= num)
  }
  return result
}
// 정확성  테스트
// 테스트 1 〉	통과 (2.21ms, 32.8MB)
// 테스트 2 〉	통과 (0.57ms, 30.1MB)
// 테스트 3 〉	통과 (0.66ms, 30.2MB)
// 테스트 4 〉	통과 (0.13ms, 29.9MB)
// 테스트 5 〉	통과 (1.74ms, 32.6MB)
// 테스트 6 〉	통과 (0.24ms, 29.9MB)
// 테스트 7 〉	통과 (0.18ms, 30MB)

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

function solution(left, right) {
  let result = 0
  for (let number = left; number <= right; number++) {
    const n = getDivisors(number).length
    if (n % 2 === 0) {
      result += number
    } else {
      result -= number
    }
  }
  return result
}
// 정확성  테스트
// 테스트 1 〉	통과 (22.93ms, 33.2MB)
// 테스트 2 〉	통과 (1.41ms, 29.9MB)
// 테스트 3 〉	통과 (1.93ms, 30.2MB)
// 테스트 4 〉	통과 (0.58ms, 30.1MB)
// 테스트 5 〉	통과 (23.95ms, 33.3MB)
// 테스트 6 〉	통과 (0.66ms, 30.2MB)
// 테스트 7 〉	통과 (0.44ms, 30.1MB)
