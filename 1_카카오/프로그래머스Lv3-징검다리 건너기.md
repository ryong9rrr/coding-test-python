> 2019 카카오 개발자 겨울 인턴십
> related topics : 이분탐색(파라메트릭 서치), 슬리이딩 윈도우

힙과 파라메트릭 서치 중에 고민을 많이 했던 문제였다... 그러나 이것은 파라메트릭 서치인 것을 발견!!

# 접근 1 : 이분탐색(파라메트릭 서치) - 시간초과

하지만 시간초과, 가장 긴 0의 길이를 구하는 함수인 `get_longest()` 의 시간복잡도가 크기 때문인 것 같다.

- 시간복잡도 : Nlog(N)

```python
import sys
def solution(stones, k):
    INF = sys.maxsize
    left = INF
    right = -INF
    for stone in stones:
        left = min(left, stone)
        right = max(right, stone)

    def get_longest(value):
        stack = stones[:]
        max_length = 0
        while stack:
            stone = stack.pop()
            stone = max(0, stone - value)
            if stone != 0:
                continue
            length = 1
            while stack and max(0, stack[-1] - value) == 0:
                length += 1
                stack.pop()
            max_length = max(max_length, length)
        return max_length

    while left < right:
        mid = left + ((right - left) // 2)
        longest = get_longest(mid)
        if longest < k:
            left = mid + 1
        else:
            right = mid

    return left

"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.04ms, 10.2MB)
테스트 4 〉	통과 (0.09ms, 10.2MB)
테스트 5 〉	통과 (0.13ms, 10.1MB)
테스트 6 〉	통과 (1.81ms, 10.2MB)
테스트 7 〉	통과 (2.78ms, 10.1MB)
테스트 8 〉	통과 (2.83ms, 10.2MB)
테스트 9 〉	통과 (6.09ms, 10.2MB)
테스트 10 〉	통과 (0.20ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.2MB)
테스트 12 〉	통과 (0.11ms, 10.3MB)
테스트 13 〉	통과 (0.24ms, 10.2MB)
테스트 14 〉	통과 (1.51ms, 10.2MB)
테스트 15 〉	통과 (2.87ms, 10.3MB)
테스트 16 〉	통과 (2.73ms, 10.4MB)
테스트 17 〉	통과 (2.66ms, 10.2MB)
테스트 18 〉	통과 (0.07ms, 10.2MB)
테스트 19 〉	통과 (0.12ms, 10.2MB)
테스트 20 〉	통과 (0.27ms, 10.2MB)
테스트 21 〉	통과 (1.64ms, 10.2MB)
테스트 22 〉	통과 (2.99ms, 10.2MB)
테스트 23 〉	통과 (2.59ms, 10.2MB)
테스트 24 〉	통과 (5.17ms, 10.3MB)
테스트 25 〉	통과 (0.04ms, 10.4MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	실패 (시간 초과)
테스트 10 〉	실패 (시간 초과)
테스트 11 〉	실패 (시간 초과)
테스트 12 〉	실패 (시간 초과)
테스트 13 〉	실패 (시간 초과)
테스트 14 〉	실패 (시간 초과)
"""
```

# 접근 2 : 최적화된 이분탐색(파라메트릭 서치) - 시간초과

진짜 최적화 해줬는데 통과못했다. 사실 이 문제는 슬라이디 윈도우로 O(N) 풀이를 해야 한다고 함...

