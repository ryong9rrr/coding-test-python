> related topics : DFS, BFS

## 접근 1 : DFS (1)

파이썬 알고리즘 인터뷰 풀이

#### python

```python
# 동서남북으로 탐색 // 264ms
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])

        def dfs(i, j):
            # 범위를 벗어나거나 섬이 아니면
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != "1":
                return
            # 마킹처리
            grid[i][j] = "0"
            # 동서남북으로 탐색
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    # 한 사이클이 끝났다면 섬을 하나 찾은 것
                    count += 1

        return count
```

#### javascript

```js
// 98ms, 45.5MB
/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
  const N = grid.length
  const M = grid[0].length

  const isVisited = (i, j) => grid[i][j] !== "1"
  const validateRange = (i, j) => 0 <= i && i < N && 0 <= j && j < M

  const dfs = (i, j) => {
    if (!validateRange(i, j) || isVisited(i, j)) {
      return
    }
    grid[i][j] = "#"
    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)
  }

  let count = 0
  for (let i = 0; i < N; i += 1) {
    for (let j = 0; j < M; j += 1) {
      if (!isVisited(i, j)) {
        dfs(i, j)
        count += 1
      }
    }
  }
  return count
}
```

## 접근 2 : DFS (2)

나의 DFS

#### python

```python
# 309ms(56%), 16MB(42%)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        def valid_range(nx, ny):
            return 0 <= nx < n and 0 <= ny < m

        def dfs(x, y):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if valid_range(nx, ny) and grid[nx][ny] == "1":
                    grid[nx][ny] = "0"
                    dfs(nx, ny)

        count = 0
        for x in range(n):
            for y in range(m):
                if grid[x][y] == "1":
                    grid[x][y] = "0"
                    dfs(x, y)
                    count += 1
        return count
```

#### javascript

```js
// 77ms(80%), 45.5MB(50%)
/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
  const n = grid.length
  const m = grid[0].length

  const dx = [0, 1, 0, -1]
  const dy = [1, 0, -1, 0]

  const validRange = (x, y) => {
    return 0 <= x && x < n && 0 <= y && y < m
  }

  const dfs = (x, y) => {
    for (let i = 0; i < 4; i += 1) {
      const nx = x + dx[i]
      const ny = y + dy[i]
      if (validRange(nx, ny) && grid[nx][ny] === "1") {
        grid[nx][ny] = "0"
        dfs(nx, ny)
      }
    }
  }

  let count = 0
  for (let x = 0; x < n; x += 1) {
    for (let y = 0; y < m; y += 1) {
      if (grid[x][y] === "1") {
        grid[x][y] = "0"
        dfs(x, y)
        count += 1
      }
    }
  }
  return count
}
```

## 접근 3 : BFS

나의 BFS

#### python

```python
# 309ms(56%), 16MB(90%)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        def valid_range(nx, ny):
            return 0 <= nx < n and 0 <= ny < m

        q = collections.deque()
        def bfs(r, c):
            grid[r][c] = "0"
            q.append([r, c])
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if valid_range(nx, ny) and grid[nx][ny] == "1":
                        grid[nx][ny] = "0"
                        q.append([nx, ny])


        count = 0
        for x in range(n):
            for y in range(m):
                if grid[x][y] == "1":
                    bfs(x, y)
                    count += 1
        return count
```

#### javascript

```js
class MyNode {
  constructor(value) {
    this.value = value
    this.next = null
  }
}

class MyQueue {
  constructor(array = []) {
    this.front = this.tail = null
    this.size = 0

    for (const el of array) {
      this.enqueue(el)
    }
  }

  get peek() {
    return !this.front || !this.tail ? undefined : this.front.value
  }

  enqueue(value) {
    const node = new MyNode(value)
    if (!this.front) {
      this.front = this.tail = node
    } else {
      this.tail = this.tail.next = node
    }
    this.size += 1
  }

  dequeue() {
    if (!this.front) {
      return undefined
    }
    const result = this.front.value
    this.front = this.front.next
    this.size -= 1
    return result
  }
}

/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
  const n = grid.length
  const m = grid[0].length

  const dx = [0, 1, 0, -1]
  const dy = [1, 0, -1, 0]

  const validRange = (x, y) => {
    return 0 <= x && x < n && 0 <= y && y < m
  }

  const q = new MyQueue()
  const bfs = (r, c) => {
    grid[r][c] = "0"
    q.enqueue([r, c])

    while (q.size > 0) {
      const [x, y] = q.dequeue()
      for (let i = 0; i < 4; i += 1) {
        const nx = x + dx[i]
        const ny = y + dy[i]
        if (validRange(nx, ny) && grid[nx][ny] === "1") {
          grid[nx][ny] = "0"
          q.enqueue([nx, ny])
        }
      }
    }
  }

  let count = 0
  for (let x = 0; x < n; x += 1) {
    for (let y = 0; y < m; y += 1) {
      if (grid[x][y] === "1") {
        bfs(x, y)
        count += 1
      }
    }
  }
  return count
}
```
