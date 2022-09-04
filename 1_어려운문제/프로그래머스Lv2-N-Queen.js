function check(queens, row) {
  // 이전까지 두었던 퀸의 위치를 확인한다.
  for (let i = 0; i < row; i += 1) {
    // 행의 위치와 대각선의 위치를 체크한다.
    if (queens[i] === queens[row] || Math.abs(queens[i] - queens[row]) === row - i) {
      return false // 둘 수 없다면 false
    }
  }

  return true // 모두 통과되면 true
}

function search(queens, row) {
  const n = queens.length
  let count = 0

  if (n === row) {
    // 체스판 끝에 도달했다면.. 재귀의 탈출 조건
    return 1
  }

  for (let col = 0; col < n; col += 1) {
    // 0부터 n까지 열을 돌면 둘 수 있게 만든다.
    queens[row] = col // 우선 퀸을 둔다
    if (check(queens, row)) {
      // 퀸을 둘 수 있다면..
      count += search(queens, row + 1) // 다음 행으로 이동!
    }
  }

  return count
}

function solution(n) {
  // 미리 n개 만큼의 배열을 초기화한다. 0번 행부터 시작한다.
  const queens = Array.from({ length: n }, () => 0)
  return search(queens, 0)
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.09ms, 33.5MB)
// 테스트 2 〉	통과 (0.09ms, 33.4MB)
// 테스트 3 〉	통과 (0.18ms, 33.4MB)
// 테스트 4 〉	통과 (0.22ms, 33.4MB)
// 테스트 5 〉	통과 (0.55ms, 33.4MB)
// 테스트 6 〉	통과 (25.38ms, 36.5MB)
// 테스트 7 〉	통과 (28.37ms, 36.5MB)
// 테스트 8 〉	통과 (39.90ms, 36.5MB)
// 테스트 9 〉	통과 (9.72ms, 35.5MB)
// 테스트 10 〉	통과 (39.26ms, 35.7MB)
// 테스트 11 〉	통과 (240.05ms, 36.5MB)

// 다른방법
function solution(n) {
  let count = 0
  const checkX = Array.from({ length: n }, (v, i) => false)
  const checkD1 = Array.from({ length: n * 2 }, (v, i) => false)
  const checkD2 = Array.from({ length: n * 2 }, (v, i) => false)

  const search = (row) => {
    if (row === n) {
      count++
      return
    }

    for (let x = 0; x < n; x++) {
      const d1 = row + x
      const d2 = row - x + n
      if (checkX[x] || checkD1[d1] || checkD2[d2]) {
        continue
      }
      checkX[x] = true
      checkD1[d1] = true
      checkD2[d2] = true

      search(row + 1)

      checkX[x] = false
      checkD1[d1] = false
      checkD2[d2] = false
    }
  }

  search(0)

  return count
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.19ms, 33.5MB)
// 테스트 2 〉	통과 (0.12ms, 33.6MB)
// 테스트 3 〉	통과 (0.21ms, 33.4MB)
// 테스트 4 〉	통과 (0.24ms, 33.4MB)
// 테스트 5 〉	통과 (0.26ms, 33.4MB)
// 테스트 6 〉	통과 (0.42ms, 33.6MB)
// 테스트 7 〉	통과 (1.41ms, 36.8MB)
// 테스트 8 〉	통과 (3.86ms, 36.8MB)
// 테스트 9 〉	통과 (6.20ms, 36.8MB)
// 테스트 10 〉	통과 (18.84ms, 36.8MB)
// 테스트 11 〉	통과 (88.07ms, 36.8MB)