```python
import sys
def solution(stones, k):
    INF = sys.maxsize
    left = INF
    right = -INF
    for stone in stones:
        left = min(left, stone)
        right = max(right, stone)

    def get_longest(value):
        max_count = 0
        count = 0
        for stone in stones:
            if stone - value <= 0:
                count += 1
                if count == k:
                    return count
            else:
                max_count = max(max_count, count)
                count = 0
        return max_count

    while left < right:
        mid = left + ((right - left) // 2)
        longest = get_longest(mid)
        if longest < k:
            left = mid + 1
        else:
            right = mid

    return left
"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.07ms, 10.2MB)
테스트 5 〉	통과 (0.06ms, 10.2MB)
테스트 6 〉	통과 (1.05ms, 10.2MB)
테스트 7 〉	통과 (1.04ms, 10.1MB)
테스트 8 〉	통과 (2.08ms, 10.3MB)
테스트 9 〉	통과 (0.92ms, 10MB)
테스트 10 〉	통과 (0.07ms, 10.1MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.07ms, 10.1MB)
테스트 13 〉	통과 (0.09ms, 10.2MB)
테스트 14 〉	통과 (0.48ms, 10.2MB)
테스트 15 〉	통과 (1.95ms, 10.1MB)
테스트 16 〉	통과 (0.86ms, 10.2MB)
테스트 17 〉	통과 (1.68ms, 10.3MB)
테스트 18 〉	통과 (0.02ms, 10.1MB)
테스트 19 〉	통과 (0.10ms, 10.2MB)
테스트 20 〉	통과 (0.13ms, 10.1MB)
테스트 21 〉	통과 (1.05ms, 10.2MB)
테스트 22 〉	통과 (1.23ms, 10.3MB)
테스트 23 〉	통과 (0.95ms, 10.2MB)
테스트 24 〉	통과 (1.17ms, 10.2MB)
테스트 25 〉	통과 (0.04ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (361.84ms, 18.6MB)
테스트 2 〉	통과 (430.48ms, 18.5MB)
테스트 3 〉	통과 (378.65ms, 18.5MB)
테스트 4 〉	통과 (594.81ms, 18.5MB)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	통과 (466.27ms, 18.6MB)
테스트 8 〉	통과 (479.88ms, 18.5MB)
테스트 9 〉	통과 (453.99ms, 18.6MB)
테스트 10 〉	통과 (470.26ms, 18.5MB)
테스트 11 〉	통과 (396.96ms, 18.6MB)
테스트 12 〉	통과 (462.96ms, 18.6MB)
테스트 13 〉	통과 (499.42ms, 18.6MB)
테스트 14 〉	통과 (150.63ms, 18.5MB)
"""
```

# 접근 3 : 슬라이딩 윈도우

이 문제는 리트코드 239 - 최대 슬라이딩 윈도우 문제와 비슷한 문제라고 한다...

하지만 슬라이딩 윈도우 풀이도 최적화를 안하면 시간초과.

```python
import sys
def solution(stones, k):
    n = len(stones)
    ans = sys.maxsize
    for i in range(n - k + 1):
        sliding_window = stones[i:i + k]
        ans = min(ans, max(sliding_window))
    return ans
"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10.1MB)
테스트 5 〉	통과 (0.04ms, 10MB)
테스트 6 〉	통과 (0.25ms, 10.2MB)
테스트 7 〉	통과 (1.17ms, 10.2MB)
테스트 8 〉	통과 (1.04ms, 10.1MB)
테스트 9 〉	통과 (1.69ms, 10.1MB)
테스트 10 〉	통과 (0.04ms, 9.97MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.04ms, 10.2MB)
테스트 13 〉	통과 (0.08ms, 10.1MB)
테스트 14 〉	통과 (0.45ms, 10.1MB)
테스트 15 〉	통과 (0.64ms, 10.2MB)
테스트 16 〉	통과 (1.13ms, 10.1MB)
테스트 17 〉	통과 (2.70ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.02ms, 10.3MB)
테스트 20 〉	통과 (0.05ms, 10.2MB)
테스트 21 〉	통과 (0.24ms, 10MB)
테스트 22 〉	통과 (0.64ms, 10.2MB)
테스트 23 〉	통과 (1.03ms, 10MB)
테스트 24 〉	통과 (1.69ms, 10.3MB)
테스트 25 〉	통과 (0.02ms, 10.2MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	실행 중단
테스트 8 〉	실행 중단
테스트 9 〉	실행 중단
테스트 10 〉	실행 중단
테스트 11 〉	실행 중단
테스트 12 〉	실행 중단
테스트 13 〉	실행 중단
테스트 14 〉	실행 중단
"""
```

