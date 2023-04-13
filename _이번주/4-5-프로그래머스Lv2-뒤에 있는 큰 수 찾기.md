# 프로그래머스 Lv2 : 뒤에 있는 큰 수 찾기

> related topics : 배열, 스택

## 접근 1 : DP + 재귀

나의 풀이... 유니온 파인드의 `find()` 함수처럼, 재귀적으로 DP 테이블을 갱신하는 방법

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

## 접근 2 : 스택

근데 그냥 스택으로도 풀 수 있다...(시간도 훨씬 빠름) 사람들 대부분 이렇게 풀었는데 왜 이런 생각을 못했지...

#### python

```python
def solution(numbers):
    n = len(numbers)
    result = [-1] * n
    stack = []
    for i in range(n):
        while stack and numbers[stack[-1]] < numbers[i]:
            result[stack.pop()] = numbers[i]
        stack.append(i)

    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (0.29ms, 10.3MB)
테스트 6 〉	통과 (2.88ms, 11.4MB)
테스트 7 〉	통과 (2.72ms, 11.3MB)
테스트 8 〉	통과 (14.82ms, 17.2MB)
테스트 9 〉	통과 (14.47ms, 17MB)
테스트 10 〉	통과 (28.58ms, 19.7MB)
테스트 11 〉	통과 (26.66ms, 19.7MB)
테스트 12 〉	통과 (57.06ms, 25.3MB)
테스트 13 〉	통과 (53.28ms, 25.4MB)
테스트 14 〉	통과 (134.46ms, 43.3MB)
테스트 15 〉	통과 (262.61ms, 75.4MB)
테스트 16 〉	통과 (285.94ms, 75.4MB)
테스트 17 〉	통과 (281.92ms, 75.4MB)
테스트 18 〉	통과 (267.79ms, 75.4MB)
테스트 19 〉	통과 (274.33ms, 75.5MB)
테스트 20 〉	통과 (396.46ms, 74.8MB)
테스트 21 〉	통과 (195.01ms, 110MB)
테스트 22 〉	통과 (225.06ms, 45.6MB)
테스트 23 〉	통과 (155.85ms, 106MB)
"""
```

#### js

```js
function solution(numbers) {
  const n = numbers.length
  const result = new Array(n).fill(-1)
  const stack = []
  for (let i = 0; i < n; i += 1) {
    while (stack.length > 0 && numbers[stack[stack.length - 1]] < numbers[i]) {
      result[stack.pop()] = numbers[i]
    }
    stack.push(i)
  }
  return result
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.05ms, 33.5MB)
// 테스트 2 〉	통과 (0.05ms, 33.5MB)
// 테스트 3 〉	통과 (0.12ms, 33.6MB)
// 테스트 4 〉	통과 (0.17ms, 33.5MB)
// 테스트 5 〉	통과 (0.29ms, 33.7MB)
// 테스트 6 〉	통과 (2.96ms, 38.4MB)
// 테스트 7 〉	통과 (3.14ms, 38.2MB)
// 테스트 8 〉	통과 (3.83ms, 42.6MB)
// 테스트 9 〉	통과 (4.44ms, 42.7MB)
// 테스트 10 〉	통과 (4.96ms, 44.9MB)
// 테스트 11 〉	통과 (6.93ms, 44.9MB)
// 테스트 12 〉	통과 (7.32ms, 52.2MB)
// 테스트 13 〉	통과 (10.07ms, 52.2MB)
// 테스트 14 〉	통과 (15.14ms, 79MB)
// 테스트 15 〉	통과 (31.17ms, 126MB)
// 테스트 16 〉	통과 (27.29ms, 126MB)
// 테스트 17 〉	통과 (25.42ms, 126MB)
// 테스트 18 〉	통과 (26.40ms, 126MB)
// 테스트 19 〉	통과 (24.46ms, 126MB)
// 테스트 20 〉	통과 (45.61ms, 160MB)
// 테스트 21 〉	통과 (41.02ms, 152MB)
// 테스트 22 〉	통과 (27.33ms, 108MB)
// 테스트 23 〉	통과 (40.83ms, 149MB)
```
