---
layout: post
title: "프로그래머스 Lv2) 배달"
tags: [BFS, 다익스트라]
comments: true
categories:
---

> 전형적인 다익스트라 (썸머/윈터 2018)

---

> [프로그래머스 Lv2) 배달](https://school.programmers.co.kr/learn/courses/30/lessons/12978)

# 접근 : 다익스트라

- 시간복잡도 : O(V + E)
- 공간복잡도 : O(V + E)

#### python

```python
from collections import defaultdict, deque

def solution(N, road, K):
    # 초기 양방향 그래프 구성
    graph = defaultdict(list)
    for v, w, cost in road:
        graph[v].append([w, cost])
        graph[w].append([v, cost])

    # 비용 테이블 초기화
    INF = int(1e9)
    costs = [INF] * (N + 1)

    # 다익스트라 시작, 1번 노드부터 시작
    q = deque([1])
    costs[1] = 0
    while q:
        node = q.popleft()
        for neighbor, cost in graph[node]:
            acc = costs[node] + cost
            # K시간 이하에 배달이 가능하고, 더 작은 값으로 갱신할 수 있다면
            if acc <= K and costs[neighbor] > acc:
                costs[neighbor] = acc
                q.append(neighbor)

    return len([cost for cost in costs if cost < INF])
"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.4MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.4MB)
테스트 8 〉	통과 (0.02ms, 10.4MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.03ms, 10.4MB)
테스트 14 〉	통과 (0.59ms, 10.5MB)
테스트 15 〉	통과 (0.69ms, 10.6MB)
테스트 16 〉	통과 (0.02ms, 10.2MB)
테스트 17 〉	통과 (0.03ms, 10.2MB)
테스트 18 〉	통과 (0.23ms, 10.2MB)
테스트 19 〉	통과 (0.53ms, 10.5MB)
테스트 20 〉	통과 (0.14ms, 10.2MB)
테스트 21 〉	통과 (0.75ms, 10.6MB)
테스트 22 〉	통과 (0.22ms, 10.4MB)
테스트 23 〉	통과 (0.88ms, 10.7MB)
테스트 24 〉	통과 (1.23ms, 10.5MB)
테스트 25 〉	통과 (1.27ms, 10.6MB)
테스트 26 〉	통과 (1.39ms, 10.7MB)
테스트 27 〉	통과 (1.95ms, 10.8MB)
테스트 28 〉	통과 (1.38ms, 10.7MB)
테스트 29 〉	통과 (2.83ms, 10.7MB)
테스트 30 〉	통과 (2.29ms, 10.6MB)
테스트 31 〉	통과 (0.09ms, 10.2MB)
테스트 32 〉	통과 (0.08ms, 10.3MB)
"""
```

#### js

노드의 개수가 최대 50밖에 되지 않아서 따로 큐나 데크 자료구조를 사용하지 않아도 시간초과는 나지 않았음.

```js
const initializeGraph = (n) => {
  const graph = {}
  for (let node = 1; node <= n; node += 1) {
    graph[node] = []
  }
  return graph
}

function solution(N, road, K) {
  // 초기 양방향 그래프 세팅
  const graph = initializeGraph(N)
  for (const [v, w, cost] of road) {
    graph[v].push([w, cost])
    graph[w].push([v, cost])
  }

  // 비용 테이블 초기화
  const costs = new Array(N + 1).fill(Infinity)

  // 다익스트라 시작, 1번 노드부터 시작
  const q = [1]
  costs[1] = 0

  while (q.length > 0) {
    const node = q.shift()
    for (const [neighbor, cost] of graph[node]) {
      const acc = costs[node] + cost
      if (acc <= K && acc < costs[neighbor]) {
        costs[neighbor] = acc
        q.push(neighbor)
      }
    }
  }

  return costs.filter((cost) => cost < Infinity).length
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.34ms, 33.6MB)
// 테스트 2 〉	통과 (0.46ms, 33.4MB)
// 테스트 3 〉	통과 (0.37ms, 33.6MB)
// 테스트 4 〉	통과 (0.55ms, 33.5MB)
// 테스트 5 〉	통과 (0.35ms, 33.4MB)
// 테스트 6 〉	통과 (0.18ms, 33.6MB)
// 테스트 7 〉	통과 (0.43ms, 33.6MB)
// 테스트 8 〉	통과 (0.22ms, 33.4MB)
// 테스트 9 〉	통과 (0.45ms, 33.4MB)
// 테스트 10 〉	통과 (0.39ms, 33.6MB)
// 테스트 11 〉	통과 (0.37ms, 33.6MB)
// 테스트 12 〉	통과 (0.56ms, 33.5MB)
// 테스트 13 〉	통과 (0.59ms, 33.5MB)
// 테스트 14 〉	통과 (1.10ms, 34.3MB)
// 테스트 15 〉	통과 (3.89ms, 34.8MB)
// 테스트 16 〉	통과 (0.40ms, 33.5MB)
// 테스트 17 〉	통과 (0.43ms, 33.6MB)
// 테스트 18 〉	통과 (0.52ms, 33.7MB)
// 테스트 19 〉	통과 (1.68ms, 34.4MB)
// 테스트 20 〉	통과 (0.52ms, 33.7MB)
// 테스트 21 〉	통과 (1.63ms, 34.7MB)
// 테스트 22 〉	통과 (1.26ms, 33.7MB)
// 테스트 23 〉	통과 (2.58ms, 34.9MB)
// 테스트 24 〉	통과 (2.46ms, 34.8MB)
// 테스트 25 〉	통과 (2.36ms, 34.8MB)
// 테스트 26 〉	통과 (2.52ms, 35.1MB)
// 테스트 27 〉	통과 (2.98ms, 35.3MB)
// 테스트 28 〉	통과 (3.80ms, 35.1MB)
// 테스트 29 〉	통과 (6.88ms, 35.4MB)
// 테스트 30 〉	통과 (3.06ms, 35MB)
// 테스트 31 〉	통과 (0.67ms, 33.6MB)
// 테스트 32 〉	통과 (0.75ms, 33.6MB)
```
