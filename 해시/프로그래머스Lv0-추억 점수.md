> https://school.programmers.co.kr/learn/courses/30/lessons/176963
> related topics : 해시

# 접근 : 해시

#### python

```python
from collections import defaultdict
def solution(name, yearning, photo):
    table = defaultdict(int)
    for i in range(len(name)):
        key = name[i]
        value = yearning[i]
        table[key] = value

    result = []
    for keys in photo:
        value = 0
        for key in keys:
            value += table[key]
        result.append(value)

    return result
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.10ms, 10.3MB)
테스트 4 〉	통과 (0.05ms, 10.2MB)
테스트 5 〉	통과 (0.24ms, 10.6MB)
테스트 6 〉	통과 (0.46ms, 10.5MB)
테스트 7 〉	통과 (0.35ms, 10.5MB)
테스트 8 〉	통과 (0.48ms, 10.6MB)
테스트 9 〉	통과 (0.48ms, 10.6MB)
테스트 10 〉	통과 (1.63ms, 10.8MB)
테스트 11 〉	통과 (0.98ms, 10.8MB)
테스트 12 〉	통과 (0.67ms, 10.6MB)
테스트 13 〉	통과 (0.05ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
"""
```

#### js

```js
function solution(name, yearning, photo) {
  const table = {}
  for (let i = 0; i < name.length; i += 1) {
    const key = name[i]
    const value = yearning[i]
    table[key] = value
  }

  return photo.map((keys) => {
    let value = 0
    for (const key of keys) {
      if (key in table) {
        value += table[key]
      }
    }
    return value
  })
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.08ms, 33.4MB)
// 테스트 2 〉	통과 (0.18ms, 33.4MB)
// 테스트 3 〉	통과 (0.38ms, 33.4MB)
// 테스트 4 〉	통과 (0.22ms, 33.5MB)
// 테스트 5 〉	통과 (0.36ms, 33.5MB)
// 테스트 6 〉	통과 (0.57ms, 33.8MB)
// 테스트 7 〉	통과 (0.51ms, 33.7MB)
// 테스트 8 〉	통과 (0.53ms, 33.7MB)
// 테스트 9 〉	통과 (0.56ms, 33.7MB)
// 테스트 10 〉	통과 (0.87ms, 33.9MB)
// 테스트 11 〉	통과 (0.86ms, 33.9MB)
// 테스트 12 〉	통과 (0.70ms, 33.9MB)
// 테스트 13 〉	통과 (0.22ms, 33.5MB)
// 테스트 14 〉	통과 (0.07ms, 33.5MB)
```
