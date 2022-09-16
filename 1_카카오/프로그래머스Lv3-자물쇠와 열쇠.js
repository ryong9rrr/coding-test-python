// N x M 행렬을 만드는 함수
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

// N x N 행렬을 오른쪽으로 90도 회전하는 함수
function rotateMatrix90(matrix) {
  const N = matrix.length
  const result = makeMatrix(N, N, 0)
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      result[j][N - i - 1] = matrix[i][j]
    }
  }
  return result
}

function solution(key, lock) {
  const lenLock = lock.length
  const lenKey = key.length
  const extendedSide = lenKey - 1
  const extendedRange = extendedSide * 2 + lenLock

  // 확장된 행렬 만들기
  const extendedMatrix = makeMatrix(extendedRange, extendedRange, 0)
  for (let i = 0; i < lenLock; i++) {
    for (let j = 0; j < lenLock; j++) {
      const x = i + extendedSide
      const y = j + extendedSide
      extendedMatrix[x][y] = lock[i][j]
    }
  }

  // 확장된 행렬에서 lock 부분을 체크하는 함수.
  // 모두 1일 때 딱 맞춰진 상태가 된다.
  function checkLock() {
    for (let x = 0; x < lenLock; x++) {
      for (let y = 0; y < lenLock; y++) {
        if (extendedMatrix[x + extendedSide][y + extendedSide] !== 1) {
          return false
        }
      }
    }
    return true
  }

  // 완전탐색
  let N = 4
  while (N--) {
    key = rotateMatrix90(key)
    for (let x = 0; x < extendedSide + lenLock; x++) {
      for (let y = 0; y < extendedSide + lenLock; y++) {
        // key를 넣어본다.
        for (let i = 0; i < lenKey; i++) {
          for (let j = 0; j < lenKey; j++) {
            extendedMatrix[x + i][y + j] += key[i][j]
          }
        }
        // 넣은 상태로 자물쇠 확인
        if (checkLock()) {
          return true
        }
        // key를 다시 뺀다.
        for (let i = 0; i < lenKey; i++) {
          for (let j = 0; j < lenKey; j++) {
            extendedMatrix[x + i][y + j] -= key[i][j]
          }
        }
      }
    }
  }
  return false
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.51ms, 33.4MB)
// 테스트 2 〉	통과 (0.52ms, 33.5MB)
// 테스트 3 〉	통과 (5.65ms, 36.9MB)
// 테스트 4 〉	통과 (0.35ms, 33.4MB)
// 테스트 5 〉	통과 (21.58ms, 37.7MB)
// 테스트 6 〉	통과 (18.85ms, 37.6MB)
// 테스트 7 〉	통과 (21.69ms, 36.6MB)
// 테스트 8 〉	통과 (10.16ms, 37.3MB)
// 테스트 9 〉	통과 (18.79ms, 37.7MB)
// 테스트 10 〉	통과 (31.62ms, 38.1MB)
// 테스트 11 〉	통과 (33.55ms, 38.2MB)
// 테스트 12 〉	통과 (0.26ms, 33.4MB)
// 테스트 13 〉	통과 (6.18ms, 36.9MB)
// 테스트 14 〉	통과 (0.67ms, 33.5MB)
// 테스트 15 〉	통과 (5.75ms, 36.9MB)
// 테스트 16 〉	통과 (17.89ms, 37.7MB)
// 테스트 17 〉	통과 (27.63ms, 38.1MB)
// 테스트 18 〉	통과 (9.93ms, 36.9MB)
// 테스트 19 〉	통과 (0.48ms, 33.4MB)
// 테스트 20 〉	통과 (23.42ms, 37.6MB)
// 테스트 21 〉	통과 (26.83ms, 37.9MB)
// 테스트 22 〉	통과 (16.80ms, 37.6MB)
// 테스트 23 〉	통과 (10.97ms, 37.7MB)
// 테스트 24 〉	통과 (11.32ms, 36.6MB)
// 테스트 25 〉	통과 (23.01ms, 37.7MB)
// 테스트 26 〉	통과 (30.63ms, 37.7MB)
// 테스트 27 〉	통과 (39.05ms, 38.1MB)
// 테스트 28 〉	통과 (19.55ms, 37.9MB)
// 테스트 29 〉	통과 (11.16ms, 37.5MB)
// 테스트 30 〉	통과 (17.47ms, 37.7MB)
// 테스트 31 〉	통과 (21.68ms, 38.1MB)
// 테스트 32 〉	통과 (34.72ms, 38MB)
// 테스트 33 〉	통과 (30.93ms, 38MB)
// 테스트 34 〉	통과 (1.16ms, 33.5MB)
// 테스트 35 〉	통과 (0.98ms, 33.4MB)
// 테스트 36 〉	통과 (1.68ms, 33.5MB)
// 테스트 37 〉	통과 (1.08ms, 33.5MB)
// 테스트 38 〉	통과 (0.44ms, 33.6MB)
