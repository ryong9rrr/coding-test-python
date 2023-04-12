> 2021 카카오 공채
> related topics : 플로이드-와샬, 다익스트라

이 문제는 출발정점(s)에서 어떤 한 정점(v)의 최단거리 + v에서 a의 최단거리 + v에서 b의 최단거리가 **최소**가 되는 정점 v를 찾는 것이 핵심인 문제인데... 어렵다...

# 접근 1 : 큐를 이용한 다익스트라 완전탐색 (시간초과)

1. 일단 s -> a, s -> b 최단거리를 구하고,
2. 모든 정점을 탐색하며 최단거리를 갱신하는 방법인데... 시간초과

#### python

```python
from collections import defaultdict, deque

def dijkstra(graph, v, w, n):
    # 다익스트라 세팅
    INF = int(1e9)
    q = deque()
    distances = [INF] * (n + 1)
    # 다익스트라 시작
    distances[v] = 0
    q.append(v)
    while q:
        node = q.popleft()
        for neighbor, cost in graph[node]:
            acc = distances[node] + cost
            if distances[neighbor] > acc:
                distances[neighbor] = acc
                q.append(neighbor)
    return distances[w]

def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    for v, w, cost in fares:
        graph[v].append([w, cost])
        graph[w].append([v, cost])

    ans = dijkstra(graph, s, a, n) + dijkstra(graph, s, b, n)

    for v in range(1, n + 1):
        if s == v:
            continue
        ans = min(ans, dijkstra(graph, s, v, n) + dijkstra(graph, v, a, n) + dijkstra(graph, v, b, n))

    return ans
"""
정확성  테스트
테스트 1 〉	통과 (0.08ms, 10.4MB)
테스트 2 〉	통과 (0.05ms, 10.4MB)
테스트 3 〉	통과 (0.07ms, 10.3MB)
테스트 4 〉	통과 (0.59ms, 10.4MB)
테스트 5 〉	통과 (0.21ms, 10.1MB)
테스트 6 〉	통과 (0.78ms, 10.3MB)
테스트 7 〉	통과 (0.57ms, 10.4MB)
테스트 8 〉	통과 (1.45ms, 10.3MB)
테스트 9 〉	통과 (0.89ms, 10.2MB)
테스트 10 〉	통과 (0.86ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (97.73ms, 10.3MB)
테스트 2 〉	통과 (897.67ms, 10.6MB)
테스트 3 〉	통과 (91.52ms, 10.3MB)
테스트 4 〉	통과 (89.12ms, 10.1MB)
테스트 5 〉	통과 (88.01ms, 10.3MB)
테스트 6 〉	통과 (104.07ms, 10.3MB)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	통과 (3333.05ms, 16MB)
테스트 10 〉	통과 (3300.92ms, 16.1MB)
테스트 11 〉	통과 (3168.02ms, 15.8MB)
테스트 12 〉	통과 (10137.58ms, 13.2MB)
테스트 13 〉	통과 (10541.84ms, 13MB)
테스트 14 〉	통과 (10246.97ms, 13MB)
테스트 15 〉	통과 (10785.48ms, 13MB)
테스트 16 〉	통과 (77.06ms, 10.2MB)
테스트 17 〉	통과 (80.33ms, 10.3MB)
테스트 18 〉	통과 (79.98ms, 10.2MB)
테스트 19 〉	통과 (445.02ms, 10.5MB)
테스트 20 〉	통과 (1129.90ms, 10.7MB)
테스트 21 〉	통과 (1120.87ms, 10.7MB)
테스트 22 〉	통과 (10925.03ms, 13MB)
테스트 23 〉	통과 (9882.37ms, 13.1MB)
테스트 24 〉	통과 (10942.00ms, 13.1MB)
테스트 25 〉	통과 (50.26ms, 10.2MB)
테스트 26 〉	통과 (35.02ms, 10.3MB)
테스트 27 〉	통과 (828.52ms, 10.5MB)
테스트 28 〉	통과 (857.41ms, 10.5MB)
테스트 29 〉	통과 (39.24ms, 10.1MB)
테스트 30 〉	통과 (62.26ms, 10.2MB)
"""
```

# 접근 2 : 힙(우선순위 큐)을 이용하여 최적화된 다익스트라

접근 1에서 그냥 큐를 사용하면 매번 연결된 모든 노드를 탐색해야한다.

이 부분을 다음과 같이 최적화한다. 거리를 기준으로 큐(힙)에 넣고, 힙에서 나온 최소거리의 노드가 이미 갱신되어있는 거리보다 멀다면 탐색하지 않아도 된다.

