// 옛날 풀이... 코테에서는 억지로 Array.prototype 메서드를 사용한 것 같음. 네이밍도 별로다. 풀이 로직도 별로다.
function solution(d, budget) {
  let lengD = d.length
  let sortD = d.sort((a, b) => a - b)
  let sumD = d.reduce((a, b) => a + b)

  if (sumD <= budget) {
    return lengD
  } else {
    let sum = 0
    let i = 0
    while (sum <= budget) {
      sum += sortD[i]
      i++
    }
    return i - 1
  }
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.06ms, 29.9MB)
// 테스트 2 〉	통과 (0.07ms, 29.8MB)
// 테스트 3 〉	통과 (0.07ms, 30.1MB)
// 테스트 4 〉	통과 (0.09ms, 30.1MB)
// 테스트 5 〉	통과 (0.09ms, 30MB)
// 테스트 6 〉	통과 (0.08ms, 29.9MB)
// 테스트 7 〉	통과 (0.10ms, 30.3MB)
// 테스트 8 〉	통과 (0.09ms, 29.9MB)
// 테스트 9 〉	통과 (0.11ms, 30MB)
// 테스트 10 〉	통과 (0.09ms, 30MB)
// 테스트 11 〉	통과 (0.13ms, 30MB)
// 테스트 12 〉	통과 (0.13ms, 30.2MB)
// 테스트 13 〉	통과 (0.13ms, 30MB)
// 테스트 14 〉	통과 (0.09ms, 30MB)
// 테스트 15 〉	통과 (0.13ms, 29.9MB)
// 테스트 16 〉	통과 (0.14ms, 29.8MB)
// 테스트 17 〉	통과 (0.13ms, 29.9MB)
// 테스트 18 〉	통과 (0.10ms, 30.1MB)
// 테스트 19 〉	통과 (0.10ms, 29.8MB)
// 테스트 20 〉	통과 (0.10ms, 29.9MB)
// 테스트 21 〉	통과 (0.11ms, 29.9MB)
// 테스트 22 〉	통과 (0.09ms, 29.8MB)
// 테스트 23 〉	통과 (0.10ms, 29.8MB)

// 22년 7월 풀이
const sorted = (array) => [...array].sort((a, b) => a - b)

function solution(d, budget) {
  let result = 0
  for (const money of sorted(d)) {
    if (budget < money) break
    budget -= money
    result += 1
  }
  return result
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.07ms, 30MB)
// 테스트 2 〉	통과 (0.09ms, 30.1MB)
// 테스트 3 〉	통과 (0.06ms, 30MB)
// 테스트 4 〉	통과 (0.08ms, 29.8MB)
// 테스트 5 〉	통과 (0.07ms, 29.9MB)
// 테스트 6 〉	통과 (0.10ms, 30.1MB)
// 테스트 7 〉	통과 (0.13ms, 29.8MB)
// 테스트 8 〉	통과 (0.09ms, 30MB)
// 테스트 9 〉	통과 (0.10ms, 30MB)
// 테스트 10 〉	통과 (0.11ms, 30.1MB)
// 테스트 11 〉	통과 (0.11ms, 30MB)
// 테스트 12 〉	통과 (0.09ms, 30MB)
// 테스트 13 〉	통과 (0.11ms, 30MB)
// 테스트 14 〉	통과 (0.11ms, 30.1MB)
// 테스트 15 〉	통과 (0.12ms, 30MB)
// 테스트 16 〉	통과 (0.10ms, 29.8MB)
// 테스트 17 〉	통과 (0.09ms, 29.8MB)
// 테스트 18 〉	통과 (0.09ms, 29.7MB)
// 테스트 19 〉	통과 (0.11ms, 30.1MB)
// 테스트 20 〉	통과 (0.08ms, 30.2MB)
// 테스트 21 〉	통과 (0.08ms, 30.1MB)
// 테스트 22 〉	통과 (0.11ms, 30MB)
// 테스트 23 〉	통과 (0.08ms, 29.8MB)
