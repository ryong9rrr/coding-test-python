const move = (command, x, y) => {
  const commands = {
    U: [-1, 0],
    L: [0, -1],
    D: [1, 0],
    R: [0, 1],
  }
  const [dx, dy] = commands[command]
  const nx = x + dx
  const ny = y + dy
  if (-5 <= nx && nx <= 5 && -5 <= ny && ny <= 5) {
    return [nx, ny]
  }
  return [x, y]
}

const generateKey = (numbers) => {
  return numbers.map((number) => String(number)).join("#")
}

function solution(dirs) {
  const visited = new Set()
  let x = 0
  let y = 0

  for (const command of dirs) {
    const [nx, ny] = move(command, x, y)
    if (x === nx && y === ny) {
      continue
    }
    const key = generateKey([x, y, nx, ny])
    if (!visited.has(key)) {
      const reverseKey = generateKey([nx, ny, x, y])
      visited.add(key)
      visited.add(reverseKey)
    }
    x = nx
    y = ny
  }
  return Array.from(visited).length / 2
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.44ms, 33.6MB)
// 테스트 2 〉	통과 (0.18ms, 33.5MB)
// 테스트 3 〉	통과 (0.18ms, 33.5MB)
// 테스트 4 〉	통과 (0.63ms, 33.8MB)
// 테스트 5 〉	통과 (0.65ms, 33.7MB)
// 테스트 6 〉	통과 (0.53ms, 33.6MB)
// 테스트 7 〉	통과 (0.43ms, 33.5MB)
// 테스트 8 〉	통과 (0.64ms, 33.5MB)
// 테스트 9 〉	통과 (0.42ms, 33.5MB)
// 테스트 10 〉	통과 (0.43ms, 33.5MB)
// 테스트 11 〉	통과 (0.44ms, 33.6MB)
// 테스트 12 〉	통과 (0.53ms, 33.6MB)
// 테스트 13 〉	통과 (0.54ms, 33.6MB)
// 테스트 14 〉	통과 (0.54ms, 33.6MB)
// 테스트 15 〉	통과 (0.58ms, 33.5MB)
// 테스트 16 〉	통과 (1.20ms, 34MB)
// 테스트 17 〉	통과 (1.23ms, 33.9MB)
// 테스트 18 〉	통과 (1.39ms, 34MB)
// 테스트 19 〉	통과 (1.24ms, 33.9MB)
// 테스트 20 〉	통과 (1.21ms, 34MB)
