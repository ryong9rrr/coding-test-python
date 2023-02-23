function isdigit(s) {
  return !Number.isNaN(Number(s))
}

function oper(a, b, op) {
  const x = Number(a)
  const y = Number(b)
  const opers = {
    '+': () => x + y,
    '-': () => x - y,
    '*': () => x * y,
  }
  return opers[op]()
}

function permute(nums, k) {
  if (k > nums.length) return null
  const results = []
  prevElements = []
  function dfs(elements, k) {
    if (k === 0) {
      results.push([...prevElements])
      return
    }

    for (let i = 0; i < elements.length; i++) {
      nextElements = [...elements]
      nextElements.splice(i, 1)

      prevElements.push(elements[i])
      dfs(nextElements, k - 1)
      prevElements.pop()
    }
  }
  dfs(nums, k)
  return results
}

function makePrecs() {
  return permute(['*', '+', '-'], 3).map((prec) => {
    const [a, b, c] = prec
    return { [`${a}`]: 1, [`${b}`]: 2, [`${c}`]: 3 }
  })
}

function splitExpression(strings) {
  const arr = ['']
  for (const char of [...strings]) {
    // 연산자면
    if (!isdigit(char)) {
      arr.push(char)
      arr.push('')
      continue
    }
    arr[arr.length - 1] += char
  }
  return arr
}

function operate(array, prec) {
  const numbers = []
  const ops = []

  for (const char of array) {
    // 숫자면 푸시
    if (isdigit(char)) numbers.push(Number(char))
    else {
      if (ops.length === 0) ops.push(char)
      else {
        while (numbers.length > 0 && ops.length > 0 && prec[char] <= prec[ops[ops.length - 1]]) {
          const b = numbers.pop()
          const a = numbers.pop()
          numbers.push(oper(a, b, ops.pop()))
        }
        ops.push(char)
      }
    }
  }
  while (numbers.length > 0 && ops.length > 0) {
    const b = numbers.pop()
    const a = numbers.pop()
    numbers.push(oper(a, b, ops.pop()))
  }
  return numbers[0]
}

function solution(expression) {
  const exp_array = splitExpression(expression)

  let result = 0
  for (const prec of makePrecs()) {
    const answer = Math.abs(operate(exp_array, prec))
    result < answer ? (result = answer) : result
  }
  return result
}

/*
정확성  테스트
테스트 1 〉	통과 (0.65ms, 29.9MB)
테스트 2 〉	통과 (0.60ms, 29.8MB)
테스트 3 〉	통과 (0.57ms, 29.8MB)
테스트 4 〉	통과 (0.60ms, 30.1MB)
테스트 5 〉	통과 (0.65ms, 30.2MB)
테스트 6 〉	통과 (0.64ms, 30MB)
테스트 7 〉	통과 (0.68ms, 30MB)
테스트 8 〉	통과 (0.65ms, 30.2MB)
테스트 9 〉	통과 (0.66ms, 29.6MB)
테스트 10 〉	통과 (0.67ms, 30.2MB)
테스트 11 〉	통과 (0.93ms, 29.8MB)
테스트 12 〉	통과 (0.69ms, 30.1MB)
테스트 13 〉	통과 (0.70ms, 30.1MB)
테스트 14 〉	통과 (0.73ms, 30MB)
테스트 15 〉	통과 (0.77ms, 30.3MB)
테스트 16 〉	통과 (0.59ms, 30MB)
테스트 17 〉	통과 (0.65ms, 30MB)
테스트 18 〉	통과 (0.60ms, 30.1MB)
테스트 19 〉	통과 (0.59ms, 30.2MB)
테스트 20 〉	통과 (0.64ms, 30.3MB)
테스트 21 〉	통과 (0.86ms, 30.2MB)
테스트 22 〉	통과 (0.75ms, 30.1MB)
테스트 23 〉	통과 (0.65ms, 30.1MB)
테스트 24 〉	통과 (0.75ms, 30.3MB)
테스트 25 〉	통과 (0.79ms, 30MB)
테스트 26 〉	통과 (0.57ms, 29.7MB)
테스트 27 〉	통과 (0.81ms, 30.1MB)
테스트 28 〉	통과 (0.73ms, 29.9MB)
테스트 29 〉	통과 (0.78ms, 30.2MB)
테스트 30 〉	통과 (0.74ms, 29.9MB)
*/