#### python

```python
from collections import defaultdict
import heapq

def dijkstra(graph, v, w, n):
    # 다익스트라 세팅
    INF = int(1e9)
    heap = []
    distances = [INF] * (n + 1)
    # 다익스트라 시작
    distances[v] = 0
    heapq.heappush(heap, [0, v])
    while heap:
        dist, node = heapq.heappop(heap)
        # 더 거리가 먼 노드라면 pass
        if distances[node] < dist:
            continue
        for neighbor, cost in graph[node]:
            acc = distances[node] + cost
            if distances[neighbor] > acc:
                distances[neighbor] = acc
                heapq.heappush(heap, [acc, neighbor])

    return distances[w]

def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    for v, w, cost in fares:
        graph[v].append([w, cost])
        graph[w].append([v, cost])

    ans = dijkstra(graph, s, a, n) + dijkstra(graph, s, b, n)

    for v in range(1, n + 1):
        if s == v:
            continue
        ans = min(ans, dijkstra(graph, s, v, n) + dijkstra(graph, v, a, n) + dijkstra(graph, v, b, n))

    return ans
"""
정확성  테스트
테스트 1 〉	통과 (0.09ms, 10.3MB)
테스트 2 〉	통과 (0.06ms, 10.1MB)
테스트 3 〉	통과 (0.13ms, 10.2MB)
테스트 4 〉	통과 (0.94ms, 10.4MB)
테스트 5 〉	통과 (0.36ms, 10.4MB)
테스트 6 〉	통과 (0.88ms, 10.3MB)
테스트 7 〉	통과 (0.91ms, 10.2MB)
테스트 8 〉	통과 (1.46ms, 10.2MB)
테스트 9 〉	통과 (1.01ms, 10.3MB)
테스트 10 〉	통과 (1.30ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (63.29ms, 10.2MB)
테스트 2 〉	통과 (326.88ms, 10.7MB)
테스트 3 〉	통과 (117.76ms, 10.3MB)
테스트 4 〉	통과 (110.03ms, 10.3MB)
테스트 5 〉	통과 (117.32ms, 10.2MB)
테스트 6 〉	통과 (121.11ms, 10.3MB)
테스트 7 〉	통과 (3816.83ms, 16.1MB)
테스트 8 〉	통과 (3884.08ms, 16MB)
테스트 9 〉	통과 (3377.89ms, 16MB)
테스트 10 〉	통과 (3465.95ms, 16.1MB)
테스트 11 〉	통과 (3377.58ms, 16MB)
테스트 12 〉	통과 (1868.21ms, 13.1MB)
테스트 13 〉	통과 (1949.34ms, 13.2MB)
테스트 14 〉	통과 (1824.57ms, 13.1MB)
테스트 15 〉	통과 (3013.49ms, 13.2MB)
테스트 16 〉	통과 (103.37ms, 10.2MB)
테스트 17 〉	통과 (103.49ms, 10.3MB)
테스트 18 〉	통과 (94.53ms, 10.4MB)
테스트 19 〉	통과 (273.46ms, 10.4MB)
테스트 20 〉	통과 (450.11ms, 10.6MB)
테스트 21 〉	통과 (421.05ms, 10.6MB)
테스트 22 〉	통과 (1906.48ms, 13.1MB)
테스트 23 〉	통과 (2100.78ms, 13.2MB)
테스트 24 〉	통과 (3159.24ms, 13.1MB)
테스트 25 〉	통과 (128.78ms, 10.4MB)
테스트 26 〉	통과 (59.60ms, 10.2MB)
테스트 27 〉	통과 (370.84ms, 10.7MB)
테스트 28 〉	통과 (402.34ms, 10.6MB)
테스트 29 〉	통과 (37.29ms, 10.2MB)
테스트 30 〉	통과 (38.81ms, 10.3MB)
"""
```

#### js

근데 자바스크립트로 힙 모듈을 사용해서 풀면 효율성 테스트에서 몇 개 시간초과가 떴다...

