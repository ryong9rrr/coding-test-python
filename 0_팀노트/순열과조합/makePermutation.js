// 백트래킹으로 순열을 구하는 함수 (n!)
function makePermutation(arr) {
  const n = arr.length
  const visited = new Array(n).fill(false)
  const result = []

  const backtracking = (path = []) => {
    if (path.length === n) {
      result.push([...path])
      return
    }

    for (let i = 0; i < n; i += 1) {
      if (!visited[i]) {
        visited[i] = true
        path.push(arr[i])

        backtracking(path)

        visited[i] = false
        path.pop()
      }
    }
  }

  backtracking()

  return result
}
