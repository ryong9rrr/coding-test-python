const getPrevMax = (prevRow, currentJ) => {
  let result = -Infinity
  for (let j = 0; j < 4; j++) {
    if (j !== currentJ) {
      result = Math.max(result, prevRow[j])
    }
  }
  return result
}

function solution(land) {
  const N = land.length
  const dp = Array.from({ length: N }, () => new Array(4).fill(0))
  dp[0] = land[0]

  for (let i = 1; i < N; i++) {
    for (let j = 0; j < 4; j++) {
      dp[i][j] = getPrevMax(dp[i - 1], j) + land[i][j]
    }
  }

  return Math.max(...dp[N - 1])
}
// 정확성  테스트
// 테스트 1 〉	통과 (1.70ms, 35.8MB)
// 테스트 2 〉	통과 (1.81ms, 36.9MB)
// 테스트 3 〉	통과 (1.87ms, 35.9MB)
// 테스트 4 〉	통과 (2.43ms, 36MB)
// 테스트 5 〉	통과 (2.40ms, 35.8MB)
// 테스트 6 〉	통과 (1.82ms, 35.8MB)
// 테스트 7 〉	통과 (2.00ms, 35.8MB)
// 테스트 8 〉	통과 (3.10ms, 37.1MB)
// 테스트 9 〉	통과 (1.78ms, 35.9MB)
// 테스트 10 〉	통과 (1.81ms, 35.9MB)
// 테스트 11 〉	통과 (1.77ms, 37.1MB)
// 테스트 12 〉	통과 (2.95ms, 37.1MB)
// 테스트 13 〉	통과 (1.86ms, 35.9MB)
// 테스트 14 〉	통과 (2.37ms, 36MB)
// 테스트 15 〉	통과 (2.40ms, 35.9MB)
// 테스트 16 〉	통과 (2.11ms, 37.1MB)
// 테스트 17 〉	통과 (1.82ms, 35.9MB)
// 테스트 18 〉	통과 (1.83ms, 35.9MB)
// 효율성  테스트
// 테스트 1 〉	통과 (58.80ms, 76.7MB)
// 테스트 2 〉	통과 (70.93ms, 75.9MB)
// 테스트 3 〉	통과 (44.81ms, 78.2MB)
// 테스트 4 〉	통과 (64.31ms, 76.4MB)
