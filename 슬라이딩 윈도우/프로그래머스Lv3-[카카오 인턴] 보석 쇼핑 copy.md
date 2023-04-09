> 2020 카카오 인턴십
> related topics : 슬라이딩 윈도우

이건 슬라이딩 윈도우 최적화 문제임...

# 접근 1 : 2중 루프 + 리스트 슬라이싱 (시간초과)

가장 직관적인 방법으로 O(N^2)의 반복문에다가 리스트 슬라이싱을 적용해봤지만 시간초과가 떴다.

#### python

```python
def solution(gems):
    kinds_length = len(set(gems))
    gems_length = len(gems)

    intervals = []
    minimum = int(1e9)
    for left in range(0, gems_length - kinds_length + 1):
        for right in range(left + kinds_length, gems_length + 1):
            pick = gems[left : right]
            if len(set(pick)) == kinds_length:
                intervals.append([left + 1, right])
                minimum = min(minimum, right - left - 1)

    for left, right in intervals:
        if right - left == minimum:
            return [left, right]
"""
정확성  테스트
테스트 1 〉	통과 (0.09ms, 10.1MB)
테스트 2 〉	통과 (5.59ms, 10.3MB)
테스트 3 〉	통과 (136.54ms, 13.6MB)
테스트 4 〉	통과 (0.07ms, 10.1MB)
테스트 5 〉	통과 (411.29ms, 24.4MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.07ms, 10.3MB)
테스트 8 〉	통과 (1922.59ms, 17MB)
테스트 9 〉	통과 (2819.38ms, 41.6MB)
테스트 10 〉	통과 (2378.97ms, 10.4MB)
테스트 11 〉	실패 (시간 초과)
테스트 12 〉	실패 (시간 초과)
테스트 13 〉	실패 (시간 초과)
테스트 14 〉	실패 (시간 초과)
테스트 15 〉	실패 (시간 초과)
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
테스트 15 〉	실행 중단
"""

# 2번째 시도... 시간초과
def solution(gems):
    left = 0
    basket = {}

    minimum = int(1e9)
    result = []
    for right in range(len(gems)):
        while left < right and len(basket) == len(set(gems)):
            result.append([left, right])
            minimum = min(minimum, right - left)
            gem = gems[left]
            basket[gem] -= 1
            if basket[gem] == 0:
                del basket[gem]
            left += 1

        gem = gems[right]
        if gem not in basket:
            basket[gem] = 0
        basket[gem] += 1

    if len(basket) == len(set(gems)):
        result.append([left, len(gems)])
        minimum = min(minimum, len(gems) - left)


    for left, right in result:
        if right - left == minimum:
            return [left + 1, right]
"""
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.2MB)
테스트 2 〉	통과 (0.52ms, 10.2MB)
테스트 3 〉	통과 (3.74ms, 10.2MB)
테스트 4 〉	통과 (4.96ms, 10.2MB)
테스트 5 〉	통과 (4.08ms, 10.1MB)
테스트 6 〉	실패 (0.01ms, 10.2MB)
테스트 7 〉	실패 (0.03ms, 10.1MB)
테스트 8 〉	통과 (19.86ms, 10.3MB)
테스트 9 〉	통과 (42.44ms, 10.3MB)
테스트 10 〉	통과 (25.57ms, 10.2MB)
테스트 11 〉	통과 (57.79ms, 10.3MB)
테스트 12 〉	통과 (102.00ms, 10.2MB)
테스트 13 〉	통과 (196.23ms, 10.4MB)
테스트 14 〉	통과 (275.60ms, 10.3MB)
테스트 15 〉	통과 (713.52ms, 10.6MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실행 중단
테스트 7 〉	실행 중단
테스트 8 〉	실행 중단
테스트 9 〉	실행 중단
테스트 10 〉	실행 중단
테스트 11 〉	실행 중단
테스트 12 〉	실행 중단
테스트 13 〉	실행 중단
테스트 14 〉	실행 중단
테스트 15 〉	실행 중단
"""
```

# 접근 2 : 슬라이딩 윈도우 최적화

이게 왜 2점 짜리 문제...? 2시간 30분 걸려서 풀었다..

#### python

