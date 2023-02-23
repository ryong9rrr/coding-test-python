// 자바스크립트에서 shift 연산은 O(N)이기 때문에 테스트케이스 1개가 시간초과가 떴음.
// 그러면 큐를 스택처럼 사용하기 위해 처음에 한번 뒤집고 마지막에 한번 더 뒤집으면 된다.
function solution(number, k) {
  const q = number.split('')
  q.reverse()
  const stack = []

  while (q.length > 0 && k) {
    while (stack.length > 0 && stack[stack.length - 1] < q[q.length - 1]) {
      stack.pop()
      k--
      if (!k) break
    }
    stack.push(q.pop())
  }

  while (k && stack.length > 0) {
    stack.pop()
    k--
  }

  q.reverse()

  return [...stack, ...q].join('')
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.12ms, 30.4MB)
// 테스트 2 〉	통과 (0.09ms, 30.5MB)
// 테스트 3 〉	통과 (0.10ms, 30.4MB)
// 테스트 4 〉	통과 (0.17ms, 30.4MB)
// 테스트 5 〉	통과 (0.21ms, 30.4MB)
// 테스트 6 〉	통과 (3.94ms, 33.2MB)
// 테스트 7 〉	통과 (8.88ms, 35.6MB)
// 테스트 8 〉	통과 (11.51ms, 37.1MB)
// 테스트 9 〉	통과 (30.76ms, 54.8MB)
// 테스트 10 〉	통과 (42.66ms, 52.4MB)
// 테스트 11 〉	통과 (0.06ms, 30.4MB)
// 테스트 12 〉	통과 (0.07ms, 30.2MB)
