//js 다시 풀었는데 또 스택으로 풀었네...
function isDigit(string) {
  return !Number.isNaN(Number(string))
}

function solution(s) {
  const dict = {}
  const stack = []
  for (const char of s) {
    if (stack[stack.length - 1] && (char === '}' || char === ',')) {
      const x = stack.pop()
      if (!dict[x]) {
        dict[x] = 0
      }
      dict[x]++
    }
    if (isDigit(char)) {
      if (stack[stack.length - 1]) {
        stack.push(stack.pop() + char)
      } else {
        stack.push(char)
      }
    }
  }

  const result = Object.entries(dict)
    .sort((a, b) => b[1] - a[1])
    .map((x) => Number(x[0]))

  return result
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.18ms, 29.8MB)
// 테스트 2 〉	통과 (0.18ms, 30MB)
// 테스트 3 〉	통과 (0.25ms, 30.1MB)
// 테스트 4 〉	통과 (0.43ms, 29.9MB)
// 테스트 5 〉	통과 (0.97ms, 30.1MB)
// 테스트 6 〉	통과 (1.87ms, 30.4MB)
// 테스트 7 〉	통과 (18.41ms, 34.7MB)
// 테스트 8 〉	통과 (40.27ms, 34.8MB)
// 테스트 9 〉	통과 (30.33ms, 35MB)
// 테스트 10 〉	통과 (41.32ms, 35.8MB)
// 테스트 11 〉	통과 (55.41ms, 36MB)
// 테스트 12 〉	통과 (108.41ms, 36.7MB)
// 테스트 13 〉	통과 (112.00ms, 36.5MB)
// 테스트 14 〉	통과 (135.51ms, 36.6MB)
// 테스트 15 〉	통과 (0.14ms, 29.8MB)

//한 번의 순회로 끝내기
function isDigit(string) {
  return !Number.isNaN(Number(string))
}

function solution(s) {
  const dict = {}
  let number = ''
  Array.from(s).forEach((char) => {
    if (isDigit(char)) number += char

    if (number.length > 0 && (char === '}' || char === ',')) {
      if (!dict[number]) {
        dict[number] = 0
      }
      dict[number]++
      number = ''
    }
  })

  const result = Object.entries(dict)
    .sort((a, b) => b[1] - a[1])
    .map((x) => Number(x[0]))
  return result
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.21ms, 30.1MB)
// 테스트 2 〉	통과 (0.16ms, 29.9MB)
// 테스트 3 〉	통과 (0.29ms, 30.1MB)
// 테스트 4 〉	통과 (0.39ms, 30.3MB)
// 테스트 5 〉	통과 (0.63ms, 29.9MB)
// 테스트 6 〉	통과 (1.28ms, 30.4MB)
// 테스트 7 〉	통과 (14.19ms, 33.7MB)
// 테스트 8 〉	통과 (25.21ms, 37.1MB)
// 테스트 9 〉	통과 (20.58ms, 34.7MB)
// 테스트 10 〉	통과 (26.63ms, 37.1MB)
// 테스트 11 〉	통과 (37.20ms, 39.2MB)
// 테스트 12 〉	통과 (104.45ms, 45.6MB)
// 테스트 13 〉	통과 (85.18ms, 45.6MB)
// 테스트 14 〉	통과 (84.79ms, 45.5MB)
// 테스트 15 〉	통과 (0.11ms, 30.1MB)
