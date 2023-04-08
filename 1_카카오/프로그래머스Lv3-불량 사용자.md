> 2019 카카오 개발자 겨울 인턴십
> related topics : 문자열, DFS, 백트래킹

# 접근 : 집합 + DFS(백트래킹)

다른 사람들의 베스트풀이보다 훨씬 잘 푼 것 같다. 근데 이게 어떻게 1점 짜리 문제임...?

#### python

```python
def match(word, reg):
    if len(word) != len(reg):
        return False
    n = len(reg)
    for i in range(n):
        if reg[i] == "*":
            continue
        if reg[i] != word[i]:
            return False
    return True

def solution(user_id, banned_id):
    n = len(banned_id)
    result = set()

    def dfs(index, users):
        if index == n:
            result.add("".join(sorted(list(users))))
            return
        banned = banned_id[index]
        for user in list(users):
            if match(user, banned):
                users.remove(user)
                dfs(index + 1, users)
                users.add(user) # 백트래킹

    dfs(0, set(user_id))
    return len(list(result))
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (0.05ms, 10.1MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (111.71ms, 10.2MB)
테스트 6 〉	통과 (1.41ms, 10.1MB)
테스트 7 〉	통과 (0.04ms, 10.3MB)
테스트 8 〉	통과 (0.05ms, 10.3MB)
테스트 9 〉	통과 (0.07ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
테스트 11 〉	통과 (0.11ms, 10.2MB)
"""
```

#### js

```js
const match = (word, reg) => {
  if (word.length !== reg.length) {
    return false
  }
  const n = word.length
  for (let i = 0; i < n; i += 1) {
    if (reg[i] === "*") {
      continue
    }
    if (reg[i] !== word[i]) {
      return false
    }
  }
  return true
}

function solution(user_id, banned_id) {
  const n = banned_id.length
  const result = new Set()

  const dfs = (index, users) => {
    if (index === n) {
      result.add([...users].sort().join(""))
      return
    }
    const banned = banned_id[index]
    for (const user of [...users]) {
      if (match(user, banned)) {
        users.delete(user)
        dfs(index + 1, users)
        users.add(user)
      }
    }
  }

  dfs(0, new Set(user_id))

  return result.size
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.12ms, 33.4MB)
// 테스트 2 〉	통과 (0.35ms, 33.5MB)
// 테스트 3 〉	통과 (0.24ms, 33.6MB)
// 테스트 4 〉	통과 (0.37ms, 33.5MB)
// 테스트 5 〉	통과 (17.63ms, 38.2MB)
// 테스트 6 〉	통과 (2.57ms, 37.4MB)
// 테스트 7 〉	통과 (0.26ms, 33.5MB)
// 테스트 8 〉	통과 (0.23ms, 33.6MB)
// 테스트 9 〉	통과 (0.28ms, 33.6MB)
// 테스트 10 〉	통과 (0.27ms, 33.5MB)
// 테스트 11 〉	통과 (0.24ms, 33.5MB)
```
