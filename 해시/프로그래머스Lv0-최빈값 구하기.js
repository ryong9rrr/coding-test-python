function solution(array) {
  const counter = {}
  array.forEach(x => {
      if (!counter[x]) counter[x] = 0
      counter[x]++
  })
  
  const mostCommon = Object.entries(counter)
                      .sort((a, b) => b[1] - a[1])
                      .map(([key, value]) => [parseInt(key, 10), value])
  if (mostCommon.length === 1) {
      return mostCommon[0][0]
  }
  
  const [a, b] = mostCommon
  if (a[1] === b[1]) {
      return -1
  }
  return a[0]
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.19ms, 33.5MB)
// 테스트 2 〉	통과 (0.51ms, 32.7MB)
// 테스트 3 〉	통과 (0.29ms, 32.7MB)
// 테스트 4 〉	통과 (0.32ms, 33.1MB)
// 테스트 5 〉	통과 (0.15ms, 33.1MB)
// 테스트 6 〉	통과 (0.12ms, 33.5MB)
// 테스트 7 〉	통과 (0.21ms, 33.5MB)
// 테스트 8 〉	통과 (0.16ms, 33.2MB)
// 테스트 9 〉	통과 (0.11ms, 33.3MB)
// 테스트 10 〉	통과 (0.09ms, 33.4MB)
// 테스트 11 〉	통과 (0.21ms, 33.5MB)
// 테스트 12 〉	통과 (0.14ms, 33.4MB)
// 테스트 13 〉	통과 (0.14ms, 33.5MB)
// 테스트 14 〉	통과 (0.23ms, 33.4MB)
// 테스트 15 〉	통과 (0.23ms, 33.6MB)
// 테스트 16 〉	통과 (0.31ms, 33.5MB)