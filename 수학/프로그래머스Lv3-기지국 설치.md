> related topics : 그리디, 포인터, 수학

어려운 문제였다. 나중에 다시 풀어보자 ㅜㅜ

# 접근 1 : 그리디 + 포인터

기지국의 위치 `loc`을 계속 변경해주는 풀이..

#### python

```python
def solution(n, stations, w):
    loc = 1
    stations_index = 0

    ans = 0
    while loc <= n:
        if stations_index < len(stations) and loc >= stations[stations_index] - w:
            loc = stations[stations_index] + w + 1
            stations_index += 1
        else:
            ans += 1
            loc += 2 * w + 1

    return ans
```

#### js

이렇게 상수로 사용안해주면 효율성에서 시간초과가 나더라..;;

```js
function solution(n, stations, w) {
  const stationsLength = stations.length
  const interval = 2 * w + 1
  let loc = 1
  let stationsIndex = 0
  let ans = 0
  while (loc <= n) {
    if (stationsIndex < stationsLength && loc >= stations[stationsIndex] - w) {
      loc = stations[stationsIndex] + w + 1
      stationsIndex += 1
    } else {
      ans += 1
      loc += interval
    }
  }
  return ans
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.06ms, 33.4MB)
// 테스트 2 〉	통과 (0.06ms, 33.6MB)
// 테스트 3 〉	통과 (0.05ms, 33.4MB)
// 테스트 4 〉	통과 (0.06ms, 33.5MB)
// 테스트 5 〉	통과 (0.07ms, 33.5MB)
// 테스트 6 〉	통과 (0.06ms, 33.5MB)
// 테스트 7 〉	통과 (0.04ms, 33.5MB)
// 테스트 8 〉	통과 (0.04ms, 33.5MB)
// 테스트 9 〉	통과 (0.04ms, 33.5MB)
// 테스트 10 〉	통과 (0.04ms, 33.5MB)
// 테스트 11 〉	통과 (0.07ms, 33.5MB)
// 테스트 12 〉	통과 (0.06ms, 33.4MB)
// 테스트 13 〉	통과 (0.08ms, 33.6MB)
// 테스트 14 〉	통과 (0.07ms, 33.6MB)
// 테스트 15 〉	통과 (0.07ms, 33.6MB)
// 테스트 16 〉	통과 (0.05ms, 33.5MB)
// 테스트 17 〉	통과 (0.14ms, 33.5MB)
// 테스트 18 〉	통과 (0.19ms, 33.5MB)
// 테스트 19 〉	통과 (0.13ms, 33.5MB)
// 테스트 20 〉	통과 (0.04ms, 33.7MB)
// 테스트 21 〉	통과 (0.12ms, 33.4MB)
// 효율성  테스트
// 테스트 1 〉	통과 (2.02ms, 36.8MB)
// 테스트 2 〉	통과 (2.09ms, 36.9MB)
// 테스트 3 〉	통과 (2.24ms, 36.9MB)
// 테스트 4 〉	통과 (2.12ms, 36.9MB)
```

# 접근 2 : 수학

수학적으로 접근하기...

수직선상에서 오른쪽 점에서 왼쪽 점을 뺀다음, 세울 수 있는 기지국의 개수로 나누는 식으로 접근하는 것인데..

어떻게 이런 생각을? 선형대수학의 관점인 것 같다. 나중에 다시 풀어볼 것

엥 근데 이것도 자바스크립트에서 시간초과..

#### python

```python
import math
def solution(n, stations, w):
    loc = 1
    ans = 0
    for station in stations:
        # 범위를 벗어나지 않도록 처리
        left = max(1, station - w)
        right = min(n, station + w)

        ans += math.ceil((left - loc) / (2 * w + 1))
        loc = right + 1

    if loc <= n:
        ans += math.ceil((n - loc + 1) / (2 * w + 1))

    return ans
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.4MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.1MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
테스트 15 〉	통과 (0.01ms, 10.3MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (0.01ms, 10.3MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.3MB)
테스트 20 〉	통과 (0.01ms, 10.4MB)
테스트 21 〉	통과 (0.02ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (4.68ms, 10.4MB)
테스트 2 〉	통과 (5.24ms, 10.4MB)
테스트 3 〉	통과 (5.18ms, 10.4MB)
테스트 4 〉	통과 (5.26ms, 10.5MB)
"""
```

#### js

이것도 상수로 안만들어주면 효율성 1번 시간초과남;;

```js
function solution(n, stations, w) {
  const interval = 2 * w + 1
  let loc = 1
  let ans = 0
  for (const station of stations) {
    const left = Math.max(1, station - w)
    const right = Math.min(n, station + w)
    ans += Math.ceil((left - loc) / interval)
    loc = right + 1
  }

  if (loc <= n) {
    ans += Math.ceil((n - loc + 1) / interval)
  }
  return ans
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.06ms, 33.5MB)
// 테스트 2 〉	통과 (0.06ms, 33.5MB)
// 테스트 3 〉	통과 (0.06ms, 33.6MB)
// 테스트 4 〉	통과 (0.06ms, 33.4MB)
// 테스트 5 〉	통과 (0.06ms, 33.6MB)
// 테스트 6 〉	통과 (0.07ms, 33.5MB)
// 테스트 7 〉	통과 (0.06ms, 33.5MB)
// 테스트 8 〉	통과 (0.06ms, 33.6MB)
// 테스트 9 〉	통과 (0.06ms, 33.5MB)
// 테스트 10 〉	통과 (0.06ms, 33.5MB)
// 테스트 11 〉	통과 (0.06ms, 33.5MB)
// 테스트 12 〉	통과 (0.06ms, 33.6MB)
// 테스트 13 〉	통과 (0.06ms, 33.6MB)
// 테스트 14 〉	통과 (0.06ms, 33.5MB)
// 테스트 15 〉	통과 (0.06ms, 33.5MB)
// 테스트 16 〉	통과 (0.07ms, 33.5MB)
// 테스트 17 〉	통과 (0.06ms, 33.4MB)
// 테스트 18 〉	통과 (0.09ms, 33.5MB)
// 테스트 19 〉	통과 (0.07ms, 33.5MB)
// 테스트 20 〉	통과 (0.08ms, 33.5MB)
// 테스트 21 〉	통과 (0.16ms, 33.5MB)
// 효율성  테스트
// 테스트 1 〉	통과 (3.82ms, 37.6MB)
// 테스트 2 〉	통과 (3.21ms, 37.6MB)
// 테스트 3 〉	통과 (3.58ms, 37.5MB)
// 테스트 4 〉	통과 (3.24ms, 37.5MB)
```
