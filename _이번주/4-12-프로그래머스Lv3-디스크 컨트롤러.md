> <프로그래머스 문제풀이전략> 참고했다...
> related topics : 정렬, 힙

#### python

```python
from collections import deque
import heapq

def solution(jobs):
    # 큐에는 작업 시작시간이 빠른(작은) 순서로 관리하고
    q = deque(sorted(jobs, key = lambda x:x[0]))
    # 힙에는 수행시간이 짧은(작은) 순으로 관리한다.
    heap = []

    acc = time = 0
    while q or heap:
        while q and q[0][0] <= time:
            start, duration = q.popleft()
            heapq.heappush(heap, [duration, start]) # 수행시간 기준으로 담을 것이므로 반대로

        # 만약 힙이 비어있다면 현재 시간이 q[0]의 작업 시작시간보다 작은 것이므로
        if not heap:
            time = q[0][0]
            continue

        duration, start = heapq.heappop(heap)
        acc += (time + duration - start)
        time += duration

    return acc // len(jobs)
"""
정확성  테스트
테스트 1 〉	통과 (0.65ms, 10.3MB)
테스트 2 〉	통과 (0.41ms, 10.2MB)
테스트 3 〉	통과 (0.35ms, 10.2MB)
테스트 4 〉	통과 (0.52ms, 10.2MB)
테스트 5 〉	통과 (0.57ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (0.57ms, 10.2MB)
테스트 8 〉	통과 (0.33ms, 10.2MB)
테스트 9 〉	통과 (0.15ms, 10.1MB)
테스트 10 〉	통과 (0.57ms, 10.2MB)
테스트 11 〉	통과 (0.03ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.1MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.02ms, 10.1MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.02ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.1MB)
테스트 18 〉	통과 (0.01ms, 10.1MB)
테스트 19 〉	통과 (0.02ms, 10.1MB)
테스트 20 〉	통과 (0.01ms, 10.2MB)
"""
```

#### js (Deque, Heap 모듈 사용)

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

class Node {
  constructor(value, prev = null, next = null) {
    this.value = value
    this.prev = prev
    this.next = next
  }
}

class Deque {
  constructor(array) {
    this._head = null
    this._tail = null
    this._length = 0

    for (const item of array) {
      this.push(item)
    }
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

function solution(jobs) {
  const q = new Deque(jobs.sort((a, b) => a[0] - b[0]))
  const heap = new Heap((a, b) => a[1] - b[1])

  let acc = 0
  let time = 0

  while (q.length > 0 || heap.size > 0) {
    while (q.length > 0 && q.head[0] <= time) {
      const job = q.shift()
      heap.add(job)
    }

    if (heap.size === 0) {
      time = q.head[0]
      continue
    }

    const [start, duration] = heap.extract()
    acc += time + duration - start
    time += duration
  }

  return Math.floor(acc / jobs.length)
}
```
