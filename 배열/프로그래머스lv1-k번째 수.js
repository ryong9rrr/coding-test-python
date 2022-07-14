function solution(array, commands) {
  return commands.map(([i, j, k]) => array.slice(i - 1, j).sort((a, b) => a - b)[k - 1])
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.08ms, 30.2MB)
// 테스트 2 〉	통과 (0.13ms, 30.1MB)
// 테스트 3 〉	통과 (0.10ms, 30.3MB)
// 테스트 4 〉	통과 (0.11ms, 30.2MB)
// 테스트 5 〉	통과 (0.07ms, 30.1MB)
// 테스트 6 〉	통과 (0.11ms, 30.2MB)
// 테스트 7 〉	통과 (0.11ms, 30.2MB)
