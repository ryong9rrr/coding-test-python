// 자바스크립트 - shift()를 사용했을 때
function solution(progresses, speeds) {
  const q = []
  for (let i = 0; i < speeds.length; i++) {
    q.push(Math.ceil((100 - progresses[i]) / speeds[i]))
  }
  let prev = q.shift()
  let result = [1]
  while (q.length > 0) {
    const x = q.shift()
    if (prev >= x) {
      result[result.length - 1]++
    } else {
      result.push(1)
      prev = x
    }
  }
  return result
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.06ms, 30MB)
// 테스트 2 〉	통과 (0.13ms, 30.3MB)
// 테스트 3 〉	통과 (0.09ms, 30.3MB)
// 테스트 4 〉	통과 (0.09ms, 30.4MB)
// 테스트 5 〉	통과 (0.09ms, 30.2MB)
// 테스트 6 〉	통과 (0.10ms, 30.4MB)
// 테스트 7 〉	통과 (0.16ms, 30.3MB)
// 테스트 8 〉	통과 (0.10ms, 30.2MB)
// 테스트 9 〉	통과 (0.09ms, 30.3MB)
// 테스트 10 〉	통과 (0.10ms, 30.2MB)
// 테스트 11 〉	통과 (0.08ms, 30.3MB)

// 큐를 뒤집어서 스택처럼 사용했을 때
function solution(progresses, speeds) {
  const q = []
  for (let i = 0; i < speeds.length; i++) {
    q.push(Math.ceil((100 - progresses[i]) / speeds[i]))
  }
  q.reverse() // shift 연산을 사용하지 않기 위해
  let prev = q.pop()
  let result = [1]
  while (q.length > 0) {
    const x = q.pop()
    if (prev >= x) {
      result[result.length - 1]++
    } else {
      result.push(1)
      prev = x
    }
  }
  return result
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.07ms, 30.1MB)
// 테스트 2 〉	통과 (0.11ms, 30.3MB)
// 테스트 3 〉	통과 (0.11ms, 30.4MB)
// 테스트 4 〉	통과 (0.12ms, 30.4MB)
// 테스트 5 〉	통과 (0.09ms, 30.2MB)
// 테스트 6 〉	통과 (0.07ms, 30.2MB)
// 테스트 7 〉	통과 (0.10ms, 30MB)
// 테스트 8 〉	통과 (0.09ms, 30.3MB)
// 테스트 9 〉	통과 (0.08ms, 30.5MB)
// 테스트 10 〉	통과 (0.09ms, 30.3MB)
// 테스트 11 〉	통과 (0.06ms, 30.1MB)
