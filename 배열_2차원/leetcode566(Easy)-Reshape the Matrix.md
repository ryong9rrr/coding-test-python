# 접근 1 : 나의 풀이

가장 직관적인 방법이 아닐까..

- 시간복잡도 : O(N^2)
- 공간복잡도 : O(N^2)

```python
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])

        if n * m != r * c:
            return mat

        ans = []
        row = []
        for i in range(n):
            for j in range(m):
                row.append(mat[i][j])
                if len(row) == c:
                    ans.append(row)
                    row = []

        return ans
```

# 접근 2 : 수학적인 접근, O(N)

인덱스를 이용해서 1번의 루프로 끝내기.. 어떻게 이런 생각을...?

- 시간복잡도 : O(N)
- 공간복잡도 : O(N^2)

```python
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])

        if n * m != r * c:
            return mat

        ans = [[0] * c for _ in range(r)]
        for i in range(r * c):
            ans[i // c][i % c] = mat[i // m][i % m]

        return ans
```

```js
/**
 * @param {number[][]} mat
 * @param {number} r
 * @param {number} c
 * @return {number[][]}
 */
var matrixReshape = function (mat, r, c) {
  const n = mat.length
  const m = mat[0].length

  if (n * m !== r * c) {
    return mat
  }

  const ans = Array.from({ length: r }, () => new Array(c).fill(0))
  for (let i = 0; i < r * c; i += 1) {
    ans[Math.floor(i / c)][i % c] = mat[Math.floor(i / m)][i % m]
  }
  return ans
}
```