```python
class Sliding_window:
    def __init__(self):
        self.window = {}
        self.size = 0

    def add(self, item):
        if item not in self.window:
            self.window[item] = 0
            self.size += 1
        self.window[item] += 1

    def remove(self, item):
        self.window[item] -= 1
        if self.window[item] == 0:
            del self.window[item]
            self.size -= 1

def solution(gems):
    kinds_length = len(set(gems))
    gems_length = len(gems)

    # 슬라이딩 윈도우 값 초기 설정,
    # (1) 일부러 모든 종류의 개수(kinds_length)에서 -2를 한 인덱스까지만 넣어준다.
    left = 0
    sliding_window = Sliding_window()
    for i in range(left, kinds_length - 1):
        sliding_window.add(gems[i])

    minimum = int(1e9)
    intervals = []
    # (2) 따라서 모든 종류의 개수(kinds_length) - 1인 인덱스부터 순회를 시작하는데,
    for right in range(kinds_length - 1, gems_length):
        sliding_window.add(gems[right])
        # (3) 이렇게 해야 while문을 아래로 내릴 수 있기 때문. 이렇게 하지 않으면 똑같은 while문을 순회가 종료한 뒤에 또 써줘야한다. (마지막 값 처리를 해야하므로)
        while sliding_window.size == kinds_length:
            intervals.append([left, right])
            minimum = min(minimum, right - left)
            sliding_window.remove(gems[left])
            left += 1

    for left, right in intervals:
        if right - left == minimum:
            return [left + 1, right + 1]
"""
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.1MB)
테스트 2 〉	통과 (0.09ms, 10.3MB)
테스트 3 〉	통과 (0.26ms, 10.3MB)
테스트 4 〉	통과 (0.42ms, 10.1MB)
테스트 5 〉	통과 (0.88ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.41ms, 10.2MB)
테스트 9 〉	통과 (0.81ms, 10.1MB)
테스트 10 〉	통과 (0.42ms, 10.2MB)
테스트 11 〉	통과 (0.57ms, 10.4MB)
테스트 12 〉	통과 (1.38ms, 10.2MB)
테스트 13 〉	통과 (1.77ms, 10.3MB)
테스트 14 〉	통과 (1.12ms, 10.4MB)
테스트 15 〉	통과 (3.75ms, 10.7MB)
효율성  테스트
테스트 1 〉	통과 (4.57ms, 10.9MB)
테스트 2 〉	통과 (6.11ms, 11.1MB)
테스트 3 〉	통과 (16.06ms, 12.6MB)
테스트 4 〉	통과 (8.42ms, 11.9MB)
테스트 5 〉	통과 (23.52ms, 14.3MB)
테스트 6 〉	통과 (32.15ms, 15.6MB)
테스트 7 〉	통과 (36.39ms, 16.2MB)
테스트 8 〉	통과 (37.43ms, 16.5MB)
테스트 9 〉	통과 (50.62ms, 18.3MB)
테스트 10 〉	통과 (52.98ms, 18.9MB)
테스트 11 〉	통과 (54.79ms, 20MB)
테스트 12 〉	통과 (29.60ms, 15.6MB)
테스트 13 〉	통과 (46.69ms, 18.1MB)
테스트 14 〉	통과 (93.15ms, 25.6MB)
테스트 15 〉	통과 (91.60ms, 25.9MB)
"""
```

#### javascript

```js
class SlidingWindow {
  constructor() {
    this.window = {}
    this.size = 0
  }

  add(item) {
    if (!this.window[item]) {
      this.window[item] = 0
      this.size += 1
    }
    this.window[item] += 1
  }

  remove(item) {
    this.window[item] -= 1
    if (this.window[item] === 0) {
      delete this.window[item]
      this.size -= 1
    }
  }
}

function solution(gems) {
  const kindsLength = new Set(gems).size
  const gemsLength = gems.length

  let left = 0
  const slidingWindow = new SlidingWindow()
  for (let i = 0; i < kindsLength - 1; i += 1) {
    slidingWindow.add(gems[i])
  }

  let minimum = Infinity
  const intervals = []
  for (let right = kindsLength - 1; right < gemsLength; right += 1) {
    slidingWindow.add(gems[right])
    while (slidingWindow.size === kindsLength) {
      intervals.push([left, right])
      minimum = Math.min(minimum, right - left)
      slidingWindow.remove(gems[left])
      left += 1
    }
  }

  for (const [left, right] of intervals) {
    if (right - left === minimum) {
      return [left + 1, right + 1]
    }
  }
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.40ms, 33.5MB)
// 테스트 2 〉	통과 (0.72ms, 33.5MB)
// 테스트 3 〉	통과 (0.50ms, 33.5MB)
// 테스트 4 〉	통과 (0.52ms, 33.5MB)
// 테스트 5 〉	통과 (0.58ms, 33.5MB)
// 테스트 6 〉	통과 (0.16ms, 33.6MB)
// 테스트 7 〉	통과 (0.28ms, 33.5MB)
// 테스트 8 〉	통과 (0.54ms, 33.6MB)
// 테스트 9 〉	통과 (0.81ms, 33.8MB)
// 테스트 10 〉	통과 (0.59ms, 33.6MB)
// 테스트 11 〉	통과 (1.07ms, 33.6MB)
// 테스트 12 〉	통과 (1.77ms, 33.7MB)
// 테스트 13 〉	통과 (1.64ms, 33.8MB)
// 테스트 14 〉	통과 (0.92ms, 33.7MB)
// 테스트 15 〉	통과 (3.49ms, 34.3MB)
// 효율성  테스트
// 테스트 1 〉	통과 (39.25ms, 36.2MB)
// 테스트 2 〉	통과 (4.80ms, 37MB)
// 테스트 3 〉	통과 (13.39ms, 38.9MB)
// 테스트 4 〉	통과 (5.12ms, 37.8MB)
// 테스트 5 〉	통과 (18.42ms, 39.9MB)
// 테스트 6 〉	통과 (22.37ms, 42.5MB)
// 테스트 7 〉	통과 (22.55ms, 44.2MB)
// 테스트 8 〉	통과 (22.68ms, 45.1MB)
// 테스트 9 〉	통과 (27.15ms, 46.3MB)
// 테스트 10 〉	통과 (44.23ms, 46MB)
// 테스트 11 〉	통과 (29.30ms, 46.1MB)
// 테스트 12 〉	통과 (12.26ms, 41.9MB)
// 테스트 13 〉	통과 (28.22ms, 46.3MB)
// 테스트 14 〉	통과 (66.54ms, 53.4MB)
// 테스트 15 〉	통과 (29.45ms, 50.2MB)
```
