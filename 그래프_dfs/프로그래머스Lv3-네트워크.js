// 인접리스트 + 재귀
function solution(n, computers) {
  const graph = {}
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      if (computers[i][j] === 1) {
        if (!graph[i + 1]) graph[i + 1] = []
        if (!graph[j + 1]) graph[j + 1] = []
        graph[i + 1].push(j + 1)
        graph[j + 1].push(i + 1)
      }
    }
  }

  let count = 0
  const visited = Array.from({ length: n + 1 }, (v, i) => false)

  const dfs = (v) => {
    if (visited[v]) {
      return 0
    }
    visited[v] = true
    if (graph[v]) {
      for (const w of graph[v]) {
        if (!visited[w]) {
          dfs(w)
        }
      }
    }
    return 1
  }

  for (let v = 1; v < n + 1; v++) {
    if (!visited[v]) {
      count += dfs(v)
    }
  }

  return count
}
// 정확성  테스트
// 테스트 1 〉	통과 (5.61ms, 33.7MB)
// 테스트 2 〉	통과 (5.09ms, 33.6MB)
// 테스트 3 〉	통과 (6.13ms, 33.7MB)
// 테스트 4 〉	통과 (6.15ms, 33.8MB)
// 테스트 5 〉	통과 (4.00ms, 33.7MB)
// 테스트 6 〉	통과 (5.30ms, 33.9MB)
// 테스트 7 〉	통과 (5.07ms, 33.7MB)
// 테스트 8 〉	통과 (6.36ms, 33.8MB)
// 테스트 9 〉	통과 (5.47ms, 33.7MB)
// 테스트 10 〉	통과 (4.97ms, 33.7MB)
// 테스트 11 〉	통과 (5.34ms, 34.3MB)
// 테스트 12 〉	통과 (6.04ms, 34.2MB)
// 테스트 13 〉	통과 (5.00ms, 33.8MB)

// 인접행렬 + 재귀
function solution(n, computers) {
  let count = 0
  const visited = Array.from({ length: n }, (v, i) => false)

  const dfs = (v) => {
    if (visited[v]) {
      return 0
    }
    visited[v] = true
    for (let w = 0; w < n; w++) {
      if (v === w || visited[w]) {
        continue
      }
      if (computers[v][w] === 1) {
        dfs(w)
      }
    }
    return 1
  }

  for (let v = 0; v < n; v++) {
    if (!visited[v]) {
      count += dfs(v)
    }
  }

  return count
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.17ms, 33.6MB)
// 테스트 2 〉	통과 (0.23ms, 33.4MB)
// 테스트 3 〉	통과 (0.27ms, 33.5MB)
// 테스트 4 〉	통과 (0.28ms, 33.5MB)
// 테스트 5 〉	통과 (0.21ms, 33.6MB)
// 테스트 6 〉	통과 (0.25ms, 33.5MB)
// 테스트 7 〉	통과 (0.24ms, 33.6MB)
// 테스트 8 〉	통과 (0.33ms, 33.5MB)
// 테스트 9 〉	통과 (0.34ms, 33.4MB)
// 테스트 10 〉	통과 (0.33ms, 33.6MB)
// 테스트 11 〉	통과 (0.66ms, 33.8MB)
// 테스트 12 〉	통과 (0.40ms, 33.8MB)
// 테스트 13 〉	통과 (0.42ms, 33.7MB)

// 인접행렬 + 스택
function solution(n, computers) {
  let count = 0
  const visited = Array.from({ length: n }, (v, i) => false)

  const dfs = (node) => {
    const stack = [node]
    while (stack.length > 0) {
      const v = stack.pop()
      visited[v] = true
      for (let w = 0; w < n; w++) {
        if (v === w || visited[w]) {
          continue
        }
        if (computers[v][w] === 1) {
          // dfs(w)만 하는 것도 됨.
          stack.push(w)
        }
      }
    }
  }

  for (let v = 0; v < n; v++) {
    if (!visited[v]) {
      dfs(v)
      count++
    }
  }

  return count
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.20ms, 33.7MB)
// 테스트 2 〉	통과 (0.20ms, 33.5MB)
// 테스트 3 〉	통과 (0.22ms, 33.7MB)
// 테스트 4 〉	통과 (0.23ms, 33.5MB)
// 테스트 5 〉	통과 (0.11ms, 33.6MB)
// 테스트 6 〉	통과 (0.58ms, 33.5MB)
// 테스트 7 〉	통과 (0.20ms, 33.7MB)
// 테스트 8 〉	통과 (0.29ms, 33.6MB)
// 테스트 9 〉	통과 (0.26ms, 33.6MB)
// 테스트 10 〉	통과 (0.26ms, 33.6MB)
// 테스트 11 〉	통과 (3.05ms, 36.9MB)
// 테스트 12 〉	통과 (3.01ms, 37MB)
// 테스트 13 〉	통과 (0.41ms, 33.7MB)
