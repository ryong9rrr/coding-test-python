> related topics : DFS, BFS

섬의 개수를 반환하는 문제, 리트코드 200번 섬의 개수 문제와 비슷...

## 접근 1 : DFS

#### python

```python
# 142ms(28%), 14MB(61%)
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]

        def is_side(x, y):
            return x == 0 or y == 0 or x == n - 1 or y == m - 1

        def valid_range(nx, ny):
            return 0 <= nx < n and 0 <= ny < m

        def dfs(x, y):
            grid[x][y] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if valid_range(nx, ny) and grid[nx][ny] == 0:
                    grid[nx][ny] = 1
                    dfs(nx, ny)

        # 가장자리가 땅(1)이 아니라면 땅이라고 생각하고 땅으로 채운다.
        for x in range(n):
            for y in range(m):
                if is_side(x, y) and grid[x][y] == 0:
                    dfs(x, y)

        ans = 0
        for x in range(n):
            for y in range(m):
                if grid[x][y] == 0:
                    dfs(x, y)
                    ans += 1
        return ans
```

#### javascript

```js
// 80ms(44%), 45MB(47%)

/**
 * @param {number[][]} grid
 * @return {number}
 */
var closedIsland = function (grid) {
  const n = grid.length
  const m = grid[0].length

  const dx = [0, 1, 0, -1]
  const dy = [1, 0, -1, 0]

  const isSide = (x, y) => {
    return x === 0 || y === 0 || x === n - 1 || y === m - 1
  }

  const validRange = (nx, ny) => {
    return 0 <= nx && nx < n && 0 <= ny && ny < m
  }

  const dfs = (x, y) => {
    grid[x][y] = 1
    for (let i = 0; i < 4; i += 1) {
      const nx = x + dx[i]
      const ny = y + dy[i]
      if (validRange(nx, ny) && grid[nx][ny] === 0) {
        dfs(nx, ny)
      }
    }
  }

  for (let x = 0; x < n; x += 1) {
    for (let y = 0; y < m; y += 1) {
      if (isSide(x, y) && grid[x][y] === 0) {
        dfs(x, y)
      }
    }
  }

  let ans = 0
  for (let x = 0; x < n; x += 1) {
    for (let y = 0; y < m; y += 1) {
      if (grid[x][y] === 0) {
        dfs(x, y)
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
# 139ms(35%), 14.2MB(99%)
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]

        def is_side(x, y):
            return x == 0 or y == 0 or x == n - 1 or y == m - 1

        def valid_range(nx, ny):
            return 0 <= nx < n and 0 <= ny < m

        q = collections.deque()
        def bfs(r, c):
            grid[r][c] = 1
            q.append([r, c])
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if valid_range(nx, ny) and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        q.append([nx, ny])

        for x in range(n):
            for y in range(m):
                if is_side(x, y) and grid[x][y] == 0:
                    bfs(x, y)

        ans = 0
        for x in range(1, n - 1):
            for y in range(1, m - 1):
                if grid[x][y] == 0:
                    bfs(x, y)
                    ans += 1

        return ans
```

#### javascript

```js
// 63ms(92%), 45MB(47%)
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
var closedIsland = function (grid) {
  const n = grid.length
  const m = grid[0].length

  const dx = [0, 1, 0, -1]
  const dy = [1, 0, -1, 0]

  const isSide = (x, y) => {
    return x === 0 || y === 0 || x === n - 1 || y === m - 1
  }

  const validRange = (nx, ny) => {
    return 0 <= nx && nx < n && 0 <= ny && ny < m
  }

  const q = new MyQueue()
  const bfs = (r, c) => {
    grid[r][c] = 1
    q.enqueue([r, c])
    while (q.size > 0) {
      const [x, y] = q.dequeue()
      for (let i = 0; i < 4; i += 1) {
        const nx = x + dx[i]
        const ny = y + dy[i]
        if (validRange(nx, ny) && grid[nx][ny] === 0) {
          grid[nx][ny] = 1
          q.enqueue([nx, ny])
        }
      }
    }
  }

  for (let x = 0; x < n; x += 1) {
    for (let y = 0; y < m; y += 1) {
      if (isSide(x, y) && grid[x][y] === 0) {
        bfs(x, y)
      }
    }
  }

  let ans = 0
  for (let x = 0; x < n; x += 1) {
    for (let y = 0; y < m; y += 1) {
      if (grid[x][y] === 0) {
        bfs(x, y)
        ans += 1
      }
    }
  }

  return ans
}
```
