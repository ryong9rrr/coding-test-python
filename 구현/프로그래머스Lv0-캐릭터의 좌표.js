function solution(keyinput, board) {
  const limitX = (board[0] - 1) / 2
  const limitY = (board[1] - 1) / 2

  const commands = {
    up: [0, 1],
    down: [0, -1],
    left: [-1, 0],
    right: [1, 0],
  }

  let x = 0
  let y = 0

  keyinput.forEach((command) => {
    const [dx, dy] = commands[command]
    const nx = x + dx
    const ny = y + dy
    if (Math.abs(nx) <= limitX && Math.abs(ny) <= limitY) {
      x = nx
      y = ny
    }
  })

  return [x, y]
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.20ms, 33.5MB)
// 테스트 2 〉	통과 (0.06ms, 33MB)
// 테스트 3 〉	통과 (0.19ms, 33.5MB)
// 테스트 4 〉	통과 (0.10ms, 33.1MB)
// 테스트 5 〉	통과 (0.10ms, 33.5MB)
// 테스트 6 〉	통과 (0.09ms, 33.6MB)
// 테스트 7 〉	통과 (0.20ms, 33.6MB)
// 테스트 8 〉	통과 (0.22ms, 33.4MB)
// 테스트 9 〉	통과 (0.21ms, 33.5MB)
// 테스트 10 〉	통과 (0.10ms, 33.5MB)
// 테스트 11 〉	통과 (0.16ms, 33.4MB)
