function compare(a, b) {
  for (let i = 0; i < a.length; i++) {
    if (a[i] === b[i]) {
      continue
    }
    return a[i] - b[i]
  }
}

function makeMatrix(N, M, defaultValue = 0) {
  const matrix = []
  for (let i = 0; i < N; i++) {
    const row = []
    for (let j = 0; j < M; j++) {
      row.push(defaultValue)
    }
    matrix.push(row)
  }
  return matrix
}

function solution(n, build_frame) {
  const pillars = makeMatrix(n + 1, n + 1, false)
  const beams = makeMatrix(n + 1, n + 1, false)

  function isPossiblePillar(x, y) {
    if (y === 0) return true
    if (beams[x][y] || (x > 0 && beams[x - 1][y])) return true
    if (y > 0 && pillars[x][y - 1]) return true
    return false
  }

  function isPossibleBeam(x, y) {
    if ((y > 0 && pillars[x][y - 1]) || (y > 0 && x < n && pillars[x + 1][y - 1])) return true
    if (x > 0 && beams[x - 1][y] && x < n && beams[x + 1][y]) return true
    return false
  }

  function checkMatrix() {
    for (let x = 0; x < n + 1; x++) {
      for (let y = 0; y < n + 1; y++) {
        if (pillars[x][y] && !isPossiblePillar(x, y)) return false
        if (beams[x][y] && !isPossibleBeam(x, y)) return false
      }
    }
    return true
  }

  function install(x, y, stuff) {
    if (stuff === 0) {
      if (isPossiblePillar(x, y)) {
        pillars[x][y] = true
        return true
      }
    } else {
      if (isPossibleBeam(x, y)) {
        beams[x][y] = true
        return true
      }
    }
    return false
  }

  function remove(x, y, stuff) {
    if (stuff === 0) {
      pillars[x][y] = false
      if (!checkMatrix()) {
        pillars[x][y] = true
        return false
      }
    } else {
      beams[x][y] = false
      if (!checkMatrix()) {
        beams[x][y] = true
        return false
      }
    }
    return true
  }

  const result = []
  for (const [x, y, stuff, command] of build_frame) {
    if (command === 1) {
      if (install(x, y, stuff)) {
        result.push([x, y, stuff])
      }
    } else {
      if (remove(x, y, stuff)) {
        const idx = result.findIndex(([a, b, c]) => a === x && b === y && c === stuff)
        idx > -1 && result.splice(idx, 1)
      }
    }
  }

  return result.sort(compare)
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.84ms, 33.5MB)
// 테스트 2 〉	통과 (0.91ms, 33.4MB)
// 테스트 3 〉	통과 (0.81ms, 33.2MB)
// 테스트 4 〉	통과 (0.77ms, 33.4MB)
// 테스트 5 〉	통과 (0.71ms, 33.4MB)
// 테스트 6 〉	통과 (0.85ms, 33.5MB)
// 테스트 7 〉	통과 (0.60ms, 33.4MB)
// 테스트 8 〉	통과 (0.40ms, 33.5MB)
// 테스트 9 〉	통과 (0.74ms, 33.4MB)
// 테스트 10 〉	통과 (45.14ms, 38.3MB)
// 테스트 11 〉	통과 (54.48ms, 39.4MB)
// 테스트 12 〉	통과 (12.39ms, 37.9MB)
// 테스트 13 〉	통과 (55.19ms, 39.5MB)
// 테스트 14 〉	통과 (21.61ms, 38.9MB)
// 테스트 15 〉	통과 (9.62ms, 39.3MB)
// 테스트 16 〉	통과 (20.98ms, 38.1MB)
// 테스트 17 〉	통과 (17.65ms, 39.5MB)
// 테스트 18 〉	통과 (25.45ms, 39MB)
// 테스트 19 〉	통과 (18.37ms, 38.7MB)
// 테스트 20 〉	통과 (22.43ms, 39.5MB)
// 테스트 21 〉	통과 (25.60ms, 39.1MB)
// 테스트 22 〉	통과 (26.26ms, 38.8MB)
// 테스트 23 〉	통과 (40.60ms, 38.7MB)
