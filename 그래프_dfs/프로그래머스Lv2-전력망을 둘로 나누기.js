// dfs
const dfs = (node, visited = [], graph) => {
  visited.push(node)
  if (graph[node].length === 0) {
    return visited.length
  }
  for (const v of graph[node]) {
    if (!visited.find((node) => node === v)) {
      dfs(v, visited, graph)
    }
  }
  return visited.length
}

function solution(n, wires) {
  const graph = {}
  for (const [v, w] of wires) {
    if (!graph[v]) {
      graph[v] = []
    }
    if (!graph[w]) {
      graph[w] = []
    }
    graph[v].push(w)
    graph[w].push(v)
  }

  let result = Infinity

  for (const [v, w] of wires) {
    graph[v] = graph[v].filter((node) => node !== w)
    graph[w] = graph[w].filter((node) => node !== v)

    const count = dfs(1, [], graph)

    result = Math.min(result, Math.abs(n - count * 2))

    graph[v].push(w)
    graph[w].push(v)
  }

  return result
}
// 정확성 테스트
// 테스트 1 〉 통과 (7.43ms, 32.6MB)
// 테스트 2 〉 통과 (6.80ms, 32.6MB)
// 테스트 3 〉 통과 (7.97ms, 32.4MB)
// 테스트 4 〉 통과 (6.97ms, 32.6MB)
// 테스트 5 〉 통과 (8.10ms, 32.5MB)
// 테스트 6 〉 통과 (0.21ms, 30.1MB)
// 테스트 7 〉 통과 (0.22ms, 30.3MB)
// 테스트 8 〉 통과 (0.47ms, 30.3MB)
// 테스트 9 〉 통과 (0.43ms, 30.2MB)
// 테스트 10 〉 통과 (6.91ms, 32.7MB)
// 테스트 11 〉 통과 (7.20ms, 32.6MB)
// 테스트 12 〉 통과 (7.04ms, 32.8MB)
// 테스트 13 〉 통과 (7.78ms, 32.3MB)

// 유니온파인드 (파이썬은 유니온파인드의 속도가 2배 더 빨랐지만... 자바스크립트는 재귀 성능이 안좋아서 그랬는지 더 느렸다.)
let uf = []

const find = (a) => {
  if (uf[a] < 0) {
    return a
  }

  uf[a] = find(uf[a])
  return uf[a]
}

const merge = (a, b) => {
  pa = find(a)
  pb = find(b)

  if (pa === pb) {
    return
  }

  uf[pa] += uf[pb]
  uf[pb] = pa
}

function solution(n, wires) {
  let result = Infinity
  const N = wires.length

  for (let node = 0; node < N; node++) {
    uf = Array.from({ length: n + 1 }, () => -1)
    const graph = wires.filter((wire, i) => i !== node)

    for (const [v, w] of graph) {
      merge(v, w)
    }

    const [a, b] = uf.slice(1).filter((v) => v < 0)
    result = Math.min(result, Math.abs(a - b))
  }

  return result
}
// 정확성 테스트
// 테스트 1 〉 통과 (27.70ms, 33.9MB)
// 테스트 2 〉 통과 (22.84ms, 34.1MB)
// 테스트 3 〉 통과 (24.77ms, 34MB)
// 테스트 4 〉 통과 (28.89ms, 33.8MB)
// 테스트 5 〉 통과 (7.89ms, 33.1MB)
// 테스트 6 〉 통과 (0.53ms, 29.8MB)
// 테스트 7 〉 통과 (0.38ms, 29.8MB)
// 테스트 8 〉 통과 (0.67ms, 30MB)
// 테스트 9 〉 통과 (0.97ms, 29.9MB)
// 테스트 10 〉 통과 (10.04ms, 33MB)
// 테스트 11 〉 통과 (11.48ms, 32.9MB)
// 테스트 12 〉 통과 (7.95ms, 32.8MB)
// 테스트 13 〉 통과 (6.63ms, 33MB)
