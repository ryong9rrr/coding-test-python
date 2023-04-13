> related topics : DP, DFS, BFS

DP + DFS 로 풀이할 수도 있지만, BFS가 더 효율적인 방법.

이유는 다음과 같다.

- 매번 3개의 트리가 생성된다는 점
- 그런 트리 구조를 레벨 순회하면 정답을 구할 수 있다는 점
- 레벨 순회하기 때문에 가장 먼저 정답을 찾으면 그것이 최단거리라고 할 수 있음.

따라서 다음과 같이 일반적인 재귀로 접근하면 시간초과가 난다.

```python
import sys
sys.setrecursionlimit(10**6)

def solution(x, y, n):
    INF = int(1e9)
    ans = INF

    def calculate(number, count):
        nonlocal ans
        if number > y:
            return
        if number == y:
            ans = min(ans, count)
            return
        if ans < count:
            return
        calculate(number + n, count + 1)
        calculate(number * 2, count + 1)
        calculate(number * 3, count + 1)

    calculate(x, 0)

    return -1 if ans == INF else ans
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	실패 (런타임 에러)
테스트 10 〉	실패 (런타임 에러)
테스트 11 〉	실패 (시간 초과)
테스트 12 〉	통과 (0.00ms, 10.1MB)
테스트 13 〉	통과 (0.00ms, 10.1MB)
테스트 14 〉	실패 (시간 초과)
테스트 15 〉	실행 중단
테스트 16 〉	실행 중단
"""
```

## 접근 : BFS

#### python

```python
from collections import deque
def solution(x, y, n):
    if x == y:
        return 0

    def calculate(number):
        return [number + n, number * 2, number * 3]

    visited = set([x])
    q = deque([[x, 0]])
    while q:
        size = len(q)
        for _ in range(size):
            number, count = q.popleft()
            if number > y:
                continue
            for next_number in calculate(number):
                if next_number == y:
                    return count + 1
                if next_number not in visited and next_number < y:
                    visited.add(next_number)
                    q.append([next_number, count + 1])

    return -1
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.4MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.4MB)
테스트 5 〉	통과 (79.77ms, 20.3MB)
테스트 6 〉	통과 (0.00ms, 10.4MB)
테스트 7 〉	통과 (64.09ms, 20.1MB)
테스트 8 〉	통과 (0.01ms, 10.4MB)
테스트 9 〉	통과 (314.39ms, 56.2MB)
테스트 10 〉	통과 (248.04ms, 55.6MB)
테스트 11 〉	통과 (116.58ms, 32.7MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (3.31ms, 10.4MB)
테스트 15 〉	통과 (0.27ms, 10.2MB)
테스트 16 〉	통과 (0.69ms, 10.3MB)
"""
```

#### js

Queue 모듈을 사용하지 않고 일반 배열(`shift`)을 사용하면 시간초과로 통과하지 못한다.

```js
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

function solution(x, y, n) {
  if (x === y) {
    return 0
  }

  const calculate = (number) => {
    return [number + n, number * 2, number * 3]
  }

  const visited = new Set([x])
  const q = new MyQueue([[x, 0]])
  while (q.size > 0) {
    const size = q.size
    for (let i = 0; i < size; i += 1) {
      const [number, count] = q.dequeue()
      if (number > y) {
        continue
      }
      for (const nextNumber of calculate(number)) {
        if (nextNumber === y) {
          return count + 1
        }
        if (!visited.has(nextNumber) && nextNumber < y) {
          visited.add(nextNumber)
          q.enqueue([nextNumber, count + 1])
        }
      }
    }
  }
  return -1
}
```
