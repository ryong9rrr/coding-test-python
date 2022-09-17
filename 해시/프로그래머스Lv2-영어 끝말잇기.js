function solution(n, words) {
  const dic = {}
  const result = [0, 0]

  dic[words[0]] = true
  for (let i = 1; i < words.length; i++) {
    const prev = words[i - 1]
    const cur = words[i]
    if (prev[prev.length - 1] !== cur[0] || dic[cur]) {
      return [(i % n) + 1, Math.floor(i / n) + 1]
    }
    dic[cur] = true
  }

  return result
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.07ms, 33.4MB)
// 테스트 2 〉	통과 (0.28ms, 33.4MB)
// 테스트 3 〉	통과 (0.06ms, 33.5MB)
// 테스트 4 〉	통과 (0.23ms, 33.6MB)
// 테스트 5 〉	통과 (0.18ms, 33.5MB)
// 테스트 6 〉	통과 (0.08ms, 33.5MB)
// 테스트 7 〉	통과 (0.19ms, 33.6MB)
// 테스트 8 〉	통과 (0.11ms, 33.4MB)
// 테스트 9 〉	통과 (0.07ms, 33.4MB)
// 테스트 10 〉	통과 (0.22ms, 33.4MB)
// 테스트 11 〉	통과 (0.23ms, 33.5MB)
// 테스트 12 〉	통과 (0.18ms, 33.6MB)
// 테스트 13 〉	통과 (0.06ms, 33.5MB)
// 테스트 14 〉	통과 (0.10ms, 33.6MB)
// 테스트 15 〉	통과 (0.10ms, 33.4MB)
// 테스트 16 〉	통과 (0.09ms, 33.4MB)
// 테스트 17 〉	통과 (0.06ms, 33.4MB)
// 테스트 18 〉	통과 (0.09ms, 33.5MB)
// 테스트 19 〉	통과 (0.10ms, 33.4MB)
// 테스트 20 〉	통과 (0.20ms, 33.4MB)
