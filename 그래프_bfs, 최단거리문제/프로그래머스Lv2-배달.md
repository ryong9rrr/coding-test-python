> 썸머/윈터 2018
> related topics : BFS, 다익스트라

# 접근 : 다익스트라

- 시간복잡도 : O(V + E)
- 공간복잡도 : O(V + E)

#### python

```python
from collections import defaultdict, deque
def solution(N, road, K):
    INF = int(1e9)
    graph = defaultdict(list)

    for v, w, cost in road:
        graph[v].append([w, cost])
        graph[w].append([v, cost])

    # 처음에는 도달하지 못한 상태로 가정
    distances = [INF] * (N + 1)
    q = deque()

    # 다익스트라 시작 : 다익스트라 BFS가 끝난 이후에 distances에는 최단거리가 담기게 됨.
    # 1번 마을 부터 출발
    distances[1] = 0
    q.append(1)
    while q:
        node = q.popleft()
        for neighbor, cost in graph[node]:
            acc = distances[node] + cost
            # 거리가 더 작을 경우에만 갱신
            if acc < distances[neighbor]:
                distances[neighbor] = acc
                q.append(neighbor)

    # 최단거리가 K이하인 것들만 찾아서 리턴
    return len([dist for dist in distances if dist <= K])
"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.05ms, 10MB)
테스트 5 〉	통과 (0.03ms, 10.1MB)
테스트 6 〉	통과 (0.02ms, 10.1MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.1MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.03ms, 10.1MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.04ms, 10.2MB)
테스트 13 〉	통과 (0.05ms, 10.3MB)
테스트 14 〉	통과 (1.19ms, 10.1MB)
테스트 15 〉	통과 (1.63ms, 10.4MB)
테스트 16 〉	통과 (0.03ms, 10.1MB)
테스트 17 〉	통과 (0.03ms, 10.2MB)
테스트 18 〉	통과 (0.34ms, 10.1MB)
테스트 19 〉	통과 (1.35ms, 10.4MB)
테스트 20 〉	통과 (0.26ms, 10.3MB)
테스트 21 〉	통과 (3.87ms, 10.5MB)
테스트 22 〉	통과 (0.62ms, 10.1MB)
테스트 23 〉	통과 (2.32ms, 10.4MB)
테스트 24 〉	통과 (1.17ms, 10.4MB)
테스트 25 〉	통과 (6.01ms, 10.6MB)
테스트 26 〉	통과 (5.48ms, 10.5MB)
테스트 27 〉	통과 (3.52ms, 10.6MB)
테스트 28 〉	통과 (3.78ms, 10.5MB)
테스트 29 〉	통과 (5.52ms, 10.6MB)
테스트 30 〉	통과 (2.33ms, 10.6MB)
테스트 31 〉	통과 (0.08ms, 10.2MB)
테스트 32 〉	통과 (0.12ms, 10.1MB)
"""
```

`K` 거리를 초과한다면 아예 순회하지 않는 것으로 다익스트라 코드 내부에서 최적화를 해줄 수도 있음.

```python
from collections import defaultdict, deque
def solution(N, road, K):
    INF = int(1e9)
    graph = defaultdict(list)

    for v, w, cost in road:
        graph[v].append([w, cost])
        graph[w].append([v, cost])

    # 처음에는 도달하지 못한 상태로 가정
    distances = [INF] * (N + 1)
    q = deque()

    # 다익스트라 시작 : 다익스트라 BFS가 끝난 이후에 distances에는 최단거리가 담기게 됨.
    # 1번 마을 부터 출발
    distances[1] = 0
    q.append(1)
    ans = 1
    while q:
        node = q.popleft()
        for neighbor, cost in graph[node]:
            acc = distances[node] + cost
            if acc > K: # 최적화
                continue
            # 거리가 더 작을 경우에만 갱신
            if acc < distances[neighbor]:
                distances[neighbor] = acc
                q.append(neighbor)

    # 도달가능한 노드만
    return len([dist for dist in distances if dist != INF])
"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (0.03ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.1MB)
테스트 12 〉	통과 (0.03ms, 10.3MB)
테스트 13 〉	통과 (0.03ms, 9.98MB)
테스트 14 〉	통과 (0.47ms, 10.1MB)
테스트 15 〉	통과 (0.72ms, 10.6MB)
테스트 16 〉	통과 (0.02ms, 9.98MB)
테스트 17 〉	통과 (0.03ms, 10.1MB)
테스트 18 〉	통과 (0.21ms, 10.1MB)
테스트 19 〉	통과 (0.51ms, 10.4MB)
테스트 20 〉	통과 (0.23ms, 10MB)
테스트 21 〉	통과 (1.32ms, 10.6MB)
테스트 22 〉	통과 (0.37ms, 10.3MB)
테스트 23 〉	통과 (1.46ms, 10.5MB)
테스트 24 〉	통과 (1.17ms, 10.3MB)
테스트 25 〉	통과 (1.16ms, 10.3MB)
테스트 26 〉	통과 (1.29ms, 10.4MB)
테스트 27 〉	통과 (1.47ms, 10.4MB)
테스트 28 〉	통과 (1.39ms, 10.6MB)
테스트 29 〉	통과 (1.53ms, 10.5MB)
테스트 30 〉	통과 (1.33ms, 10.5MB)
테스트 31 〉	통과 (0.05ms, 10.1MB)
테스트 32 〉	통과 (0.08ms, 9.91MB)
"""
```