# 접근 4 : 큐와 스택으로 최적화된 슬라이딩 윈도우

리트코드 239문제와 99% 동일한 문제..

#### python

```python
from collections import deque
import sys

def solution(stones, k):
    ans = sys.maxsize
    slide = deque()
    for i, stone in enumerate(stones):
        if slide and i - slide[0] == k:
            slide.popleft()

        while slide and stones[slide[-1]] <= stone:
            slide.pop()

        slide.append(i)

        # 첫 인덱스부터 순회하므로 처음 슬라이딩 윈도우는 k 사이즈를 갖지 않기 때문에
        # 슬라이딩 윈도우 범위안에서만 갱신하기 위한 조건문
        if k <= i + 1:
            ans = min(ans, stones[slide[0]])

    return ans
```

#### javascript (데크를 쓰지 않으면 시간초과..)

```js
function solution(stones, k) {
  let ans = Infinity
  const slide = []
  for (let i = 0; i < stones.length; i += 1) {
    if (slide.length > 0 && i - slide[0] === k) {
      slide.shift()
    }

    while (slide.length > 0 && stones[slide[slide.length - 1]] <= stones[i]) {
      slide.pop()
    }

    slide.push(i)

    if (k <= i + 1) {
      ans = Math.min(ans, stones[slide[0]])
    }
  }

  return ans
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.05ms, 33.4MB)
// 테스트 2 〉	통과 (0.06ms, 33.6MB)
// 테스트 3 〉	통과 (0.19ms, 33.5MB)
// 테스트 4 〉	통과 (0.16ms, 33.5MB)
// 테스트 5 〉	통과 (0.17ms, 33.4MB)
// 테스트 6 〉	통과 (0.27ms, 33.6MB)
// 테스트 7 〉	통과 (0.35ms, 33.5MB)
// 테스트 8 〉	통과 (0.35ms, 33.6MB)
// 테스트 9 〉	통과 (0.36ms, 33.4MB)
// 테스트 10 〉	통과 (0.17ms, 33.6MB)
// 테스트 11 〉	통과 (0.14ms, 33.6MB)
// 테스트 12 〉	통과 (0.16ms, 33.5MB)
// 테스트 13 〉	통과 (0.16ms, 33.5MB)
// 테스트 14 〉	통과 (0.24ms, 33.5MB)
// 테스트 15 〉	통과 (0.35ms, 33.5MB)
// 테스트 16 〉	통과 (0.34ms, 33.5MB)
// 테스트 17 〉	통과 (0.34ms, 33.5MB)
// 테스트 18 〉	통과 (0.21ms, 33.5MB)
// 테스트 19 〉	통과 (0.15ms, 33.5MB)
// 테스트 20 〉	통과 (0.17ms, 33.5MB)
// 테스트 21 〉	통과 (0.31ms, 33.4MB)
// 테스트 22 〉	통과 (0.35ms, 33.6MB)
// 테스트 23 〉	통과 (0.36ms, 33.6MB)
// 테스트 24 〉	통과 (0.36ms, 33.5MB)
// 테스트 25 〉	통과 (0.15ms, 33.5MB)
// 효율성  테스트
// 테스트 1 〉	통과 (12.39ms, 40.9MB)
// 테스트 2 〉	통과 (10.37ms, 40.9MB)
// 테스트 3 〉	통과 (11.36ms, 41MB)
// 테스트 4 〉	통과 (10.61ms, 40.9MB)
// 테스트 5 〉	통과 (13.64ms, 40.9MB)
// 테스트 6 〉	통과 (10.25ms, 40.9MB)
// 테스트 7 〉	통과 (9.75ms, 41.2MB)
// 테스트 8 〉	통과 (12.15ms, 40.9MB)
// 테스트 9 〉	통과 (12.22ms, 40.9MB)
// 테스트 10 〉	통과 (12.13ms, 40.9MB)
// 테스트 11 〉	통과 (11.18ms, 40.9MB)
// 테스트 12 〉	통과 (9.29ms, 41MB)
// 테스트 13 〉	실패 (시간 초과)
// 테스트 14 〉	통과 (7.71ms, 42.7MB)
```

