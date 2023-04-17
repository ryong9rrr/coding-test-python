---
layout: post
title: "프로그래머스 Lv3) [카카오 인턴] 보석 쇼핑"
tags: [슬라이딩 윈도우, KAKAO]
comments: true
categories:
---

> 슬라이딩 윈도우 최적화 방안 (2020 카카오 인턴십)

---

> [프로그래머스 Lv3) [카카오 인턴] 보석 쇼핑](https://school.programmers.co.kr/learn/courses/30/lessons/67258)

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
```

# 접근 2 : 슬라이딩 윈도우 + 최적화된 슬라이딩 윈도우

**최적화된 슬라이딩 윈도우**를 구현하여 O(N)으로 풀이가 가능하다.

#### python

```python
# 해시테이블 형태의 슬라이딩윈도우 클래스
class Slide:
    def __init__(self):
        self.window = {}
        self.kinds = 0

    def increase(self, item):
        if item not in self.window:
            self.window[item] = 0
            self.kinds += 1
        self.window[item] += 1

    def decrease(self, item):
        if item not in self.window: # (없어도 되긴 하지만)존재하지 않는 아이템을 없앨 수는 없으므로 예외처리
            raise
        self.window[item] -= 1
        if self.window[item] == 0:
            del self.window[item]
            self.kinds -= 1


def solution(gems):
    GEMS_LENGTH = len(gems)
    GEMS_KINDS = len(set(gems))

    slide = Slide()
    # 어쨌든 모든 보석을 담아야 하므로 종류만큼 윈도우를 늘리고 시작해야함.
    # 그런데 딱 종류만큼 늘리고 시작하면 처음에 모두 담길 경우도 고려해주는 코드를 작성해야하므로...
    # (종류 - 1) 만큼만 늘리고 시작한다.
    for i in range(GEMS_KINDS - 1):
        slide.increase(gems[i])

    minimum_size = GEMS_LENGTH
    intervals = []
    left = 0
    # GEMS_KINDS - 1 전까지만 늘렸으므로 GEMS_KINDS - 1 부터 늘리기 시작
    for right in range(GEMS_KINDS - 1, GEMS_LENGTH):
        slide.increase(gems[right])

        # 만약 충분한 보석을 가지고 있다면
        while slide.kinds == GEMS_KINDS:
            intervals.append([left, right])
            minimum_size = min(minimum_size, right - left)
            slide.decrease(gems[left])
            left += 1

    for left, right in intervals:
        if right - left == minimum_size:
            return [left + 1, right + 1]
"""
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.10ms, 10.1MB)
테스트 3 〉	통과 (0.28ms, 10.1MB)
테스트 4 〉	통과 (0.21ms, 10.3MB)
테스트 5 〉	통과 (0.50ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.44ms, 10.2MB)
테스트 9 〉	통과 (0.82ms, 10.2MB)
테스트 10 〉	통과 (0.41ms, 10.4MB)
테스트 11 〉	통과 (0.58ms, 10.4MB)
테스트 12 〉	통과 (1.42ms, 9.97MB)
테스트 13 〉	통과 (1.92ms, 10.4MB)
테스트 14 〉	통과 (1.17ms, 10.4MB)
테스트 15 〉	통과 (4.11ms, 10.6MB)
효율성  테스트
테스트 1 〉	통과 (5.05ms, 10.5MB)
테스트 2 〉	통과 (6.26ms, 11MB)
테스트 3 〉	통과 (16.64ms, 12.4MB)
테스트 4 〉	통과 (7.49ms, 11.8MB)
테스트 5 〉	통과 (23.65ms, 14MB)
테스트 6 〉	통과 (30.66ms, 15.4MB)
테스트 7 〉	통과 (38.05ms, 16.1MB)
테스트 8 〉	통과 (40.98ms, 16.8MB)
테스트 9 〉	통과 (46.51ms, 18.3MB)
테스트 10 〉	통과 (55.12ms, 19.1MB)
테스트 11 〉	통과 (60.14ms, 19.9MB)
테스트 12 〉	통과 (29.23ms, 15.5MB)
테스트 13 〉	통과 (47.80ms, 18.1MB)
테스트 14 〉	통과 (100.86ms, 25.7MB)
테스트 15 〉	통과 (97.82ms, 26MB)
"""
```

#### javascript

```js
class Slide {
  constructor() {
    this.window = {}
    this.kinds = 0
  }

  increase(item) {
    if (!this.window[item]) {
      this.window[item] = 0
      this.kinds += 1
    }
    this.window[item] += 1
  }

  decrease(item) {
    this.window[item] -= 1
    if (this.window[item] === 0) {
      delete this.window[item]
      this.kinds -= 1
    }
  }
}

function solution(gems) {
  const GEMS_KINDS = new Set(gems).size
  const GEMS_LENGTH = gems.length

  const slide = new Slide()
  for (let i = 0; i < GEMS_KINDS - 1; i += 1) {
    slide.increase(gems[i])
  }

  let left = 0
  let minimumSize = GEMS_LENGTH
  const intervals = []
  for (let right = GEMS_KINDS - 1; right < GEMS_LENGTH; right += 1) {
    slide.increase(gems[right])

    while (slide.kinds === GEMS_KINDS) {
      intervals.push([left, right])
      minimumSize = Math.min(minimumSize, right - left)
      slide.decrease(gems[left])
      left += 1
    }
  }

  for (const [left, right] of intervals) {
    if (right - left === minimumSize) {
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