#### js

Deque 자료구조를 사용해도되고, 안해도 시간초과는 안걸린다.

```js
class Node {
  constructor(value, prev = null, next = null) {
    this.value = value
    this.prev = prev
    this.next = next
  }
}

class Deque {
  constructor() {
    this._head = null
    this._tail = null
    this._length = 0
  }

  get head() {
    return this._head ? this._head.value : null
  }

  get tail() {
    return this._tail ? this._tail.value : null
  }

  get length() {
    return this._length
  }

  unshift(element) {
    const newNode = new Node(element, null, this._head)
    if (this._head) {
      this._head.prev = newNode
    } else {
      this._tail = newNode
    }
    this._head = newNode
    this._length++
  }

  push(element) {
    const newNode = new Node(element, this._tail, null)
    if (this._tail) {
      this._tail.next = newNode
    } else {
      this._head = newNode
    }
    this._tail = newNode
    this._length++
  }

  shift() {
    if (!this._head) {
      return null
    }
    const removedNode = this._head
    if (this._head === this._tail) {
      this._head = null
      this._tail = null
    } else {
      this._head = removedNode.next
      this._head.prev = null
    }
    this._length--
    return removedNode.value
  }

  pop() {
    if (!this._tail) {
      return null
    }
    const removedNode = this._tail
    if (this._head === this._tail) {
      this._head = null
      this._tail = null
    } else {
      this._tail = removedNode.prev
      this._tail.next = null
    }
    this._length--
    return removedNode.value
  }

  clear() {
    this._head = null
    this._tail = null
    this._length = 0
  }
}

const makeGraph = (road) => {
  const graph = {}
  for (const [v, w, cost] of road) {
    if (!graph[v]) graph[v] = []
    if (!graph[w]) graph[w] = []
    graph[v].push([w, cost])
    graph[w].push([v, cost])
  }
  return graph
}

function solution(N, road, K) {
  const graph = makeGraph(road)
  const distances = new Array(N + 1).fill(Infinity)

  // 다익스트라, 1번 노드부터 시작
  const q = new Deque()
  distances[1] = 0
  q.push(1)

  while (q.length > 0) {
    const node = q.shift()
    if (!graph[node]) {
      continue
    }
    for (const [neighbor, cost] of graph[node]) {
      const acc = distances[node] + cost
      if (acc > K) {
        continue
      }
      if (acc < distances[neighbor]) {
        distances[neighbor] = acc
        q.push(neighbor)
      }
    }
  }

  return distances.filter((dist) => dist !== Infinity).length
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.29ms, 33.6MB)
// 테스트 2 〉	통과 (0.28ms, 33.8MB)
// 테스트 3 〉	통과 (0.42ms, 33.6MB)
// 테스트 4 〉	통과 (0.45ms, 33.6MB)
// 테스트 5 〉	통과 (0.27ms, 33MB)
// 테스트 6 〉	통과 (0.14ms, 32.9MB)
// 테스트 7 〉	통과 (0.29ms, 32.9MB)
// 테스트 8 〉	통과 (0.26ms, 33.4MB)
// 테스트 9 〉	통과 (0.30ms, 33.3MB)
// 테스트 10 〉	통과 (0.36ms, 33.3MB)
// 테스트 11 〉	통과 (0.51ms, 33.3MB)
// 테스트 12 〉	통과 (0.50ms, 33.4MB)
// 테스트 13 〉	통과 (0.40ms, 33.4MB)
// 테스트 14 〉	통과 (1.64ms, 34.4MB)
// 테스트 15 〉	통과 (3.75ms, 34.6MB)
// 테스트 16 〉	통과 (0.42ms, 32.8MB)
// 테스트 17 〉	통과 (0.34ms, 33.4MB)
// 테스트 18 〉	통과 (0.48ms, 33.6MB)
// 테스트 19 〉	통과 (1.71ms, 34.4MB)
// 테스트 20 〉	통과 (0.60ms, 33.6MB)
// 테스트 21 〉	통과 (1.79ms, 34.6MB)
// 테스트 22 〉	통과 (0.70ms, 33.3MB)
// 테스트 23 〉	통과 (2.92ms, 34.7MB)
// 테스트 24 〉	통과 (2.27ms, 34.6MB)
// 테스트 25 〉	통과 (2.62ms, 34.6MB)
// 테스트 26 〉	통과 (2.62ms, 35MB)
// 테스트 27 〉	통과 (3.00ms, 35MB)
// 테스트 28 〉	통과 (2.76ms, 34.9MB)
// 테스트 29 〉	통과 (6.23ms, 35.2MB)
// 테스트 30 〉	통과 (2.82ms, 35.1MB)
// 테스트 31 〉	통과 (0.36ms, 33.6MB)
// 테스트 32 〉	통과 (0.49ms, 33.6MB)
```
