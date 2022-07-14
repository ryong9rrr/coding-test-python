function makeSet(string) {
  const result = {}
  const reg = /[^A-Z]/g
  for (let i = 0; i < string.length - 1; i++) {
    const s = string
      .slice(i, i + 2)
      .toUpperCase()
      .replace(reg, '')
    if (s.length === 2) {
      if (!result[s]) result[s] = 0
      result[s]++
    }
  }
  return result
}

function solution(str1, str2) {
  const s1 = makeSet(str1)
  const s2 = makeSet(str2)

  if (Object.keys(s1).length === 0 && Object.keys(s2).length === 0) {
    return 65536
  }

  const allKeys = new Set([])

  for (const key in s1) {
    allKeys.add(key)
  }

  for (const key in s2) {
    allKeys.add(key)
  }

  let union = 0
  let intersection = 0

  for (const key of [...allKeys]) {
    if (s1[key] && s2[key]) {
      intersection += Math.min(s1[key], s2[key])
    }
    if (!s1[key]) s1[key] = 0
    if (!s2[key]) s2[key] = 0

    union += Math.max(s1[key], s2[key])
  }

  return Math.floor((intersection / union) * 65536)
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.46ms, 30MB)
// 테스트 2 〉	통과 (0.57ms, 30.1MB)
// 테스트 3 〉	통과 (0.34ms, 29.9MB)
// 테스트 4 〉	통과 (2.06ms, 30.2MB)
// 테스트 5 〉	통과 (0.37ms, 29.7MB)
// 테스트 6 〉	통과 (0.37ms, 30.1MB)
// 테스트 7 〉	통과 (0.53ms, 30MB)
// 테스트 8 〉	통과 (0.35ms, 30.1MB)
// 테스트 9 〉	통과 (0.51ms, 30.1MB)
// 테스트 10 〉	통과 (0.87ms, 30MB)
// 테스트 11 〉	통과 (1.06ms, 30.2MB)
// 테스트 12 〉	통과 (0.32ms, 30.1MB)
// 테스트 13 〉	통과 (0.46ms, 29.9MB)
