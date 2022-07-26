// 크기가 동일한 n x m 행렬 더하기
const sumMatrix = (arr1, arr2) => {
  const n = arr1.length
  const m = arr1[0].length

  const result = []
  for (let i = 0; i < n; i++) {
    const temp = []
    for (let j = 0; j < m; j++) {
      const x = arr1[i][j]
      const y = arr2[i][j]
      temp.push(x + y)
    }
    result.push(temp)
  }
  return result
}
