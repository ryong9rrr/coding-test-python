> related topics : DFS, BFS, 2차원 배열

`image[sr][sc]` 에 `color`를 떨어뜨려서 동서남북 방향으로 물감을 퍼지게 했을 때, 퍼진 이후의 `image` 행렬을 반환하는 문제.

## 접근 1 : DFS

#### python

```python
# 74ms(82%), 14MB(30%)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        n = len(image)
        m = len(image[0])

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        def valid_range(nx, ny):
            return 0 <= nx < n and 0 <= ny < m

        def dfs(x, y, val):
            image[x][y] = color
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if valid_range(nx, ny) and image[nx][ny] == val:
                    dfs(nx, ny, val)

        dfs(sr, sc, image[sr][sc])

        return image
```

#### javascript

```js
// 63ms(94%), 44MB(31%)
/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */
var floodFill = function (image, sr, sc, color) {
  if (image[sr][sc] === color) {
    return image
  }

  const n = image.length
  const m = image[0].length

  const dx = [0, 1, 0, -1]
  const dy = [1, 0, -1, 0]

  const validRange = (nx, ny) => {
    return 0 <= nx && nx < n && 0 <= ny && ny < m
  }

  const dfs = (x, y, val) => {
    image[x][y] = color
    for (let i = 0; i < 4; i += 1) {
      const nx = x + dx[i]
      const ny = y + dy[i]
      if (validRange(nx, ny) && image[nx][ny] === val) {
        dfs(nx, ny, val)
      }
    }
  }

  dfs(sr, sc, image[sr][sc])

  return image
}
```

## 접근 2 : BFS

#### python

```python
# 68ms(97%), 14MB(58%)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        n = len(image)
        m = len(image[0])

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        def valid_range(nx, ny):
            return 0 <= nx < n and 0 <= ny < m

        initial_value = image[sr][sc]
        q = collections.deque([[sr, sc]])

        while q:
            x, y = q.popleft()
            image[x][y] = color
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if valid_range(nx, ny) and image[nx][ny] == initial_value:
                    q.append([nx, ny])

        return image
```

#### javascript

```js
// 66ms(88%), 44MB(67%)
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
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */
var floodFill = function (image, sr, sc, color) {
  if (image[sr][sc] === color) {
    return image
  }

  const n = image.length
  const m = image[0].length

  const dx = [0, 1, 0, -1]
  const dy = [1, 0, -1, 0]

  const validRange = (nx, ny) => {
    return 0 <= nx && nx < n && 0 <= ny && ny < m
  }

  const initialValue = image[sr][sc]
  const q = new MyQueue()
  q.enqueue([sr, sc])

  while (q.size > 0) {
    const [x, y] = q.dequeue()
    image[x][y] = color

    for (let i = 0; i < 4; i += 1) {
      const nx = x + dx[i]
      const ny = y + dy[i]

      if (validRange(nx, ny) && image[nx][ny] === initialValue) {
        q.enqueue([nx, ny])
      }
    }
  }

  return image
}
```
