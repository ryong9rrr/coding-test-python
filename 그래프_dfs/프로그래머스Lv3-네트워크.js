function solution(n, computers) {
  const visited = new Array(n).fill(false)

  const dfs = (v) => {
    visited[v] = true
    for (let w = 0; w < n; w += 1) {
      if (v !== w && !visited[w] && computers[v][w] === 1) {
        dfs(w)
      }
    }
  }

  let count = 0
  for (let v = 0; v < n; v += 1) {
    if (!visited[v]) {
      dfs(v)
      count += 1
    }
  }

  return count
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.16ms, 33.4MB)
// 테스트 2 〉	통과 (0.22ms, 33.4MB)
// 테스트 3 〉	통과 (0.17ms, 33.5MB)
// 테스트 4 〉	통과 (0.16ms, 33.5MB)
// 테스트 5 〉	통과 (0.11ms, 33.4MB)
// 테스트 6 〉	통과 (0.21ms, 33.5MB)
// 테스트 7 〉	통과 (0.17ms, 33.4MB)
// 테스트 8 〉	통과 (0.22ms, 33.5MB)
// 테스트 9 〉	통과 (0.18ms, 33.5MB)
// 테스트 10 〉	통과 (0.18ms, 33.5MB)
// 테스트 11 〉	통과 (0.38ms, 33.7MB)
// 테스트 12 〉	통과 (0.36ms, 33.7MB)
// 테스트 13 〉	통과 (0.25ms, 33.5MB)
