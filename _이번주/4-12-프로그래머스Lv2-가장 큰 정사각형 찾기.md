> related topics : DP

# 접근 1 : 브루트포스 (시간초과)

내가 처음 푼 풀이로, size를 1부터 가능한 만큼 늘리면서 가장 큰 사이즈의 정사각형을 찾는 방법... 하지만 시간초과.

#### python

```python
def solution(board):
    n = len(board)
    m = len(board[0])

    def possible(x, y, size):
        for i in range(x, x + size):
            for j in range(y, y + size):
                if board[i][j] == 0:
                    return False
        return True

    ans = 0
    for size in range(1, min(n, m) + 1):
        for i in range(n - size + 1):
            for j in range(m - size + 1):
                if not possible(i, j, size):
                    continue
                ans = max(ans, size ** 2)

    return ans
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.51ms, 10.2MB)
테스트 3 〉	통과 (0.59ms, 10.2MB)
테스트 4 〉	통과 (0.78ms, 10.2MB)
테스트 5 〉	통과 (1.04ms, 9.99MB)
테스트 6 〉	통과 (0.07ms, 9.98MB)
테스트 7 〉	통과 (0.08ms, 10.1MB)
테스트 8 〉	통과 (0.45ms, 10.1MB)
테스트 9 〉	통과 (0.12ms, 10.1MB)
테스트 10 〉	통과 (0.52ms, 10.1MB)
테스트 11 〉	통과 (0.09ms, 10.1MB)
테스트 12 〉	통과 (0.31ms, 10.2MB)
테스트 13 〉	통과 (0.06ms, 10.3MB)
테스트 14 〉	통과 (0.32ms, 10.2MB)
테스트 15 〉	통과 (0.31ms, 10.2MB)
테스트 16 〉	통과 (0.99ms, 10MB)
테스트 17 〉	통과 (0.63ms, 10.2MB)
테스트 18 〉	통과 (679.45ms, 10.1MB)
테스트 19 〉	통과 (400.75ms, 10MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
"""
```

# 접근 2 : DP

**행렬 최단거리 경우의 수** 문제와 비슷한 문제로,

1. 첫행, 첫열은 처음 행렬대로 갱신한 후에,
2. (1, 1) 부터 (n - 1, m - 1) 까지 DP 테이블을 갱신하는 식으로 풀이한다.

#### python

```python
def solution(board):
    n = len(board)
    m = len(board[0])

    dp = [[0] * m for _ in range(n)]

    # 첫 행과 첫 열은 그대로 채운다.
    for i in range(n):
        dp[i][0] = board[i][0]

    for j in range(m):
        dp[0][j] = board[0][j]

    max_value = 0 # (dp테이블을 다 구해놓고 최댓값을 찾아도 되지만) 최댓값도 같이 갱신
    for i in range(n):
        for j in range(m):
            # (1, 1) 부터 (n - 1, m - 1)까지 dp 테이블 갱신
            if board[i][j] == 1 and i > 0 and j > 0:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            max_value = max(max_value, dp[i][j])

    return max_value ** 2
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (0.05ms, 10.2MB)
테스트 4 〉	통과 (0.06ms, 10.1MB)
테스트 5 〉	통과 (0.06ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.05ms, 10.3MB)
테스트 10 〉	통과 (0.10ms, 10.1MB)
테스트 11 〉	통과 (0.03ms, 10.2MB)
테스트 12 〉	통과 (0.04ms, 10.1MB)
테스트 13 〉	통과 (0.03ms, 10.2MB)
테스트 14 〉	통과 (0.09ms, 10.2MB)
테스트 15 〉	통과 (0.06ms, 10.2MB)
테스트 16 〉	통과 (0.06ms, 10.3MB)
테스트 17 〉	통과 (0.12ms, 10.2MB)
테스트 18 〉	통과 (1.45ms, 10.2MB)
테스트 19 〉	통과 (2.19ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (568.78ms, 38.8MB)
테스트 2 〉	통과 (552.77ms, 38.5MB)
테스트 3 〉	통과 (588.09ms, 38.6MB)
"""
```

#### js

```js
function solution(board) {
  const n = board.length
  const m = board[0].length

  const dp = Array.from({ length: n }, () => new Array(m).fill(0))

  // 첫 행과 첫 열은 그대로 채운다.
  for (let i = 0; i < n; i += 1) {
    dp[i][0] = board[i][0]
  }

  for (let j = 0; j < m; j += 1) {
    dp[0][j] = board[0][j]
  }

  // dp 갱신
  let maxValue = 0
  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < m; j += 1) {
      if (i > 0 && j > 0 && board[i][j] === 1) {
        dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
      }
      maxValue = Math.max(maxValue, dp[i][j])
    }
  }
  return maxValue ** 2
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.12ms, 33.5MB)
// 테스트 2 〉	통과 (0.32ms, 33.6MB)
// 테스트 3 〉	통과 (0.32ms, 33.5MB)
// 테스트 4 〉	통과 (0.34ms, 33.5MB)
// 테스트 5 〉	통과 (0.23ms, 33.6MB)
// 테스트 6 〉	통과 (0.22ms, 33.5MB)
// 테스트 7 〉	통과 (0.26ms, 33.5MB)
// 테스트 8 〉	통과 (0.22ms, 33.6MB)
// 테스트 9 〉	통과 (0.30ms, 33.5MB)
// 테스트 10 〉	통과 (0.24ms, 33.5MB)
// 테스트 11 〉	통과 (0.28ms, 33.4MB)
// 테스트 12 〉	통과 (0.36ms, 33.5MB)
// 테스트 13 〉	통과 (0.40ms, 33.6MB)
// 테스트 14 〉	통과 (0.24ms, 33.5MB)
// 테스트 15 〉	통과 (0.22ms, 33.4MB)
// 테스트 16 〉	통과 (0.34ms, 33.5MB)
// 테스트 17 〉	통과 (0.27ms, 33.5MB)
// 테스트 18 〉	통과 (0.67ms, 33.4MB)
// 테스트 19 〉	통과 (0.68ms, 33.5MB)
// 효율성  테스트
// 테스트 1 〉	통과 (27.55ms, 82.3MB)
// 테스트 2 〉	통과 (28.34ms, 82.5MB)
// 테스트 3 〉	통과 (28.68ms, 82.2MB)
```
