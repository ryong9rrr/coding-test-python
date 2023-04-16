> https://school.programmers.co.kr/learn/courses/30/lessons/154538
> related topics : BFS

# 접근 1 : BFS

- 매번 3개의 트리가 생성된다는 점
- 그런 트리 구조를 레벨 순회하면 정답을 구할 수 있다는 점
- 레벨 순회하기 때문에 가장 먼저 정답을 찾으면 그것이 최단거리라고 할 수 있음.

#### python

```python
from collections import deque

def solution(x, y, n):
    if x == y:
        return 0

    def calculate(value):
        return [value + n, value * 2, value * 3]

    visited = set([x])
    q = deque([[x, 0]])
    while q:
        length = len(q)
        for _ in range(length):
            value, level = q.popleft()
            for next_value in calculate(value):
                if next_value in visited or next_value > y:
                    continue
                if next_value == y:
                    return level + 1
                visited.add(next_value)
                q.append([next_value, level + 1])

    return -1
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.4MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (73.95ms, 20.3MB)
테스트 6 〉	통과 (0.00ms, 10.1MB)
테스트 7 〉	통과 (66.93ms, 20.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (445.03ms, 56.1MB)
테스트 10 〉	통과 (328.21ms, 55.6MB)
테스트 11 〉	통과 (133.39ms, 32.8MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.4MB)
테스트 14 〉	통과 (1.68ms, 10.4MB)
테스트 15 〉	통과 (0.14ms, 10.2MB)
테스트 16 〉	통과 (0.65ms, 10.3MB)
"""
```

#### js

Queue 모듈을 사용하지 않고 일반 배열(`shift`)을 사용하면 시간초과로 통과하지 못한다.

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

function solution(x, y, n) {
  if (x === y) {
    return 0
  }

  const calculate = (value) => {
    return [value + n, value * 2, value * 3]
  }

  const visited = new Set([x])
  const q = new Deque()
  q.push([x, 0])

  while (q.length > 0) {
    const qLength = q.length
    for (let i = 0; i < qLength; i += 1) {
      const [value, level] = q.shift()
      for (const nextValue of calculate(value)) {
        if (nextValue > y || visited.has(nextValue)) {
          continue
        }
        if (nextValue === y) {
          return level + 1
        }
        visited.add(nextValue)
        q.push([nextValue, level + 1])
      }
    }
  }
  return -1
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.20ms, 33.6MB)
// 테스트 2 〉	통과 (0.19ms, 33.4MB)
// 테스트 3 〉	통과 (0.19ms, 33.4MB)
// 테스트 4 〉	통과 (0.18ms, 33.5MB)
// 테스트 5 〉	통과 (69.61ms, 55.7MB)
// 테스트 6 〉	통과 (0.08ms, 33.4MB)
// 테스트 7 〉	통과 (55.29ms, 55.7MB)
// 테스트 8 〉	통과 (0.28ms, 33.4MB)
// 테스트 9 〉	통과 (334.66ms, 92.3MB)
// 테스트 10 〉	통과 (253.85ms, 92.3MB)
// 테스트 11 〉	통과 (121.99ms, 70.3MB)
// 테스트 12 〉	통과 (0.20ms, 33.5MB)
// 테스트 13 〉	통과 (0.21ms, 33.4MB)
// 테스트 14 〉	통과 (6.06ms, 36.6MB)
// 테스트 15 〉	통과 (0.62ms, 33.5MB)
// 테스트 16 〉	통과 (2.22ms, 33.9MB)
```

# 접근 2 : 굳이 BFS를 돌리지 않고 집합 자료형만 잘 이용하는 방법

자료형 자체를 바꿔치기 해버리는 방법.. 이런 방식도 일종의 BFS라고 할 수 있으니...

```js
const calculate = (value, n) => {
  return [value + n, value * 2, value * 3]
}

function solution(x, y, n) {
  let sets = new Set([x])
  let level = 0

  while (sets.size > 0) {
    if (sets.has(y)) {
      return level
    }

    const nextSets = new Set()
    for (const value of [...sets]) {
      for (const nextValue of calculate(value, n)) {
        if (nextValue > y) {
          continue
        }
        nextSets.add(nextValue)
      }
    }

    sets = nextSets
    level += 1
  }

  return -1
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.08ms, 33.5MB)
// 테스트 2 〉	통과 (0.08ms, 33.3MB)
// 테스트 3 〉	통과 (0.07ms, 33.3MB)
// 테스트 4 〉	통과 (0.08ms, 33.4MB)
// 테스트 5 〉	통과 (75.85ms, 52.4MB)
// 테스트 6 〉	통과 (0.07ms, 33.5MB)
// 테스트 7 〉	통과 (62.08ms, 52.3MB)
// 테스트 8 〉	통과 (0.08ms, 33.4MB)
// 테스트 9 〉	통과 (330.06ms, 82MB)
// 테스트 10 〉	통과 (492.70ms, 82.2MB)
// 테스트 11 〉	통과 (64.61ms, 52.7MB)
// 테스트 12 〉	통과 (0.08ms, 33.4MB)
// 테스트 13 〉	통과 (0.10ms, 33.4MB)
// 테스트 14 〉	통과 (8.77ms, 37.4MB)
// 테스트 15 〉	통과 (0.35ms, 33.5MB)
// 테스트 16 〉	통과 (0.99ms, 34MB)
```