```js
class Heap {
  constructor(compareFn) {
    this.values = []

    this.compareFn = compareFn
  }

  compare(a, b) {
    const result = this.compareFn(a, b)
    if (typeof result === "boolean") {
      return result
    }
    return result < 0 ? true : false
  }

  get top() {
    return this.values.length > 0 ? this.values[0] : undefined
  }

  get size() {
    return this.values.length
  }

  add(element) {
    this.values.push(element)
    this.percolateUp(this.values.length - 1)
  }

  extract() {
    if (this.values.length < 1) {
      throw new Error("heap is empty")
    }

    const top = this.values[0]
    const end = this.values.pop()

    if (this.values.length > 0) {
      this.values[0] = end
      this.percolateDown(0)
    }

    // return the top
    return top
  }

  swap(aIndex, bIndex) {
    ;[this.values[aIndex], this.values[bIndex]] = [
      this.values[bIndex],
      this.values[aIndex],
    ]
  }

  parent(index) {
    return Math.floor(Math.floor((index - 1) / 2))
  }

  leftChild(index) {
    return index * 2 + 1
  }

  rightChild(index) {
    return index * 2 + 2
  }

  isLeaf(index) {
    return (
      index >= Math.floor(this.values.length / 2) &&
      index <= this.values.length - 1
    )
  }

  percolateUp(index) {
    let currentIndex = index
    let parentIndex = this.parent(currentIndex)

    while (
      currentIndex > 0 &&
      this.compare(this.values[currentIndex], this.values[parentIndex])
    ) {
      this.swap(currentIndex, parentIndex)
      currentIndex = parentIndex
      parentIndex = this.parent(parentIndex)
    }
  }

  percolateDown(index) {
    if (this.isLeaf(index)) {
      return
    }

    let leftChildIndex = this.leftChild(index)
    let rightChildIndex = this.rightChild(index)
    let largestIndex = index

    if (
      leftChildIndex < this.values.length &&
      this.compare(this.values[leftChildIndex], this.values[largestIndex])
    ) {
      largestIndex = leftChildIndex
    }

    if (
      rightChildIndex < this.values.length &&
      this.compare(this.values[rightChildIndex], this.values[largestIndex])
    ) {
      largestIndex = rightChildIndex
    }

    if (largestIndex !== index) {
      this.swap(index, largestIndex)
      this.percolateDown(largestIndex)
    }
  }
}

function makeGraph(n, fares) {
  const graph = {}
  for (let v = 1; v < n + 1; v += 1) {
    graph[v] = []
  }
  for (const [v, w, cost] of fares) {
    graph[v].push([w, cost])
    graph[w].push([v, cost])
  }
  return graph
}

function dijkstra(graph, v, w, n) {
  const distances = new Array(n + 1).fill(Infinity)
  const heap = new Heap((a, b) => a[0] - b[0])

  distances[v] = 0
  heap.add([0, v])

  while (heap.size > 0) {
    const [dist, node] = heap.extract()
    if (distances[node] < dist) {
      continue
    }
    for (const [neighbor, cost] of graph[node]) {
      const acc = distances[node] + cost
      if (distances[neighbor] > acc) {
        distances[neighbor] = acc
        heap.add([acc, neighbor])
      }
    }
  }
  return distances[w]
}

function solution(n, s, a, b, fares) {
  const graph = makeGraph(n, fares)

  let minCost = dijkstra(graph, s, a, n) + dijkstra(graph, s, b, n)
  for (let v = 1; v < n + 1; v += 1) {
    if (s === v) {
      continue
    }
    const dist =
      dijkstra(graph, s, v, n) +
      dijkstra(graph, v, a, n) +
      dijkstra(graph, v, b, n)
    minCost = Math.min(minCost, dist)
  }
  return minCost
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.99ms, 33.7MB)
// 테스트 2 〉	통과 (0.75ms, 33.6MB)
// 테스트 3 〉	통과 (0.86ms, 32.2MB)
// 테스트 4 〉	통과 (5.33ms, 39MB)
// 테스트 5 〉	통과 (1.74ms, 34MB)
// 테스트 6 〉	통과 (5.31ms, 38.9MB)
// 테스트 7 〉	통과 (5.31ms, 39.2MB)
// 테스트 8 〉	통과 (6.91ms, 38.8MB)
// 테스트 9 〉	통과 (10.02ms, 39.3MB)
// 테스트 10 〉	통과 (8.46ms, 39.4MB)
// 효율성  테스트
// 테스트 1 〉	통과 (47.00ms, 41MB)
// 테스트 2 〉	통과 (124.38ms, 43.5MB)
// 테스트 3 〉	통과 (83.37ms, 41.7MB)
// 테스트 4 〉	통과 (108.27ms, 41.7MB)
// 테스트 5 〉	통과 (107.72ms, 41.7MB)
// 테스트 6 〉	통과 (97.08ms, 41.8MB)
// 테스트 7 〉	실패 (시간 초과)
// 테스트 8 〉	실패 (시간 초과)
// 테스트 9 〉	통과 (319.16ms, 59.7MB)
// 테스트 10 〉	통과 (297.96ms, 59.8MB)
// 테스트 11 〉	통과 (294.98ms, 60.2MB)
// 테스트 12 〉	통과 (363.78ms, 49.1MB)
// 테스트 13 〉	실패 (시간 초과)
// 테스트 14 〉	통과 (360.14ms, 49.4MB)
// 테스트 15 〉	통과 (397.11ms, 49.3MB)
// 테스트 16 〉	통과 (82.48ms, 41.8MB)
// 테스트 17 〉	통과 (76.01ms, 41.3MB)
// 테스트 18 〉	통과 (76.51ms, 41.6MB)
// 테스트 19 〉	통과 (116.61ms, 42.9MB)
// 테스트 20 〉	통과 (169.41ms, 43.7MB)
// 테스트 21 〉	통과 (159.08ms, 43.5MB)
// 테스트 22 〉	통과 (361.95ms, 49.3MB)
// 테스트 23 〉	실패 (시간 초과)
// 테스트 24 〉	실패 (시간 초과)
// 테스트 25 〉	통과 (53.31ms, 39.8MB)
// 테스트 26 〉	통과 (101.08ms, 41.4MB)
// 테스트 27 〉	통과 (153.10ms, 43.8MB)
// 테스트 28 〉	통과 (155.51ms, 43.2MB)
// 테스트 29 〉	통과 (55.33ms, 41.6MB)
// 테스트 30 〉	통과 (47.49ms, 41.3MB)
```

