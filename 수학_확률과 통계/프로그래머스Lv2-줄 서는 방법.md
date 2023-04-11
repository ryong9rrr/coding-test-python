> related topics : 순열과 조합, DFS, 수학

이 문제는 파이썬의 `itertools`를 사용하면, 어떻게 하든 효율성 테스트에서 시간초과가 걸린다.

## 접근 1 : 순열, 처음부터 모든 순열을 만드는 경우 (시간초과)

```python
from itertools import permutations
def solution(n, k):
    nums = [num for num in range(1, n + 1)]
    combis = permutations(nums, n)
    i = 1
    for combi in combis:
        if i == k:
            return combi
        i += 1
"""
정확성  테스트
테스트 1 〉	통과 (0.08ms, 10MB)
테스트 2 〉	통과 (13.22ms, 10.2MB)
테스트 3 〉	통과 (5.69ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 9.98MB)
테스트 7 〉	통과 (0.60ms, 10MB)
테스트 8 〉	통과 (0.05ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (172.09ms, 10.3MB)
테스트 11 〉	통과 (271.08ms, 10MB)
테스트 12 〉	통과 (355.87ms, 10.2MB)
테스트 13 〉	통과 (628.26ms, 10.1MB)
테스트 14 〉	통과 (0.08ms, 10.2MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
"""
```

## 접근 2 : 순열을 생성하는 DFS (시간초과)

즉 처음부터 모든 순열을 만들지말고 dfs로 순열을 만들면서 `k`번째 순열을 리턴시키는 방식, 그러나 이것도 시간초과

#### javascript

```js
function permute(array, k, limit) {
  if (k > array.length) return null
  const results = []
  const prevElements = []
  function dfs(elements, k, l) {
    if (results.length === l) {
      return
    }
    if (k === 0) {
      results.push([...prevElements])
      return
    }

    for (let i = 0; i < elements.length; i++) {
      const nextElements = [...elements]
      nextElements.splice(i, 1)

      prevElements.push(elements[i])
      dfs(nextElements, k - 1, l)
      prevElements.pop()
    }
  }
  dfs(array, k, limit)
  return results
}

function solution(n, k) {
  const nums = Array.from({ length: n }, (v, i) => i + 1)
  const permutations = permute(nums, n, k)
  return permutations[k - 1]
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.54ms, 33.7MB)
// 테스트 2 〉	통과 (106.71ms, 71.2MB)
// 테스트 3 〉	통과 (34.19ms, 59MB)
// 테스트 4 〉	통과 (0.44ms, 33.5MB)
// 테스트 5 〉	통과 (0.21ms, 33.5MB)
// 테스트 6 〉	통과 (0.32ms, 33.5MB)
// 테스트 7 〉	통과 (5.78ms, 38.1MB)
// 테스트 8 〉	통과 (0.43ms, 33.5MB)
// 테스트 9 〉	통과 (0.29ms, 33.3MB)
// 테스트 10 〉	통과 (1743.52ms, 327MB)
// 테스트 11 〉	통과 (2348.21ms, 451MB)
// 테스트 12 〉	통과 (2835.47ms, 617MB)
// 테스트 13 〉	실패 (signal: aborted (core dumped))
// 테스트 14 〉	통과 (0.66ms, 33.7MB)
// 효율성  테스트
// 테스트 1 〉	실패 (시간 초과)
// 테스트 2 〉	실패 (시간 초과)
// 테스트 3 〉	실패 (시간 초과)
// 테스트 4 〉	실패 (시간 초과)
// 테스트 5 〉	실패 (시간 초과)
```

## 접근 3 : 수학적으로 규칙찾기

이건 규칙을 찾는 문제였다..

내가 처음 접근한 풀이

#### javascript

```js
function divmod(n, k) {
  const a = Math.floor(n / k)
  const b = n % k
  return [a, b]
}

function makeFactorials(n) {
  const dp = [1, 1]
  for (let i = 2; i <= n; i += 1) {
    dp.push(i * dp[i - 1])
  }
  return dp
}

function solution(n, k) {
  const numbers = Array.from({ length: n }, (v, i) => i + 1)
  const factorials = makeFactorials(n)
  const result = []

  for (let i = 1; i <= n; i += 1) {
    const [a, b] = divmod(k, factorials[n - i])
    if (b === 0) {
      result.push(numbers[a - 1])
      numbers.splice(a - 1, 1)
      k = factorials[n - i]
      continue
    }
    result.push(numbers[a])
    numbers.splice(a, 1)
    k = b
  }

  return result
}
```

자바스크립트 `splice`를 좀 더 활용하고, `k`가 아니라 `k - 1`에서 나누는 식으로 더 스마트하게 할 수 있음.

```js
function makeFactorials(n) {
  const dp = [1, 1]
  for (let i = 2; i <= n; i += 1) {
    dp.push(i * dp[i - 1])
  }
  return dp
}

function solution(n, k) {
  const numbers = Array.from({ length: n }, (v, i) => i + 1)
  const factorials = makeFactorials(n)
  const result = []

  for (let i = 1; i <= n; i += 1) {
    const a = Math.floor((k - 1) / factorials[n - i])
    const b = k % factorials[n - i]
    const [number] = numbers.splice(a, 1)
    result.push(number)
    k = b
  }

  return result
}
```

#### python

`pop` 메서드에 `index`를 넣을 수도 있음.

```python
def make_factorials(n):
    dp = [1, 1]
    for i in range(2, n + 1):
        dp.append(i * dp[i - 1])
    return dp

def solution(n, k):
    numbers = [num for num in range(1, n + 1)]
    factorials = make_factorials(n)
    result = []

    for i in range(1, n + 1):
        index = (k - 1) // factorials[n - i]
        result.append(numbers.pop(index))
        k = k % factorials[n - i]

    return result
```
