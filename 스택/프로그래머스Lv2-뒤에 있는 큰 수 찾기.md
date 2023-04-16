> https://school.programmers.co.kr/learn/courses/30/lessons/154539
> related topics : 배열, 스택

# 접근 1 : 브루트포스 (시간초과)

가장 직관적인 방법...

#### python

```python
def solution(numbers):
    n = len(numbers)

    result = []
    for i in range(n):
        number = -1
        for j in range(i + 1, n):
            if numbers[i] < numbers[j]:
                number = numbers[j]
                break
        result.append(number)

    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.05ms, 10.1MB)
테스트 5 〉	통과 (0.79ms, 10.4MB)
테스트 6 〉	통과 (9.45ms, 11.3MB)
테스트 7 〉	통과 (9.05ms, 11.4MB)
테스트 8 〉	통과 (53.58ms, 16.6MB)
테스트 9 〉	통과 (66.60ms, 16.7MB)
테스트 10 〉	통과 (128.39ms, 19.5MB)
테스트 11 〉	통과 (158.02ms, 19.5MB)
테스트 12 〉	통과 (300.18ms, 25.4MB)
테스트 13 〉	통과 (340.64ms, 25.3MB)
테스트 14 〉	통과 (1313.21ms, 43.2MB)
테스트 15 〉	통과 (3822.42ms, 75.5MB)
테스트 16 〉	통과 (4379.87ms, 75.4MB)
테스트 17 〉	통과 (4397.48ms, 75.3MB)
테스트 18 〉	통과 (3791.14ms, 75.4MB)
테스트 19 〉	통과 (3333.18ms, 75.4MB)
테스트 20 〉	실패 (시간 초과)
테스트 21 〉	실패 (시간 초과)
테스트 22 〉	실패 (시간 초과)
테스트 23 〉	실행 중단
"""
```

## 접근 2 : DP + 재귀

내가 처음 푼 풀이... 유니온 파인드의 `find()` 함수처럼, 재귀적으로 DP 테이블을 갱신하는 방법

#### python

```python
def solution(numbers):
    n = len(numbers)
    dp = [-1] * n

    def find(number, index):
        if index >= n:
            return -1
        if dp[index] == -1:
            return -1
        if number < numbers[dp[index]]:
            return dp[index]
        return find(number, dp[index])

    for i in range(n - 2, -1, -1):
        if numbers[i] < numbers[i + 1]:
            dp[i] = i + 1
            continue
        dp[i] = find(numbers[i], i + 1)

    return [-1 if index == -1 else numbers[index] for index in dp]
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.05ms, 10.2MB)
테스트 5 〉	통과 (0.62ms, 10.3MB)
테스트 6 〉	통과 (4.34ms, 11.5MB)
테스트 7 〉	통과 (3.71ms, 11.5MB)
테스트 8 〉	통과 (28.19ms, 18MB)
테스트 9 〉	통과 (23.42ms, 17.9MB)
테스트 10 〉	통과 (47.56ms, 22.3MB)
테스트 11 〉	통과 (42.61ms, 22.2MB)
테스트 12 〉	통과 (79.77ms, 30.2MB)
테스트 13 〉	통과 (81.02ms, 30.3MB)
테스트 14 〉	통과 (217.99ms, 55MB)
테스트 15 〉	통과 (434.03ms, 98.5MB)
테스트 16 〉	통과 (391.37ms, 98.6MB)
테스트 17 〉	통과 (383.50ms, 98.5MB)
테스트 18 〉	통과 (710.13ms, 98.7MB)
테스트 19 〉	통과 (472.83ms, 98.7MB)
테스트 20 〉	통과 (520.93ms, 59.6MB)
테스트 21 〉	통과 (302.26ms, 81.8MB)
테스트 22 〉	통과 (354.98ms, 58.5MB)
테스트 23 〉	통과 (381.41ms, 79.9MB)
"""
```

#### javascript

