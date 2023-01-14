// 데크가 아니라 큐만 사용한다면 거꾸로 스택으로 푸는 것도 가능.
function solution(tickets) {
  const graph = tickets
    .sort()
    .reverse()
    .reduce((obj, [v, w]) => {
      if (!obj[v]) obj[v] = []
      obj[v].push(w)
      return obj
    }, {})

  const result = []

  const dfs = (node) => {
    while (graph[node] && graph[node].length > 0) {
      dfs(graph[node].pop())
    }
    result.push(node)
  }

  dfs("ICN")

  return result.reverse()
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.26ms, 33.5MB)
// 테스트 2 〉	통과 (0.14ms, 33.7MB)
// 테스트 3 〉	통과 (0.10ms, 33.6MB)
// 테스트 4 〉	통과 (0.11ms, 33.5MB)
