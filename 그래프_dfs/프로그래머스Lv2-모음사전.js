function solution(word) {
  const ALPHAS = ['A', 'E', 'I', 'O', 'U']
  const setWords = new Set()

  const dfs = (words) => {
    setWords.add(words)
    if (words.length === 5) {
      return
    }
    for (const nextAlpha of ALPHAS) {
      dfs(words + nextAlpha)
    }
  }

  for (const alpha of ALPHAS) {
    dfs(alpha)
  }

  const sortedWords = [...setWords].sort()

  for (let i = 0; i < sortedWords.length; i++) {
    if (sortedWords[i] === word) {
      return i + 1
    }
  }
}
// 정확성  테스트
// 테스트 1 〉	통과 (1.26ms, 30.1MB)
// 테스트 2 〉	통과 (1.96ms, 30.3MB)
// 테스트 3 〉	통과 (1.28ms, 30.2MB)
// 테스트 4 〉	통과 (1.35ms, 30.2MB)
// 테스트 5 〉	통과 (1.28ms, 30.3MB)
// 테스트 6 〉	통과 (1.18ms, 30.2MB)
// 테스트 7 〉	통과 (1.27ms, 30.2MB)
// 테스트 8 〉	통과 (1.18ms, 30.3MB)
// 테스트 9 〉	통과 (1.18ms, 30.3MB)
// 테스트 10 〉	통과 (1.26ms, 30.3MB)
// 테스트 11 〉	통과 (1.23ms, 30MB)
// 테스트 12 〉	통과 (1.20ms, 30.3MB)
// 테스트 13 〉	통과 (2.24ms, 30.3MB)
// 테스트 14 〉	통과 (1.21ms, 30.1MB)
// 테스트 15 〉	통과 (1.35ms, 30.4MB)
// 테스트 16 〉	통과 (1.23ms, 30.3MB)
// 테스트 17 〉	통과 (1.29ms, 30.3MB)
// 테스트 18 〉	통과 (1.31ms, 30.2MB)
// 테스트 19 〉	통과 (1.31ms, 30.4MB)
// 테스트 20 〉	통과 (1.49ms, 30.1MB)
// 테스트 21 〉	통과 (2.05ms, 30.2MB)
// 테스트 22 〉	통과 (1.17ms, 30.3MB)
// 테스트 23 〉	통과 (1.18ms, 30.2MB)
// 테스트 24 〉	통과 (1.17ms, 30.2MB)
// 테스트 25 〉	통과 (1.16ms, 30.2MB)
// 테스트 26 〉	통과 (3.05ms, 30MB)
// 테스트 27 〉	통과 (2.10ms, 30.3MB)
// 테스트 28 〉	통과 (1.47ms, 30.1MB)
// 테스트 29 〉	통과 (1.18ms, 30.4MB)
// 테스트 30 〉	통과 (1.23ms, 30.2MB)
// 테스트 31 〉	통과 (1.28ms, 30.2MB)
// 테스트 32 〉	통과 (2.19ms, 30.3MB)
// 테스트 33 〉	통과 (1.77ms, 30MB)
// 테스트 34 〉	통과 (1.22ms, 30.2MB)
// 테스트 35 〉	통과 (1.47ms, 30.1MB)
// 테스트 36 〉	통과 (2.27ms, 30.2MB)
// 테스트 37 〉	통과 (1.44ms, 30.3MB)
// 테스트 38 〉	통과 (1.99ms, 30.1MB)
// 테스트 39 〉	통과 (1.19ms, 30.2MB)
// 테스트 40 〉	통과 (1.19ms, 30.1MB)