```js
function solution(numbers) {
  const n = numbers.length
  const dp = new Array(n).fill(-1)

  const find = (number, index) => {
    if (index >= n) {
      return -1
    }
    if (dp[index] === -1) {
      return -1
    }
    if (number < numbers[dp[index]]) {
      return dp[index]
    }
    return find(number, dp[index])
  }

  for (let i = n - 2; i >= 0; i -= 1) {
    if (numbers[i] < numbers[i + 1]) {
      dp[i] = i + 1
      continue
    }
    dp[i] = find(numbers[i], i + 1)
  }

  return dp.map((index) => {
    if (index === -1) {
      return -1
    }
    return numbers[index]
  })
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.07ms, 33.5MB)
// 테스트 2 〉	통과 (0.09ms, 33.5MB)
// 테스트 3 〉	통과 (0.08ms, 33.5MB)
// 테스트 4 〉	통과 (0.20ms, 33.5MB)
// 테스트 5 〉	통과 (0.37ms, 33.8MB)
// 테스트 6 〉	통과 (3.96ms, 36.8MB)
// 테스트 7 〉	통과 (3.97ms, 36.8MB)
// 테스트 8 〉	통과 (6.09ms, 43.2MB)
// 테스트 9 〉	통과 (6.49ms, 42MB)
// 테스트 10 〉	통과 (8.85ms, 45.6MB)
// 테스트 11 〉	통과 (8.85ms, 45.7MB)
// 테스트 12 〉	통과 (13.29ms, 53.1MB)
// 테스트 13 〉	통과 (13.06ms, 53.3MB)
// 테스트 14 〉	통과 (28.25ms, 79.7MB)
// 테스트 15 〉	통과 (46.27ms, 137MB)
// 테스트 16 〉	통과 (46.93ms, 137MB)
// 테스트 17 〉	통과 (50.13ms, 137MB)
// 테스트 18 〉	통과 (51.72ms, 137MB)
// 테스트 19 〉	통과 (51.64ms, 137MB)
// 테스트 20 〉	통과 (34.82ms, 137MB)
// 테스트 21 〉	통과 (36.10ms, 134MB)
// 테스트 22 〉	통과 (32.19ms, 106MB)
// 테스트 23 〉	통과 (34.52ms, 130MB)
```

## 접근 3 : 스택

하지만 이 문제는 전형적인 "스택" 문제이다.

#### python

```python
def solution(numbers):
    n = len(numbers)
    stack = []
    result = []
    for i in range(n - 1, -1, -1):
        cur = numbers[i]
        while stack and stack[-1] <= cur:
            stack.pop()
        value = -1 if not stack else stack[-1]
        result.append(value)
        stack.append(cur)

    return result[::-1]
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.04ms, 10.2MB)
테스트 5 〉	통과 (0.56ms, 10.3MB)
테스트 6 〉	통과 (2.73ms, 11.5MB)
테스트 7 〉	통과 (2.87ms, 11.4MB)
테스트 8 〉	통과 (15.72ms, 17.1MB)
테스트 9 〉	통과 (14.57ms, 17.1MB)
테스트 10 〉	통과 (29.31ms, 19.9MB)
테스트 11 〉	통과 (33.38ms, 19.9MB)
테스트 12 〉	통과 (62.00ms, 25.6MB)
테스트 13 〉	통과 (58.34ms, 25.5MB)
테스트 14 〉	통과 (140.41ms, 43.2MB)
테스트 15 〉	통과 (334.17ms, 75.5MB)
테스트 16 〉	통과 (279.46ms, 77.2MB)
테스트 17 〉	통과 (299.76ms, 77.2MB)
테스트 18 〉	통과 (297.59ms, 75.5MB)
테스트 19 〉	통과 (302.59ms, 75.8MB)
테스트 20 〉	통과 (255.56ms, 51MB)
테스트 21 〉	통과 (280.69ms, 72.3MB)
테스트 22 〉	통과 (211.48ms, 38.4MB)
테스트 23 〉	통과 (265.72ms, 75.1MB)
"""
```

#### js

```js
function solution(numbers) {
  const n = numbers.length
  const stack = []
  const result = []

  for (let i = n - 1; i >= 0; i -= 1) {
    const cur = numbers[i]
    while (stack.length > 0 && stack[stack.length - 1] <= cur) {
      stack.pop()
    }

    const value = stack.length > 0 ? stack[stack.length - 1] : -1
    result.push(value)

    stack.push(cur)
  }

  return [...result].reverse()
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.05ms, 33.5MB)
// 테스트 2 〉	통과 (0.05ms, 33.5MB)
// 테스트 3 〉	통과 (0.13ms, 33.5MB)
// 테스트 4 〉	통과 (0.27ms, 33.4MB)
// 테스트 5 〉	통과 (0.31ms, 33.6MB)
// 테스트 6 〉	통과 (3.61ms, 37.9MB)
// 테스트 7 〉	통과 (23.67ms, 37.9MB)
// 테스트 8 〉	통과 (4.92ms, 42.3MB)
// 테스트 9 〉	통과 (25.10ms, 42.7MB)
// 테스트 10 〉	통과 (6.72ms, 46.9MB)
// 테스트 11 〉	통과 (7.46ms, 47MB)
// 테스트 12 〉	통과 (11.47ms, 59.1MB)
// 테스트 13 〉	통과 (12.08ms, 58.9MB)
// 테스트 14 〉	통과 (23.85ms, 74.9MB)
// 테스트 15 〉	통과 (49.69ms, 148MB)
// 테스트 16 〉	통과 (49.93ms, 149MB)
// 테스트 17 〉	통과 (53.26ms, 148MB)
// 테스트 18 〉	통과 (52.01ms, 148MB)
// 테스트 19 〉	통과 (58.42ms, 148MB)
// 테스트 20 〉	통과 (49.87ms, 151MB)
// 테스트 21 〉	통과 (43.77ms, 147MB)
// 테스트 22 〉	통과 (30.68ms, 110MB)
// 테스트 23 〉	통과 (42.58ms, 144MB)
```
