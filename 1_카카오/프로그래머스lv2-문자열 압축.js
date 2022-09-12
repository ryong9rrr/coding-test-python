// unit: number, s: string => string[]
function divideString(unit, s) {
  let array = []
  for (let i = 0; i < s.length; i += unit) {
    array.push(s.slice(i, i + unit))
  }
  return array
}

function solution(s) {
  let result = s.length
  for (let unit = 1; unit < Math.floor(s.length / 2) + 1; unit++) {
    const array = divideString(unit, s)
    let temp = ''
    let count = 1
    let cur = array[0]
    for (let i = 1; i < array.length; i++) {
      if (cur === array[i]) {
        count++
      } else {
        if (count > 1) temp += String(count)
        temp += cur
        cur = array[i]
        count = 1
      }
    }
    if (count > 1) temp += String(count)
    temp += cur
    if (result > temp.length) {
      result = temp.length
    }
  }
  return result
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.17ms, 30.2MB)
// 테스트 2 〉	통과 (0.30ms, 30.1MB)
// 테스트 3 〉	통과 (0.21ms, 30.4MB)
// 테스트 4 〉	통과 (0.20ms, 30.3MB)
// 테스트 5 〉	통과 (0.06ms, 30.3MB)
// 테스트 6 〉	통과 (0.13ms, 30.4MB)
// 테스트 7 〉	통과 (0.33ms, 30.4MB)
// 테스트 8 〉	통과 (0.34ms, 30.3MB)
// 테스트 9 〉	통과 (0.49ms, 30.3MB)
// 테스트 10 〉	통과 (3.18ms, 32.6MB)
// 테스트 11 〉	통과 (0.18ms, 30MB)
// 테스트 12 〉	통과 (0.19ms, 30.3MB)
// 테스트 13 〉	통과 (0.19ms, 30.4MB)
// 테스트 14 〉	통과 (0.42ms, 30.2MB)
// 테스트 15 〉	통과 (0.16ms, 30.2MB)
// 테스트 16 〉	통과 (0.12ms, 30.1MB)
// 테스트 17 〉	통과 (1.29ms, 32.9MB)
// 테스트 18 〉	통과 (1.32ms, 33.1MB)
// 테스트 19 〉	통과 (1.37ms, 32.8MB)
// 테스트 20 〉	통과 (2.01ms, 32.8MB)
// 테스트 21 〉	통과 (1.94ms, 32.8MB)
// 테스트 22 〉	통과 (1.96ms, 32.7MB)
// 테스트 23 〉	통과 (1.97ms, 33MB)
// 테스트 24 〉	통과 (1.89ms, 32.7MB)
// 테스트 25 〉	통과 (1.94ms, 32.2MB)
// 테스트 26 〉	통과 (1.91ms, 32.9MB)
// 테스트 27 〉	통과 (2.00ms, 32.8MB)
// 테스트 28 〉	통과 (0.13ms, 30.2MB)

function solution(s) {
  const N = s.length
  const LIMIT = Math.floor(N / 2)

  let result = N

  for (let unit = 1; unit < LIMIT + 1; unit++) {
    const stack = []
    let count = 1
    for (let index = 0; index < N; index += unit) {
      const top = stack[stack.length - 1]
      const cur = s.slice(index, index + unit)
      if (top === cur) {
        count++
      } else {
        if (count > 1) {
          stack[stack.length - 1] = String(count) + top
          count = 1
        }
        stack.push(cur)
      }
    }
    if (count > 1) {
      stack[stack.length - 1] = String(count) + stack[stack.length - 1]
    }
    const compression = stack.join('')
    result = Math.min(result, compression.length)
  }
  return result
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.22ms, 33.5MB)
// 테스트 2 〉	통과 (0.38ms, 33.6MB)
// 테스트 3 〉	통과 (0.27ms, 33.5MB)
// 테스트 4 〉	통과 (0.19ms, 33.4MB)
// 테스트 5 〉	통과 (0.07ms, 33.4MB)
// 테스트 6 〉	통과 (0.19ms, 33.4MB)
// 테스트 7 〉	통과 (0.42ms, 33.5MB)
// 테스트 8 〉	통과 (0.44ms, 33.6MB)
// 테스트 9 〉	통과 (0.52ms, 33.6MB)
// 테스트 10 〉	통과 (1.62ms, 34.3MB)
// 테스트 11 〉	통과 (0.22ms, 33.5MB)
// 테스트 12 〉	통과 (0.22ms, 33.4MB)
// 테스트 13 〉	통과 (0.23ms, 33.4MB)
// 테스트 14 〉	통과 (0.56ms, 33.6MB)
// 테스트 15 〉	통과 (0.23ms, 33.4MB)
// 테스트 16 〉	통과 (0.08ms, 33.4MB)
// 테스트 17 〉	통과 (0.80ms, 33.8MB)
// 테스트 18 〉	통과 (0.76ms, 33.8MB)
// 테스트 19 〉	통과 (0.78ms, 33.7MB)
// 테스트 20 〉	통과 (4.44ms, 37.5MB)
// 테스트 21 〉	통과 (4.34ms, 37.5MB)
// 테스트 22 〉	통과 (4.40ms, 37.5MB)
// 테스트 23 〉	통과 (1.57ms, 34.4MB)
// 테스트 24 〉	통과 (1.57ms, 34.3MB)
// 테스트 25 〉	통과 (4.34ms, 37.6MB)
// 테스트 26 〉	통과 (1.63ms, 34.4MB)
// 테스트 27 〉	통과 (4.59ms, 37.6MB)
// 테스트 28 〉	통과 (0.18ms, 33.4MB)
