> 2022 8월 프로그래머스 모의테스트 1회 3번문제
> related topics : 큐, 스택

# 접근 : 큐 + 스택

1부터 n까지 순서대로 오는 컨베이어 박스를 '큐'라고 생각할 수도 있고, 굳이 큐로 두지 않고 번호를 증가시키는 식으로 구현할 수도 있다.

## 굳이 큐를 사용하지 않고, 스택과 인덱스 번호만으로 풀이(약간 포인터 방식)

#### python

```python
def solution(order):
    n = len(order)
    stack = []
    ans = 0

    box_number = 1
    order_index = 0
    while box_number <= n and order_index < n:
        # 바로 트럭에 싣을 수 있다면 싣는다.
        if box_number == order[order_index]:
            ans += 1
            order_index += 1
        # 그렇지 않다면 임시 컨베이어(스택)에 싣는다.
        else:
            stack.append(box_number)
        box_number += 1

        # 임시 컨테이어(스택) 처리
        while order_index < n and stack and stack[-1] == order[order_index]:
            stack.pop()
            ans += 1
            order_index += 1

    return ans
"""
정확성  테스트
테스트 1 〉	통과 (26.50ms, 19.2MB)
테스트 2 〉	통과 (113.05ms, 52.7MB)
테스트 3 〉	통과 (146.79ms, 66.4MB)
테스트 4 〉	통과 (124.97ms, 46.2MB)
테스트 5 〉	통과 (234.14ms, 94.5MB)
테스트 6 〉	통과 (56.44ms, 18.9MB)
테스트 7 〉	통과 (215.06ms, 46.5MB)
테스트 8 〉	통과 (11.79ms, 12MB)
테스트 9 〉	통과 (170.81ms, 35.2MB)
테스트 10 〉	통과 (286.04ms, 52.9MB)
"""
```

#### javascript

```js
function solution(order) {
  const n = order.length
  const stack = []
  let orderIndex = 0
  let boxNumber = 1
  let ans = 0

  while (orderIndex < n && boxNumber <= n) {
    if (order[orderIndex] === boxNumber) {
      ans += 1
      orderIndex += 1
    } else {
      stack.push(boxNumber)
    }
    boxNumber += 1

    while (
      orderIndex < n &&
      stack.length > 0 &&
      stack[stack.length - 1] === order[orderIndex]
    ) {
      stack.pop()
      ans += 1
      orderIndex += 1
    }
  }

  return ans
}
// 정확성  테스트
// 테스트 1 〉	통과 (30.89ms, 42.3MB)
// 테스트 2 〉	통과 (18.46ms, 56MB)
// 테스트 3 〉	통과 (21.58ms, 74MB)
// 테스트 4 〉	통과 (16.64ms, 62.4MB)
// 테스트 5 〉	통과 (30.66ms, 92.6MB)
// 테스트 6 〉	통과 (5.14ms, 40.9MB)
// 테스트 7 〉	통과 (13.44ms, 68.4MB)
// 테스트 8 〉	통과 (3.28ms, 38.7MB)
// 테스트 9 〉	통과 (10.69ms, 57MB)
// 테스트 10 〉	통과 (14.15ms, 75.2MB)
```

## 큐를 사용하면 조금 더 이해하기 쉬워 보이기도 한다.

```python
from collections import deque
def solution(order):
    n = len(order)
    boxes = deque([i + 1 for i in range(n)])
    stack = []
    ans = 0
    order_index = 0
    while boxes and order_index < n:
        box = boxes.popleft() # 일단 바로 큐에서 하나 빼줌
        if box == order[order_index]:
            ans += 1
            order_index += 1
        else:
            stack.append(box)

        # 임시 컨테이어(스택) 처리
        while order_index < n and stack and stack[-1] == order[order_index]:
            stack.pop()
            ans += 1
            order_index += 1

    return ans

"""
정확성  테스트
테스트 1 〉	통과 (31.61ms, 19.7MB)
테스트 2 〉	통과 (137.02ms, 53.4MB)
테스트 3 〉	통과 (181.05ms, 66.4MB)
테스트 4 〉	통과 (123.24ms, 50MB)
테스트 5 〉	통과 (295.65ms, 95.3MB)
테스트 6 〉	통과 (71.37ms, 28.4MB)
테스트 7 〉	통과 (301.31ms, 82.2MB)
테스트 8 〉	통과 (15.44ms, 13.7MB)
테스트 9 〉	통과 (191.74ms, 59.8MB)
테스트 10 〉	통과 (328.63ms, 95.1MB)
"""
```