# 접근 3 : 플로이드-와샬

플로이드-와샬을 이런식으로 사용할 수도 있었다....

#### python

```python
def solution(n, s, a, b, fares):
    # 모든 정점으로 가는 거리를 무한대로 초기화
    INF = int(1e9)
    dp = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신으로 가는 거리는 0으로 초기화
    for v in range(1, n + 1):
        dp[v][v] = 0

    # 간선 비용 정보 삽입
    for v, w, cost in fares:
        dp[v][w] = cost
        dp[w][v] = cost

    # 플로이드-와샬 시작
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    # 모든 노드를 순회하면서 최저 비용 갱신
    min_cost = dp[s][a] + dp[s][b]
    for v in range(1, n + 1):
        min_cost = min(min_cost, dp[v][s] + dp[v][a] + dp[v][b])
    return min_cost
"""
정확성  테스트
테스트 1 〉	통과 (0.09ms, 10.4MB)
테스트 2 〉	통과 (0.21ms, 10.2MB)
테스트 3 〉	통과 (0.08ms, 10.3MB)
테스트 4 〉	통과 (0.32ms, 10.2MB)
테스트 5 〉	통과 (1.00ms, 10.1MB)
테스트 6 〉	통과 (0.81ms, 10.2MB)
테스트 7 〉	통과 (0.53ms, 10.2MB)
테스트 8 〉	통과 (1.29ms, 10.2MB)
테스트 9 〉	통과 (3.25ms, 10.3MB)
테스트 10 〉	통과 (2.71ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (297.48ms, 10.5MB)
테스트 2 〉	통과 (943.67ms, 11MB)
테스트 3 〉	통과 (2221.11ms, 11.3MB)
테스트 4 〉	통과 (2221.61ms, 11.4MB)
테스트 5 〉	통과 (2255.57ms, 11.4MB)
테스트 6 〉	통과 (2325.31ms, 11.4MB)
테스트 7 〉	통과 (2381.80ms, 13.7MB)
테스트 8 〉	통과 (2479.36ms, 13.8MB)
테스트 9 〉	통과 (2470.02ms, 12.8MB)
테스트 10 〉	통과 (2282.05ms, 13MB)
테스트 11 〉	통과 (2410.73ms, 13MB)
테스트 12 〉	통과 (2385.14ms, 12.8MB)
테스트 13 〉	통과 (2354.75ms, 12.8MB)
테스트 14 〉	통과 (2341.75ms, 12.6MB)
테스트 15 〉	통과 (2347.49ms, 12.7MB)
테스트 16 〉	통과 (2336.47ms, 11.4MB)
테스트 17 〉	통과 (2206.34ms, 11.3MB)
테스트 18 〉	통과 (2338.41ms, 11MB)
테스트 19 〉	통과 (2347.20ms, 11.4MB)
테스트 20 〉	통과 (2441.56ms, 11.6MB)
테스트 21 〉	통과 (2361.09ms, 11.7MB)
테스트 22 〉	통과 (2360.22ms, 12.7MB)
테스트 23 〉	통과 (2368.99ms, 12.7MB)
테스트 24 〉	통과 (2271.24ms, 12.8MB)
테스트 25 〉	통과 (2270.61ms, 11.1MB)
테스트 26 〉	통과 (2375.43ms, 10.9MB)
테스트 27 〉	통과 (2265.74ms, 10.5MB)
테스트 28 〉	통과 (2231.76ms, 10.4MB)
테스트 29 〉	통과 (283.44ms, 10.3MB)
테스트 30 〉	통과 (281.94ms, 10.4MB)
"""
```

