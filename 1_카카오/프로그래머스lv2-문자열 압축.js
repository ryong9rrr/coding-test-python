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
  const stringsLength = s.length
  const LIMIT = Math.floor(stringsLength / 2)
  let result = stringsLength

  for (let unit = 1; unit < LIMIT + 1; unit++) {
    const stack = []
    let count = 1
    for (let index = 0; index < stringsLength; index += unit) {
      const stackTop = stack[stack.length - 1]
      const cur = s.slice(index, index + unit)
      if (stackTop === cur) {
        count++
      } else {
        if (count > 1) {
          stack[stack.length - 1] = String(count) + stackTop
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
// 테스트 1 〉	통과 (0.12ms, 30.1MB)
// 테스트 2 〉	통과 (0.32ms, 29.9MB)
// 테스트 3 〉	통과 (0.21ms, 30.1MB)
// 테스트 4 〉	통과 (0.15ms, 29.9MB)
// 테스트 5 〉	통과 (0.08ms, 30.1MB)
// 테스트 6 〉	통과 (0.12ms, 30.1MB)
// 테스트 7 〉	통과 (0.34ms, 30.2MB)
// 테스트 8 〉	통과 (0.36ms, 30.3MB)
// 테스트 9 〉	통과 (0.43ms, 30MB)
// 테스트 10 〉	통과 (1.20ms, 30.1MB)
// 테스트 11 〉	통과 (0.15ms, 30.2MB)
// 테스트 12 〉	통과 (0.15ms, 30.1MB)
// 테스트 13 〉	통과 (0.16ms, 30.2MB)
// 테스트 14 〉	통과 (0.43ms, 30MB)
// 테스트 15 〉	통과 (0.17ms, 30.2MB)
// 테스트 16 〉	통과 (0.10ms, 29.9MB)
// 테스트 17 〉	통과 (0.74ms, 30.2MB)
// 테스트 18 〉	통과 (0.62ms, 30.1MB)
// 테스트 19 〉	통과 (0.74ms, 30.2MB)
// 테스트 20 〉	통과 (4.36ms, 33.2MB)
// 테스트 21 〉	통과 (5.33ms, 33MB)
// 테스트 22 〉	통과 (5.48ms, 33.2MB)
// 테스트 23 〉	통과 (1.31ms, 30.2MB)
// 테스트 24 〉	통과 (1.19ms, 30.1MB)
// 테스트 25 〉	통과 (4.39ms, 33.2MB)
// 테스트 26 〉	통과 (4.41ms, 33.2MB)
// 테스트 27 〉	통과 (5.79ms, 33.2MB)
// 테스트 28 〉	통과 (0.10ms, 30.3MB)
