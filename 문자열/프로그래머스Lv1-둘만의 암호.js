function getNextChar(curChar, interval, skipSet) {
  const nextChars = []
  let n = curChar.charCodeAt()
  while (nextChars.length < interval) {
    n = n === 122 ? 97 : n + 1
    if (!skipSet.has(String.fromCharCode(n))) {
      nextChars.push(String.fromCharCode(n))
    }
  }
  return nextChars[interval - 1]
}

function solution(s, skip, index) {
  return [...s]
    .map((char) => getNextChar(char, index, new Set([...skip])))
    .join("")
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.25ms, 33.5MB)
// 테스트 2 〉	통과 (0.18ms, 33.4MB)
// 테스트 3 〉	통과 (0.37ms, 33.6MB)
// 테스트 4 〉	통과 (0.19ms, 33.4MB)
// 테스트 5 〉	통과 (0.30ms, 33.5MB)
// 테스트 6 〉	통과 (0.36ms, 33.5MB)
// 테스트 7 〉	통과 (0.49ms, 33.5MB)
// 테스트 8 〉	통과 (0.24ms, 33.4MB)
// 테스트 9 〉	통과 (0.32ms, 33.4MB)
// 테스트 10 〉	통과 (0.23ms, 33.5MB)
// 테스트 11 〉	통과 (0.27ms, 33.4MB)
// 테스트 12 〉	통과 (0.23ms, 33.4MB)
// 테스트 13 〉	통과 (0.24ms, 33.4MB)
// 테스트 14 〉	통과 (0.19ms, 33.4MB)
// 테스트 15 〉	통과 (0.21ms, 33.5MB)
// 테스트 16 〉	통과 (0.22ms, 33.4MB)
// 테스트 17 〉	통과 (0.27ms, 33.5MB)
// 테스트 18 〉	통과 (0.46ms, 33.4MB)
// 테스트 19 〉	통과 (0.33ms, 33.4MB)
