# 접근 : 그리디 + 문자열

- 시간복잡도 : O(N)
- 공간복잡도 : O(1)

```python
# 116ms(63%), 14MB(47%)
class Solution:
    def partitionString(self, s: str) -> int:
        ans = 0
        cur = set()
        for char in s:
            if char in cur:
                cur = set()
                ans += 1
            cur.add(char)

        if cur:
            ans += 1

        return ans
```

## js

```js
// 125ms(38%), 53MB(21%)

/**
 * @param {string} s
 * @return {number}
 */
var partitionString = function (s) {
  let count = 0
  const cur = new Set()

  Array.from(s).forEach((char) => {
    if (cur.has(char)) {
      cur.clear()
      count += 1
    }
    cur.add(char)
  })

  if (cur.size > 0) {
    count += 1
  }

  return count
}
```
