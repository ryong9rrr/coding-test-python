> related topics : 그래프, 유니온파인드, 크루스칼 알고리즘, 최소신장트리

# 접근 : 유니온파인드 + 크루스칼 알고리즘 (최소신장트리)

```python
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    x, y = find_parent(parent, a), find_parent(parent, b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def solution(n, costs):
    costs = sorted(costs, key=lambda x: x[2]) # 비용이 적은 간선 순으로
    parent = [x for x in range(n)]

    ans = 0
    for v, w, cost in costs:
        if find_parent(parent, v) != find_parent(parent, w):
            ans += cost
            union_parent(parent, v, w)

    return ans
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.4MB)
테스트 6 〉	통과 (0.05ms, 10.2MB)
테스트 7 〉	통과 (0.06ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.1MB)
"""
```

```js
const findParent = (parent, x) => {
  if (parent[x] !== x) {
    parent[x] = findParent(parent, parent[x])
  }
  return parent[x]
}

const unionParent = (parent, a, b) => {
  const x = findParent(parent, a)
  const y = findParent(parent, b)
  if (x < y) {
    parent[y] = x
  } else {
    parent[x] = y
  }
}

function solution(n, costs) {
  costs = costs.sort((a, b) => a[2] - b[2])
  const parent = Array.from({ length: n }, (v, i) => i)

  let ans = 0
  for (const [v, w, cost] of costs) {
    if (findParent(parent, v) !== findParent(parent, w)) {
      ans += cost
      unionParent(parent, v, w)
    }
  }
  return ans
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.13ms, 33.4MB)
// 테스트 2 〉	통과 (0.13ms, 33.5MB)
// 테스트 3 〉	통과 (0.23ms, 33.4MB)
// 테스트 4 〉	통과 (0.33ms, 33.6MB)
// 테스트 5 〉	통과 (0.23ms, 33.5MB)
// 테스트 6 〉	통과 (0.33ms, 33.5MB)
// 테스트 7 〉	통과 (0.33ms, 33.5MB)
// 테스트 8 〉	통과 (0.21ms, 33.5MB)
```
