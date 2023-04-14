> related topics : 스택, 배열

두 개의 배열이 주어질 때, push, pop 메서드로 두 배열의 순서를 맞출 수 있는지 없는지 반환하는 문제.

이런 단순한 류의 문제가 코딩테스트 1~2번에 자주 나올만한데, 은근 까다로운 문제같다..

# 접근 1 : 두 개의 큐 + 스택

내가 푼 풀이. 하지만 이렇게 두 개의 큐를 그대로 쓰는 것은 배열의 인덱스를 잘 사용하는 것으로도 풀 수 있다.

#### python

```python
# 76ms(42%), 14MB(85%)
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        push_q = collections.deque(pushed)
        pop_q = collections.deque(popped)

        stack = []

        while push_q and pop_q:
            if push_q[0] == pop_q[0]:
                push_q.popleft()
                pop_q.popleft()
            else:
                stack.append(push_q.popleft())

            while stack and pop_q and stack[-1] == pop_q[0]:
                stack.pop()
                pop_q.popleft()

        return not stack and not push_q and not pop_q
```

# 접근 2 : 스택 + 배열 포인터

리트코드 솔루션의 접근.. 확실히 더 스마트해보인다.

#### python

```python
# 67ms(90%), 14MB(85%)
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        popped_index = 0
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and popped_index < n and stack[-1] == popped[popped_index]:
                stack.pop()
                popped_index += 1

        return popped_index == n
```

#### js

```js
// 61ms(81%), 44.4MB(30%)
/**
 * @param {number[]} pushed
 * @param {number[]} popped
 * @return {boolean}
 */
var validateStackSequences = function (pushed, popped) {
  const n = pushed.length
  const stack = []
  let poppedIndex = 0
  for (const num of pushed) {
    stack.push(num)
    while (
      stack.length > 0 &&
      poppedIndex < n &&
      stack[stack.length - 1] === popped[poppedIndex]
    ) {
      stack.pop()
      poppedIndex += 1
    }
  }

  return poppedIndex === n
}
```
