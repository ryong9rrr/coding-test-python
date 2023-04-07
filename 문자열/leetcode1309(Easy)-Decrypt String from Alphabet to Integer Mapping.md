> related topics : 문자열

`[key, value]` 형태의 배열을 만든 뒤, `replace` 내장 메서드를 사용.

## 접근 : 해싱 + 내장 메서드

#### python

```python
# 15ms(100%), 13.7MB(94%)
class Solution:
    def freqAlphabets(self, s: str) -> str:
        maps = []
        for i in range(1, 27):
            value = chr(96 + i)
            if 1 <= i <= 9:
                key = str(i)
                maps.append([key, value])
                continue
            key = f"{i}#"
            maps.append([key, value])

        ans = s
        for key, value in maps[::-1]:
            ans = ans.replace(key, value)

        return ans
```

#### javascript

```js
// 52ms(90%), 43MB(17%)
/**
 * @param {string} s
 * @return {string}
 */
var freqAlphabets = function (s) {
  const maps = Array.from({ length: 26 }, (v, i) => i + 1).map((i) => {
    const value = String.fromCharCode(96 + i)
    if (0 <= i && i <= 9) {
      return [String(i), value]
    }
    return [`${i}#`, value]
  })

  let ans = s
  for (const [key, value] of [...maps].reverse()) {
    const regex = new RegExp(key, "g")
    ans = ans.replace(regex, value)
  }
  return ans
}
```
