function makeCombination(arr, k) {
  const n = arr.length
  const result = []

  const backtracking = (path = [], index = 0) => {
    if (path.length === k) {
      result.push([...path])
      return
    }

    for (let i = index; i < n; i += 1) {
      path.push(arr[i])
      backtracking(path, i + 1)
      path.pop()
    }
  }

  backtracking()
  return result
}
