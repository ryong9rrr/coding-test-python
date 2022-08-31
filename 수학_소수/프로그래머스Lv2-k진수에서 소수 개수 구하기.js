function isPrime(number) {
  if (number <= 1) {
    return false
  }
  let i = 2
  while (i * i <= number) {
    if (number % i === 0) {
      return false
    }
    i++
  }
  return true
}

// number.toString(k)...와 같다.
function convertNumber(number, k) {
  let string = ''
  while (number > 0) {
    string = String(number % k) + string
    number = Math.floor(number / k)
  }
  return string
}

function solution(n, k) {
  const convertedNumber = convertNumber(n, k)
  const numbers = convertedNumber.split('0').filter((n) => n !== '')

  let result = 0
  for (const number of numbers) {
    if (isPrime(number)) {
      result++
    }
  }
  return result
}
// 정확성 테스트
// 테스트 1 〉 통과 (208.81ms, 34.8MB)
// 테스트 2 〉 통과 (0.13ms, 30.3MB)
// 테스트 3 〉 통과 (0.16ms, 30.1MB)
// 테스트 4 〉 통과 (0.16ms, 29.8MB)
// 테스트 5 〉 통과 (0.14ms, 29.9MB)
// 테스트 6 〉 통과 (0.11ms, 30MB)
// 테스트 7 〉 통과 (0.13ms, 30.1MB)
// 테스트 8 〉 통과 (0.11ms, 30MB)
// 테스트 9 〉 통과 (0.11ms, 29.9MB)
// 테스트 10 〉 통과 (0.13ms, 30MB)
// 테스트 11 〉 통과 (0.18ms, 29.8MB)
// 테스트 12 〉 통과 (0.16ms, 30.2MB)
// 테스트 13 〉 통과 (0.14ms, 30MB)
// 테스트 14 〉 통과 (0.11ms, 29.8MB)
// 테스트 15 〉 통과 (0.11ms, 30.1MB)
// 테스트 16 〉 통과 (0.18ms, 29.9MB)