#### javascript : deque 자료구조 구현

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

  get size() {
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

function solution(stones, k) {
  let ans = Infinity
  const slide = new Deque()
  for (let i = 0; i < stones.length; i += 1) {
    if (slide.size > 0 && i - slide.head === k) {
      slide.shift()
    }

    while (slide.size > 0 && stones[slide.tail] <= stones[i]) {
      slide.pop()
    }

    slide.push(i)

    if (k <= i + 1) {
      ans = Math.min(ans, stones[slide.head])
    }
  }

  return ans
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.13ms, 33.4MB)
// 테스트 2 〉	통과 (0.15ms, 33.5MB)
// 테스트 3 〉	통과 (0.27ms, 33.4MB)
// 테스트 4 〉	통과 (0.31ms, 33.5MB)
// 테스트 5 〉	통과 (0.37ms, 33.4MB)
// 테스트 6 〉	통과 (0.59ms, 33.4MB)
// 테스트 7 〉	통과 (0.85ms, 33.6MB)
// 테스트 8 〉	통과 (0.89ms, 33.7MB)
// 테스트 9 〉	통과 (1.14ms, 33.5MB)
// 테스트 10 〉	통과 (0.36ms, 33.4MB)
// 테스트 11 〉	통과 (0.29ms, 33.5MB)
// 테스트 12 〉	통과 (0.33ms, 33.4MB)
// 테스트 13 〉	통과 (0.36ms, 33.6MB)
// 테스트 14 〉	통과 (0.66ms, 33.5MB)
// 테스트 15 〉	통과 (1.25ms, 33.5MB)
// 테스트 16 〉	통과 (0.90ms, 33.5MB)
// 테스트 17 〉	통과 (1.17ms, 33.6MB)
// 테스트 18 〉	통과 (0.46ms, 33.5MB)
// 테스트 19 〉	통과 (0.31ms, 33.5MB)
// 테스트 20 〉	통과 (0.58ms, 33.5MB)
// 테스트 21 〉	통과 (0.58ms, 33.5MB)
// 테스트 22 〉	통과 (0.86ms, 33.6MB)
// 테스트 23 〉	통과 (0.90ms, 33.5MB)
// 테스트 24 〉	통과 (1.26ms, 33.6MB)
// 테스트 25 〉	통과 (0.53ms, 33.5MB)
// 효율성  테스트
// 테스트 1 〉	통과 (25.91ms, 42.7MB)
// 테스트 2 〉	통과 (18.17ms, 42.8MB)
// 테스트 3 〉	통과 (28.31ms, 42.9MB)
// 테스트 4 〉	통과 (25.00ms, 42.9MB)
// 테스트 5 〉	통과 (28.95ms, 42.8MB)
// 테스트 6 〉	통과 (24.49ms, 42.8MB)
// 테스트 7 〉	통과 (23.59ms, 42.9MB)
// 테스트 8 〉	통과 (25.10ms, 43MB)
// 테스트 9 〉	통과 (27.33ms, 42.8MB)
// 테스트 10 〉	통과 (27.90ms, 42.9MB)
// 테스트 11 〉	통과 (28.06ms, 42.8MB)
// 테스트 12 〉	통과 (21.06ms, 42.8MB)
// 테스트 13 〉	통과 (35.93ms, 54.1MB)
// 테스트 14 〉	통과 (18.06ms, 44.1MB)
```
