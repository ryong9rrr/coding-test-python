# 다른 문자 찾기

> 문자열, prefix-sum, 비트조작

## 접근 1 : 문자열을 마킹하는 방법

- 시간복잡도 : O(N)
- 공간복잡도 : O(N)

#### python

```python
# 42ms(24%),
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = sorted(s)
        b = sorted(t)
        n = max(len(a), len(b))

        while len(a) < n:
            a += "#"

        while len(b) < n:
            b += "#"

        for i in range(n):
            if a[i] != b[i]:
                return a[i] if b[i] == "#" else b[i]
```

## 접근 2 : prefix-sum

- 시간복잡도 : O(N)
- 공간복잡도 : O(N)

어차피 다른 문자는 하나 뿐이니까 아스키코드로 변환 후, 모두 더해서 비교하는 방법

#### python

```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_sum = sum([ord(char) for char in s])
        t_sum = sum([ord(char) for char in t])

        return chr(abs(s_sum - t_sum))
```

## 접근 3 : XOR

- 시간복잡도 : O(N)
- 공간복잡도 : O(1)

#### python

```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for char in s:
            ans ^= ord(char)

        for char in t:
            ans ^= ord(char)

        return chr(ans)
```

#### javascript

```js
/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function (s, t) {
  let ans = 0
  Array.from(s).forEach((char) => {
    ans ^= char.charCodeAt()
  })

  Array.from(t).forEach((char) => {
    ans ^= char.charCodeAt()
  })

  return String.fromCharCode(ans)
}
```
