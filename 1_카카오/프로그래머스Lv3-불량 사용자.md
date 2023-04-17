---
layout: post
title: "프로그래머스 Lv3) 불량 사용자"
tags: [문자열, DFS, 백트래킹, KAKAO]
comments: true
categories:
---

> 2019 카카오 개발자 겨울 인턴십

---

> [프로그래머스 Lv3) 불량 사용자](https://school.programmers.co.kr/learn/courses/30/lessons/64064)

# 접근 : 집합 + DFS(백트래킹)

다른 사람들의 베스트풀이보다 훨씬 잘 푼 것 같다. 근데 이게 어떻게 1점 짜리 문제임...?

#### python

```python
def match(username, rule):
    if len(username) != len(rule):
        return False
    for i in range(len(username)):
        if rule[i] == "*":
            continue
        if username[i] != rule[i]:
            return False
    return True

def solution(user_id, banned_id):
    # 밴을 당하지 않고 남은 유저들을 문자열 순으로 정렬시켜서 관리(중복 방지)
    not_banned_users = set()

    def dfs(banned_index, not_banned_user_set):
        if banned_index == len(banned_id):
            not_banned_users.add("".join(sorted(not_banned_user_set)))
            return

        rule = banned_id[banned_index]

        for user in not_banned_user_set:
            if match(user, rule):
                not_banned_user_set.remove(user)
                dfs(banned_index + 1, not_banned_user_set)
                not_banned_user_set.add(user) # 백트래킹

    dfs(0, set(user_id))

    return len(not_banned_users)
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
const match = (user, rule) => {
  if (user.length !== rule.length) {
    return false
  }

  for (let i = 0; i < user.length; i += 1) {
    if (rule[i] === "*") {
      continue
    }
    if (rule[i] !== user[i]) {
      return false
    }
  }
  return true
}

function solution(user_id, banned_id) {
  const notBannedUsers = new Set()

  const dfs = (bannedIndex, notBannedUserSet) => {
    if (bannedIndex === banned_id.length) {
      notBannedUsers.add([...notBannedUserSet].sort().join(""))
      return
    }

    const rule = banned_id[bannedIndex]
    for (const user of [...notBannedUserSet]) {
      if (match(user, rule)) {
        notBannedUserSet.delete(user)
        dfs(bannedIndex + 1, notBannedUserSet)
        notBannedUserSet.add(user)
      }
    }
  }

  dfs(0, new Set(user_id))

  return notBannedUsers.size
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
