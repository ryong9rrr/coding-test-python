# 접근 1 : 행렬 축 간의 공식을 찾기

- 시간복잡도 : N x N 행렬일 때 O(N)
- 공간복잡도 : O(1)

## python

```python
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)

        ans = 0
        # primary diagonal
        for i in range(n):
            value = mat[i][i]
            mat[i][i] = 0
            ans += value

        # secondary diagonal
        for i in range(n):
            j = n - i - 1
            ans += mat[i][j]

        return ans
```

## js

한 번의 순회로 끝낼 수도 있음.

```js
/**
 * @param {number[][]} mat
 * @return {number}
 */
var diagonalSum = function (mat) {
  const n = mat.length

  let ans = 0
  for (let i = 0; i < n; i += 1) {
    ans += mat[i][i] // primary diagonal

    mat[i][i] = 0

    const j = n - i - 1
    ans += mat[i][j] // secondary diagonal
  }

  return ans
}
```
