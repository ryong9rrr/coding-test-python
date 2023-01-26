const getPrevMax = (prevRow, currentJ) => {
  return Math.max(...prevRow.filter((v, j) => j !== currentJ))
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
// 테스트 1 〉	통과 (2.89ms, 37.9MB)
// 테스트 2 〉	통과 (3.81ms, 37.9MB)
// 테스트 3 〉	통과 (4.49ms, 37.8MB)
// 테스트 4 〉	통과 (2.83ms, 37.8MB)
// 테스트 5 〉	통과 (2.97ms, 37.8MB)
// 테스트 6 〉	통과 (3.19ms, 37.9MB)
// 테스트 7 〉	통과 (2.74ms, 38MB)
// 테스트 8 〉	통과 (4.71ms, 37.8MB)
// 테스트 9 〉	통과 (3.04ms, 37.9MB)
// 테스트 10 〉	통과 (3.21ms, 37.9MB)
// 테스트 11 〉	통과 (4.80ms, 38MB)
// 테스트 12 〉	통과 (2.95ms, 37.8MB)
// 테스트 13 〉	통과 (3.22ms, 37.9MB)
// 테스트 14 〉	통과 (2.77ms, 37.8MB)
// 테스트 15 〉	통과 (2.85ms, 37.9MB)
// 테스트 16 〉	통과 (2.88ms, 37.9MB)
// 테스트 17 〉	통과 (2.90ms, 37.8MB)
// 테스트 18 〉	통과 (3.01ms, 37.8MB)
// 효율성  테스트
// 테스트 1 〉	통과 (69.76ms, 90.1MB)
// 테스트 2 〉	통과 (76.40ms, 90.5MB)
// 테스트 3 〉	통과 (69.32ms, 90.1MB)
// 테스트 4 〉	통과 (75.95ms, 90.6MB)
