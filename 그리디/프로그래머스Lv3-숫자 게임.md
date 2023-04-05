# 프로그래머스 Lv3 : 숫자 게임

> related topics : 그리디, 정렬, 큐, 힙

## 접근 1 : 정렬된 큐 + 힙

#### python

```python
from collections import deque
import heapq

def solution(A, B):
    if min(A) >= max(B):
        return 0

    # A는 큐로,
    a_queue = deque(sorted(A))

    # B는 힙으로 만듬
    heap = []
    for num in B:
        heapq.heappush(heap, num)

    ans = 0
    while a_queue and heap:
        a = a_queue[0]
        b = heap[0]

        if a < b:
            a_queue.popleft()
            heapq.heappop(heap)
            ans += 1
            continue

        while a_queue and heap and a_queue[0] >= heap[0]:
            heapq.heappop(heap)

    return ans
```

## 접근 2 : 정렬 + 투포인터

#### python

```python
def solution(A, B):
    A.sort()
    B.sort()

    ans = 0
    index_A = index_B = 0 # 투포인터
    while index_A < len(A) and index_B < len(B):
        if A[index_A] < B[index_B]:
            ans += 1
            index_A += 1
        index_B += 1
    return ans
"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.07ms, 10.3MB)
테스트 7 〉	통과 (0.05ms, 9.98MB)
테스트 8 〉	통과 (0.03ms, 10.3MB)
테스트 9 〉	통과 (0.31ms, 10.2MB)
테스트 10 〉	통과 (0.40ms, 10.4MB)
테스트 11 〉	통과 (0.36ms, 10MB)
테스트 12 〉	통과 (0.16ms, 10.4MB)
테스트 13 〉	통과 (4.12ms, 10.5MB)
테스트 14 〉	통과 (4.08ms, 10.5MB)
테스트 15 〉	통과 (4.41ms, 10.2MB)
테스트 16 〉	통과 (3.80ms, 10.4MB)
테스트 17 〉	통과 (0.93ms, 10.4MB)
테스트 18 〉	통과 (0.80ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (61.97ms, 18.5MB)
테스트 2 〉	통과 (57.59ms, 18.2MB)
테스트 3 〉	통과 (53.12ms, 18.3MB)
"""
```

#### js

```js
function solution(A, B) {
  const a = A.sort((a, b) => a - b)
  const b = B.sort((a, b) => a - b)

  let ans = 0
  let aIndex = 0
  let bIndex = 0
  while (aIndex < a.length && bIndex < b.length) {
    if (a[aIndex] < b[bIndex]) {
      ans += 1
      aIndex += 1
    }
    bIndex += 1
  }
  return ans
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.06ms, 33.7MB)
// 테스트 2 〉	통과 (0.06ms, 33.8MB)
// 테스트 3 〉	통과 (0.06ms, 33.7MB)
// 테스트 4 〉	통과 (0.07ms, 33.4MB)
// 테스트 5 〉	통과 (0.15ms, 33.6MB)
// 테스트 6 〉	통과 (0.17ms, 33.5MB)
// 테스트 7 〉	통과 (0.17ms, 33.6MB)
// 테스트 8 〉	통과 (0.17ms, 33.5MB)
// 테스트 9 〉	통과 (0.58ms, 33.7MB)
// 테스트 10 〉	통과 (0.44ms, 33.5MB)
// 테스트 11 〉	통과 (0.69ms, 33.7MB)
// 테스트 12 〉	통과 (0.36ms, 33.6MB)
// 테스트 13 〉	통과 (4.18ms, 36MB)
// 테스트 14 〉	통과 (6.42ms, 36.5MB)
// 테스트 15 〉	통과 (4.13ms, 36.2MB)
// 테스트 16 〉	통과 (5.78ms, 36.5MB)
// 테스트 17 〉	통과 (0.33ms, 33.6MB)
// 테스트 18 〉	통과 (0.60ms, 34MB)
// 효율성  테스트
// 테스트 1 〉	통과 (66.00ms, 45.5MB)
// 테스트 2 〉	통과 (67.02ms, 44.1MB)
// 테스트 3 〉	통과 (70.63ms, 45MB)
```
