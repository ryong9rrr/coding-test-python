const isDiffOne = (a, b) => {
  let flag = false
  for (let i = 0; i < a.length; i += 1) {
    if (a[i] !== b[i]) {
      if (flag) {
        return false
      }
      flag = true
    }
  }
  return true
}

function solution(begin, target, words) {
  if (!words.includes(target)) {
    return 0
  }

  const INF = Infinity
  let result = INF

  const dfs = (cur, visited, count) => {
    if (cur === target) {
      result = Math.min(result, count)
      return
    }

    for (const word of words) {
      if (!visited[word] && isDiffOne(cur, word)) {
        dfs(word, { ...visited, [word]: true }, count + 1)
      }
    }
  }

  const visited = {}
  visited[begin] = true

  dfs(begin, visited, 0)
  return result === INF ? 0 : result
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.12ms, 33.5MB)
// 테스트 2 〉	통과 (0.28ms, 33.6MB)
// 테스트 3 〉	통과 (0.42ms, 33.6MB)
// 테스트 4 〉	통과 (0.20ms, 33.4MB)
// 테스트 5 〉	통과 (0.05ms, 33.5MB)