#### js

```js
function solution(n, s, a, b, fares) {
  const dp = Array.from({ length: n + 1 }, () =>
    new Array(n + 1).fill(Infinity),
  )

  for (let v = 1; v < n + 1; v += 1) {
    dp[v][v] = 0
  }

  for (const [v, w, cost] of fares) {
    dp[v][w] = cost
    dp[w][v] = cost
  }

  for (let k = 1; k < n + 1; k += 1) {
    for (let i = 1; i < n + 1; i += 1) {
      for (let j = 1; j < n + 1; j += 1) {
        dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k][j])
      }
    }
  }

  let minCost = dp[s][a] + dp[s][b]
  for (let v = 1; v < n + 1; v += 1) {
    minCost = Math.min(minCost, dp[v][s] + dp[v][a] + dp[v][b])
  }
  return minCost
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.30ms, 33.5MB)
// 테스트 2 〉	통과 (0.33ms, 33.6MB)
// 테스트 3 〉	통과 (0.30ms, 33.5MB)
// 테스트 4 〉	통과 (0.41ms, 33.7MB)
// 테스트 5 〉	통과 (0.50ms, 33.6MB)
// 테스트 6 〉	통과 (0.67ms, 33.7MB)
// 테스트 7 〉	통과 (0.54ms, 33.7MB)
// 테스트 8 〉	통과 (0.88ms, 33.8MB)
// 테스트 9 〉	통과 (1.07ms, 33.9MB)
// 테스트 10 〉	통과 (1.33ms, 34MB)
// 효율성  테스트
// 테스트 1 〉	통과 (11.06ms, 38MB)
// 테스트 2 〉	통과 (47.37ms, 38.2MB)
// 테스트 3 〉	통과 (44.02ms, 38.3MB)
// 테스트 4 〉	통과 (66.43ms, 37.9MB)
// 테스트 5 〉	통과 (46.80ms, 38.3MB)
// 테스트 6 〉	통과 (69.16ms, 38.3MB)
// 테스트 7 〉	통과 (48.00ms, 45.2MB)
// 테스트 8 〉	통과 (75.32ms, 44.7MB)
// 테스트 9 〉	통과 (44.21ms, 45.2MB)
// 테스트 10 〉	통과 (47.29ms, 44.9MB)
// 테스트 11 〉	통과 (47.56ms, 45MB)
// 테스트 12 〉	통과 (52.71ms, 42.7MB)
// 테스트 13 〉	통과 (52.09ms, 42.7MB)
// 테스트 14 〉	통과 (52.89ms, 42.8MB)
// 테스트 15 〉	통과 (51.11ms, 42.4MB)
// 테스트 16 〉	통과 (109.66ms, 37.9MB)
// 테스트 17 〉	통과 (68.36ms, 37.9MB)
// 테스트 18 〉	통과 (70.39ms, 37.9MB)
// 테스트 19 〉	통과 (44.07ms, 38.8MB)
// 테스트 20 〉	통과 (46.44ms, 39.1MB)
// 테스트 21 〉	통과 (90.84ms, 38.9MB)
// 테스트 22 〉	통과 (52.12ms, 42.7MB)
// 테스트 23 〉	통과 (51.17ms, 42.6MB)
// 테스트 24 〉	통과 (52.08ms, 42.6MB)
// 테스트 25 〉	통과 (44.83ms, 38.3MB)
// 테스트 26 〉	통과 (50.61ms, 38.4MB)
// 테스트 27 〉	통과 (47.19ms, 39.3MB)
// 테스트 28 〉	통과 (45.00ms, 39.2MB)
// 테스트 29 〉	통과 (12.48ms, 38.1MB)
// 테스트 30 〉	통과 (12.03ms, 38MB)
```
