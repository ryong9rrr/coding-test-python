function check(brackets) {
  const stack = []
  for (const s of [...brackets]) {
    if (s === ')') {
      if (stack.length > 0) stack.pop()
      else return false
    } else {
      stack.push(s)
    }
  }
  return true
}

function divide(brackets) {
  let count = 0
  for (let i = 0; i < brackets.length; i++) {
    if (brackets[i] === '(') count++
    else count--
    if (count === 0) return i
  }
  return brackets.length - 1
}

function rev(brackets) {
  let result = ''
  for (const s of [...brackets]) {
    if (s === '(') result += ')'
    else result += '('
  }
  return result
}

function solution(p) {
  if (!p || check(p)) return p

  const index = divide(p)
  const u = p.slice(0, index + 1)
  const v = p.slice(index + 1)

  if (check(u)) return u + solution(v)

  let temp = '('
  temp += solution(v)
  temp += ')'

  return temp + rev(u.slice(1, -1))
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.08ms, 33.4MB)
// 테스트 2 〉	통과 (0.11ms, 33.4MB)
// 테스트 3 〉	통과 (0.07ms, 33.4MB)
// 테스트 4 〉	통과 (0.12ms, 33.4MB)
// 테스트 5 〉	통과 (0.10ms, 33.4MB)
// 테스트 6 〉	통과 (0.20ms, 33.3MB)
// 테스트 7 〉	통과 (0.12ms, 33.4MB)
// 테스트 8 〉	통과 (0.08ms, 33.5MB)
// 테스트 9 〉	통과 (0.12ms, 33.4MB)
// 테스트 10 〉	통과 (0.23ms, 33.4MB)
// 테스트 11 〉	통과 (0.25ms, 33.5MB)
// 테스트 12 〉	통과 (0.27ms, 33.4MB)
// 테스트 13 〉	통과 (0.27ms, 33.4MB)
// 테스트 14 〉	통과 (0.32ms, 33.4MB)
// 테스트 15 〉	통과 (0.37ms, 33.4MB)
// 테스트 16 〉	통과 (0.52ms, 33.7MB)
// 테스트 17 〉	통과 (0.48ms, 33.6MB)
// 테스트 18 〉	통과 (0.76ms, 33.6MB)
// 테스트 19 〉	통과 (0.95ms, 33.9MB)
// 테스트 20 〉	통과 (0.88ms, 33.8MB)
// 테스트 21 〉	통과 (0.61ms, 33.6MB)
// 테스트 22 〉	통과 (0.41ms, 33.5MB)
// 테스트 23 〉	통과 (0.74ms, 33.6MB)
// 테스트 24 〉	통과 (0.31ms, 33.6MB)
// 테스트 25 〉	통과 (0.59ms, 33.7MB)
