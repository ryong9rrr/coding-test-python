function solution(citations) {
  citations.sort((a, b) => b - a)
  const N = citations.length
  for (let hIndex = 0; hIndex < N; hIndex++) {
    if (hIndex >= citations[hIndex]) return hIndex
  }
  return N
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.20ms, 30MB)
// 테스트 2 〉	통과 (0.28ms, 30MB)
// 테스트 3 〉	통과 (0.27ms, 29.9MB)
// 테스트 4 〉	통과 (0.22ms, 30.2MB)
// 테스트 5 〉	통과 (0.28ms, 29.9MB)
// 테스트 6 〉	통과 (0.33ms, 30.1MB)
// 테스트 7 〉	통과 (0.18ms, 30MB)
// 테스트 8 〉	통과 (0.09ms, 30.1MB)
// 테스트 9 〉	통과 (0.08ms, 30.1MB)
// 테스트 10 〉	통과 (0.20ms, 30MB)
// 테스트 11 〉	통과 (0.38ms, 30.1MB)
// 테스트 12 〉	통과 (0.12ms, 30.1MB)
// 테스트 13 〉	통과 (0.34ms, 29.9MB)
// 테스트 14 〉	통과 (0.28ms, 30.1MB)
// 테스트 15 〉	통과 (0.33ms, 30MB)
// 테스트 16 〉	통과 (0.05ms, 30.1MB)
