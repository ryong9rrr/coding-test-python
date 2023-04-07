> related topics : 문자열, 해시, 정렬

외계인 나라의 문자 우선순위대로 문자열이 정렬되어있는지 아닌지 불리언을 반환하는 문제

## 접근 : 우선순위 해시테이블을 만들어서 앞 뒤 문자를 하나하나 비교

- 시간복잡도 : O(N^2)
- 공간복잡도 : O(N)

#### python

```python
# 30ms(94%), 13MB(73%)
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        freq = {}
        # i가 작을수록 높은 우선순위
        for i, char in enumerate(order):
            freq[char] = i

        def compare(word1, word2):
            min_len = min(len(word1), len(word2))
            for i in range(min_len):
                char1, char2 = word1[i], word2[i]
                if freq[char1] < freq[char2]:
                    return True
                if freq[char1] > freq[char2]:
                    return False
            return len(word1) <= len(word2) # 마지막으로 두 단어의 길이를 체크


        for i in range(len(words) - 1):
            if not compare(words[i], words[i + 1]):
                return False

        return True
```

#### javascript

```js
// 62ms(66%), 44MB(15%)
/**
 * @param {string[]} words
 * @param {string} order
 * @return {boolean}
 */
var isAlienSorted = function (words, order) {
  const freq = [...order].reduce((obj, char, i) => {
    obj[char] = i
    return obj
  }, {})

  const compare = (word1, word2) => {
    const minLength = Math.min(word1.length, word2.length)
    for (let i = 0; i < minLength; i += 1) {
      const char1 = word1[i]
      const char2 = word2[i]
      if (freq[char1] < freq[char2]) {
        return true
      }
      if (freq[char1] > freq[char2]) {
        return false
      }
    }
    return word1.length <= word2.length
  }

  for (let i = 0; i < words.length - 1; i += 1) {
    if (!compare(words[i], words[i + 1])) {
      return false
    }
  }
  return true
}
```
