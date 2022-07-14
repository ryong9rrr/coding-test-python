function solution(new_id) {
  let parsedId = new_id
  parsedId = parsedId
    .toLowerCase()
    .replace(/[^a-z0-9\-_.]/g, '')
    .replace(/\.+/g, '.')
    .replace(/^\.|\.$/g, '')
    .replace(/^$/g, 'a')
    .slice(0, 15)
    .replace(/\.$/g, '')

  const len = parsedId.length
  const lastStr = parsedId[len - 1]

  return len <= 2 ? parsedId + lastStr.repeat(3 - len) : parsedId
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.35ms, 30.2MB)
// 테스트 2 〉	통과 (0.22ms, 29.7MB)
// 테스트 3 〉	통과 (0.23ms, 30.2MB)
// 테스트 4 〉	통과 (0.39ms, 29.9MB)
// 테스트 5 〉	통과 (0.22ms, 30.2MB)
// 테스트 6 〉	통과 (0.35ms, 30.2MB)
// 테스트 7 〉	통과 (0.20ms, 30.2MB)
// 테스트 8 〉	통과 (0.25ms, 29.8MB)
// 테스트 9 〉	통과 (0.20ms, 30.1MB)
// 테스트 10 〉	통과 (0.31ms, 30MB)
// 테스트 11 〉	통과 (0.35ms, 30.1MB)
// 테스트 12 〉	통과 (0.33ms, 30.1MB)
// 테스트 13 〉	통과 (0.36ms, 29.8MB)
// 테스트 14 〉	통과 (0.32ms, 30MB)
// 테스트 15 〉	통과 (0.21ms, 30MB)
// 테스트 16 〉	통과 (0.35ms, 30.1MB)
// 테스트 17 〉	통과 (0.33ms, 30.1MB)
// 테스트 18 〉	통과 (0.37ms, 30.1MB)
// 테스트 19 〉	통과 (0.30ms, 30.1MB)
// 테스트 20 〉	통과 (0.36ms, 29.9MB)
// 테스트 21 〉	통과 (0.29ms, 30MB)
// 테스트 22 〉	통과 (0.33ms, 30MB)
// 테스트 23 〉	통과 (0.40ms, 30.2MB)
// 테스트 24 〉	통과 (0.21ms, 30.1MB)
// 테스트 25 〉	통과 (0.20ms, 29.9MB)
// 테스트 26 〉	통과 (0.32ms, 30MB)
