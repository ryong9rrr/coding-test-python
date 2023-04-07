> related topics : DFS, BFS, 2차원 배열

섬의 개수를 찾는 문제와 거의 동일한 문제.

0으로 둘러싸인 1의 개수 => 가장자리에 도달할 수 없는 1 => 가장자리부터 탐색하자

## 접근 1 : DFS

#### python

```python
# 721ms(51%), 81MB(36%)
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        def is_rand(x, y):
            return grid[x][y] == 1

        def is_side(x, y):
            return x == 0 or y == 0 or x == n - 1 or y == m - 1

        def valid_range(x, y):
            return 0 <= x < n and 0 <= y < m

        def dfs(x, y):
            grid[x][y] = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if valid_range(nx, ny) and is_rand(nx, ny):
                    grid[nx][ny] = 0
                    dfs(nx, ny)

        # 가장자리부터 dfs
        for i in range(n):
            for j in range(m):
                if is_rand(i, j) and is_side(i, j):
                    dfs(i, j)

        # 도달하지 못한 1 개수 세기
        ans = 0
        for i in range(n):
            for j in range(m):
                if is_rand(i, j):
                    ans += 1

        return ans
```

#### javascript

```js
// 102ms(64%), 55MB(57%)
/**
 * @param {number[][]} grid
 * @return {number}
 */
var numEnclaves = function (grid) {
  const n = grid.length
  const m = grid[0].length

  const dx = [0, 1, 0, -1]
  const dy = [1, 0, -1, 0]

  const isRand = (x, y) => {
    return grid[x][y] === 1
  }

  const isSide = (x, y) => {
    return x === 0 || y === 0 || x === n - 1 || y === m - 1
  }

  const validRange = (x, y) => {
    return 0 <= x && x < n && 0 <= y && y < m
  }

  const dfs = (x, y) => {
    grid[x][y] = 0
    for (let i = 0; i < 4; i += 1) {
      const nx = x + dx[i]
      const ny = y + dy[i]
      if (validRange(nx, ny) && isRand(nx, ny)) {
        grid[nx][ny] = 0
        dfs(nx, ny)
      }
    }
  }

  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < m; j += 1) {
      if (isRand(i, j) && isSide(i, j)) {
        dfs(i, j)
      }
    }
  }

  let ans = 0
  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < m; j += 1) {
      if (isRand(i, j)) {
        ans += 1
      }
    }
  }
  return ans
}
```

## 접근 2 : BFS

#### python

```python
# 737ms(47%), 15.5MB(94%)
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        def is_rand(x, y):
            return grid[x][y] == 1

        def is_side(x, y):
            return x == 0 or y == 0 or x == n - 1 or y == m - 1

        def valid_range(x, y):
            return 0 <= x < n and 0 <= y < m

        q = collections.deque()
        def bfs(r, c):
            q.append([r, c])
            grid[r][c] = 0
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if valid_range(nx, ny) and is_rand(nx, ny):
                        q.append([nx, ny])
                        grid[nx][ny] = 0

        # 가장자리부터 bfs
        for i in range(n):
            for j in range(m):
                if is_rand(i, j) and is_side(i, j):
                    bfs(i, j)

        # 도달하지 못한 1 개수 세기
        ans = 0
        for i in range(n):
            for j in range(m):
                if is_rand(i, j):
                    ans += 1

        return ans
```

#### javascript

```js
// 98ms(77%), 51MB(81%)
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
 * @param {number[][]} grid
 * @return {number}
 */
var numEnclaves = function (grid) {
  const n = grid.length
  const m = grid[0].length

  const dx = [0, 1, 0, -1]
  const dy = [1, 0, -1, 0]

  const isRand = (x, y) => {
    return grid[x][y] === 1
  }

  const isSide = (x, y) => {
    return x === 0 || y === 0 || x === n - 1 || y === m - 1
  }

  const validRange = (x, y) => {
    return 0 <= x && x < n && 0 <= y && y < m
  }

  const q = new MyQueue()
  const bfs = (r, c) => {
    q.enqueue([r, c])
    grid[r][c] = 0
    while (q.size > 0) {
      const [x, y] = q.dequeue()
      for (let i = 0; i < 4; i += 1) {
        const nx = x + dx[i]
        const ny = y + dy[i]
        if (validRange(nx, ny) && isRand(nx, ny)) {
          grid[nx][ny] = 0
          q.enqueue([nx, ny])
        }
      }
    }
  }

  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < m; j += 1) {
      if (isRand(i, j) && isSide(i, j)) {
        bfs(i, j)
      }
    }
  }

  let ans = 0
  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < m; j += 1) {
      if (isRand(i, j)) {
        ans += 1
      }
    }
  }
  return ans
}
```
