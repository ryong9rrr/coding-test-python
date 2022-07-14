function solution(priorities, location) {
  const q = priorities.map((prior, loc) => [loc, prior])
  const revPrior = [...priorities].sort().reverse()
  let count = 0
  while (q.length > 0) {
    const [loc, prior] = q.shift()
    const max = revPrior[count]
    if (loc === location && max === prior) return count + 1
    if (max === prior) count++
    else q.push([loc, prior])
  }
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.19ms, 30.1MB)
// 테스트 2 〉	통과 (0.28ms, 30.3MB)
// 테스트 3 〉	통과 (0.16ms, 30.3MB)
// 테스트 4 〉	통과 (0.12ms, 30.1MB)
// 테스트 5 〉	통과 (0.11ms, 30.2MB)
// 테스트 6 〉	통과 (0.16ms, 30MB)
// 테스트 7 〉	통과 (0.16ms, 30.4MB)
// 테스트 8 〉	통과 (0.22ms, 30.1MB)
// 테스트 9 〉	통과 (0.13ms, 29.8MB)
// 테스트 10 〉	통과 (0.17ms, 30.1MB)
// 테스트 11 〉	통과 (0.21ms, 29.9MB)
// 테스트 12 〉	통과 (0.15ms, 30.2MB)
// 테스트 13 〉	통과 (0.25ms, 30MB)
// 테스트 14 〉	통과 (0.10ms, 30.2MB)
// 테스트 15 〉	통과 (0.12ms, 30.1MB)
// 테스트 16 〉	통과 (0.12ms, 30MB)
// 테스트 17 〉	통과 (0.23ms, 30.1MB)
// 테스트 18 〉	통과 (0.14ms, 30.1MB)
// 테스트 19 〉	통과 (0.20ms, 30.3MB)
// 테스트 20 〉	통과 (0.15ms, 30.2MB)
