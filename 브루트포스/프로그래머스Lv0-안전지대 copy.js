function solution(board) {
  const N = board.length
  const dx = [-1, 1, 0, 0, -1, -1, 1, 1]
  const dy = [0, 0, -1, 1, -1, 1, -1, 1]

  // 지뢰가 설치된 곳
  const booms = []
  for (let x = 0; x < N; x++) {
    for (let y = 0; y < N; y++) {
      if (board[x][y] === 1) {
        booms.push([x, y])
      }
    }
  }

  // 지뢰가 설치된 곳 주변에 폭탄 설치
  booms.forEach(([x, y]) => {
    for (let i = 0; i < 8; i++) {
      const nx = x + dx[i]
      const ny = y + dy[i]
      if (0 <= nx && nx < N && 0 <= ny && ny < N) {
        board[nx][ny] = 1
      }
    }
  })

  // 폭탄이 설치되지 않은 곳만 카운팅
  let count = 0
  for (let x = 0; x < N; x++) {
    for (let y = 0; y < N; y++) {
      if (board[x][y] === 0) {
        count++
      }
    }
  }

  return count
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.23ms, 33.4MB)
// 테스트 2 〉	통과 (0.15ms, 33.4MB)
// 테스트 3 〉	통과 (0.21ms, 33.4MB)
// 테스트 4 〉	통과 (0.20ms, 33.4MB)
// 테스트 5 〉	통과 (0.19ms, 33.2MB)
// 테스트 6 〉	통과 (0.23ms, 33.4MB)
// 테스트 7 〉	통과 (0.25ms, 33.5MB)
// 테스트 8 〉	통과 (0.07ms, 33.1MB)
// 테스트 9 〉	통과 (0.10ms, 33.4MB)
// 테스트 10 〉	통과 (0.07ms, 33.5MB)
// 테스트 11 〉	통과 (0.10ms, 33.4MB)
// 테스트 12 〉	통과 (0.20ms, 33.5MB)
// 테스트 13 〉	통과 (0.19ms, 33.4MB)
// 테스트 14 〉	통과 (0.26ms, 33.4MB)
