> https://school.programmers.co.kr/learn/courses/30/lessons/12987
> related topics : 그리디, 정렬, 배열, 힙

일단 이 문제는 그리디 기반의 문제임.

힙 풀이도 좋지만 배열의 인덱스를 잘 조정해서 푸는 것이 제일 베스트인 것 같다.

# 접근 1 : 이분탐색 (효율성에서 시간초과)

이분탐색을 하려면 **배열을 매번 정렬시켜야**한다. 이 부분에서 시간초과가 난듯. 따라서 **힙**을 사용하자.

```python
from bisect import bisect_left

def solution(A, B):
    if max(B) < min(A):
        return 0

    setB = set(B)
    B.sort() # 이분탐색을 위해서

    ans = 0
    for a in A:
        index = bisect_left(B, a + 1)
        if 0 <= index < len(B):
            ans += 1
            setB.remove(B[index])
            B = sorted(list(setB))

    return ans
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.07ms, 10.2MB)
테스트 6 〉	통과 (0.23ms, 10.2MB)
테스트 7 〉	통과 (0.33ms, 10.4MB)
테스트 8 〉	통과 (0.11ms, 10.2MB)
테스트 9 〉	통과 (25.71ms, 10.4MB)
테스트 10 〉	통과 (11.74ms, 10.4MB)
테스트 11 〉	통과 (31.59ms, 10.4MB)
테스트 12 〉	통과 (9.59ms, 10.1MB)
테스트 13 〉	통과 (1747.39ms, 11.1MB)
테스트 14 〉	통과 (4609.06ms, 11.4MB)
테스트 15 〉	통과 (2020.52ms, 11.1MB)
테스트 16 〉	통과 (3936.82ms, 11.1MB)
테스트 17 〉	통과 (31.88ms, 10.4MB)
테스트 18 〉	통과 (1.43ms, 10.3MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
"""
```

# 접근 2 : 힙

#### python

```python
import heapq

def solution(A, B):
    A.sort() # 순서는 중요하지 않으므로 정렬

    # B 카드는 모두 힙에 담는다.
    heap = []
    for num in B:
        heapq.heappush(heap, num)

    ans = 0
    for a in A:
        # 이길 수 없는 카드들은 모두 버림
        while heap and heap[0] <= a:
            heapq.heappop(heap)

        if heap and heap[0] > a:
            ans += 1
            heapq.heappop(heap)

    return ans
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.02ms, 10.1MB)
테스트 6 〉	통과 (0.05ms, 10.1MB)
테스트 7 〉	통과 (0.04ms, 10.3MB)
테스트 8 〉	통과 (0.05ms, 10.1MB)
테스트 9 〉	통과 (0.42ms, 10.2MB)
테스트 10 〉	통과 (0.28ms, 10.2MB)
테스트 11 〉	통과 (0.47ms, 10.2MB)
테스트 12 〉	통과 (0.24ms, 10.2MB)
테스트 13 〉	통과 (3.14ms, 10.5MB)
테스트 14 〉	통과 (5.48ms, 10.6MB)
테스트 15 〉	통과 (6.16ms, 10.5MB)
테스트 16 〉	통과 (7.62ms, 10.5MB)
테스트 17 〉	통과 (0.74ms, 10.2MB)
테스트 18 〉	통과 (1.26ms, 10MB)
효율성  테스트
테스트 1 〉	통과 (115.08ms, 18.6MB)
테스트 2 〉	통과 (109.07ms, 18.3MB)
테스트 3 〉	통과 (84.54ms, 18.2MB)
"""
```

#### js (Heap 모듈 사용)

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

function solution(A, B) {
  A = A.sort((a, b) => a - b)

  // 최소 힙 구성
  const heap = new Heap((a, b) => a - b)
  for (const num of B) {
    heap.add(num)
  }

  let ans = 0
  for (const a of A) {
    while (heap.size > 0 && heap.top <= a) {
      heap.extract()
    }

    if (heap.size > 0) {
      ans += 1
      heap.extract()
    }
  }
  return ans
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.29ms, 33.5MB)
// 테스트 2 〉	통과 (0.30ms, 33.4MB)
// 테스트 3 〉	통과 (0.46ms, 33.5MB)
// 테스트 4 〉	통과 (0.28ms, 33.5MB)
// 테스트 5 〉	통과 (0.73ms, 33.6MB)
// 테스트 6 〉	통과 (0.95ms, 33.7MB)
// 테스트 7 〉	통과 (0.85ms, 33.6MB)
// 테스트 8 〉	통과 (0.82ms, 33.6MB)
// 테스트 9 〉	통과 (6.64ms, 36.9MB)
// 테스트 10 〉	통과 (4.67ms, 36.9MB)
// 테스트 11 〉	통과 (5.72ms, 36.9MB)
// 테스트 12 〉	통과 (7.39ms, 36.8MB)
// 테스트 13 〉	통과 (13.75ms, 39MB)
// 테스트 14 〉	통과 (18.95ms, 39.5MB)
// 테스트 15 〉	통과 (14.36ms, 39.2MB)
// 테스트 16 〉	통과 (18.19ms, 39.3MB)
// 테스트 17 〉	통과 (6.12ms, 37MB)
// 테스트 18 〉	통과 (5.83ms, 36.5MB)
// 효율성  테스트
// 테스트 1 〉	통과 (115.92ms, 54MB)
// 테스트 2 〉	통과 (320.73ms, 52.5MB)
// 테스트 3 〉	통과 (94.26ms, 52.9MB)
```

# 접근 3 : 정렬 + 투포인터

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
