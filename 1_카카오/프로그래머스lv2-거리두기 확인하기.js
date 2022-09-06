//dfs 조합 함수를 이용
function combine(array, k) {
  const results = []
  function dfs(elements, start, k) {
    if (k === 0) {
      results.push([...elements])
      return
    }
    for (let i = start; i < array.length; i++) {
      elements.push(array[i])
      dfs(elements, i + 1, k - 1)
      elements.pop()
    }
  }
  dfs([], 0, k)
  return results
}

function getMht([x1, y1], [x2, y2]) {
  return Math.abs(x1 - x2) + Math.abs(y1 - y2)
}

function isWell(seats, place) {
  const combis = combine(seats, 2)
  for (const [a, b] of combis) {
    const mht = getMht(a, b)
    if (mht === 1) return 0
    if (mht === 2) {
      const [x1, y1] = a
      const [x2, y2] = b

      if (x1 === x2 && place[x1][Math.max(y1, y2) - 1] === 'O') {
        return 0
      }

      if (y1 === y2 && place[Math.max(x1, x2) - 1][y1] === 'O') {
        return 0
      }

      if (x1 !== x2 && y1 !== y2 && (place[x1][y2] === 'O' || place[x2][y1] === 'O')) {
        return 0
      }
    }
  }

  return 1
}

function search(place) {
  const seats = []
  for (let i = 0; i < 5; i++) {
    for (let j = 0; j < 5; j++) {
      if (place[i][j] === 'P') {
        seats.push([i, j])
      }
    }
  }
  return seats
}

function solution(places) {
  return places.map((place) => {
    const seats = search(place)
    return isWell(seats, place)
  })
}
// 정확성 테스트
// 테스트 1 〉 통과 (0.90ms, 33.6MB)
// 테스트 2 〉 통과 (0.40ms, 33.6MB)
// 테스트 3 〉 통과 (0.36ms, 33.6MB)
// 테스트 4 〉 통과 (0.39ms, 33.5MB)
// 테스트 5 〉 통과 (0.34ms, 33.6MB)
// 테스트 6 〉 통과 (0.55ms, 33.6MB)
// 테스트 7 〉 통과 (0.36ms, 33.6MB)
// 테스트 8 〉 통과 (0.38ms, 33.6MB)
// 테스트 9 〉 통과 (0.36ms, 33.6MB)
// 테스트 10 〉 통과 (0.36ms, 33.5MB)
// 테스트 11 〉 통과 (0.36ms, 33.7MB)
// 테스트 12 〉 통과 (0.35ms, 33.5MB)
// 테스트 13 〉 통과 (0.57ms, 33.6MB)
// 테스트 14 〉 통과 (0.32ms, 33.6MB)
// 테스트 15 〉 통과 (0.42ms, 33.6MB)
// 테스트 16 〉 통과 (0.51ms, 33.6MB)
// 테스트 17 〉 통과 (0.67ms, 33.6MB)
// 테스트 18 〉 통과 (0.39ms, 33.6MB)
// 테스트 19 〉 통과 (0.41ms, 33.5MB)
// 테스트 20 〉 통과 (0.73ms, 33.6MB)
// 테스트 21 〉 통과 (0.40ms, 33.5MB)
// 테스트 22 〉 통과 (0.37ms, 33.5MB)
// 테스트 23 〉 통과 (0.25ms, 33.5MB)
// 테스트 24 〉 통과 (1.34ms, 33.7MB)
// 테스트 25 〉 통과 (0.39ms, 33.5MB)
// 테스트 26 〉 통과 (0.38ms, 33.6MB)
// 테스트 27 〉 통과 (0.34ms, 33.5MB)
// 테스트 28 〉 통과 (0.41ms, 33.5MB)
// 테스트 29 〉 통과 (0.48ms, 33.6MB)
// 테스트 30 〉 통과 (0.31ms, 33.5MB)
// 테스트 31 〉 통과 (0.35ms, 33.5MB)

// 조합을 구한뒤에 체크하지 않고, 조합을 구하면서 바로 체크 => 불필요한 루프가 줄어서 시간이 2배 빨라졌음
function getMht([x1, y1], [x2, y2]) {
  return Math.abs(x1 - x2) + Math.abs(y1 - y2)
}

function isWell(seats, place) {
  const N = seats.length
  for (let i = 0; i < N - 1; i++) {
    for (let j = i + 1; j < N; j++) {
      const a = seats[i]
      const b = seats[j]
      const mht = getMht(a, b)
      if (mht > 2) continue
      if (mht === 1) return 0
      if (mht === 2) {
        const [x1, y1] = a
        const [x2, y2] = b

        if (x1 === x2 && place[x1][Math.max(y1, y2) - 1] === 'O') {
          return 0
        }

        if (y1 === y2 && place[Math.max(x1, x2) - 1][y1] === 'O') {
          return 0
        }

        if (x1 !== x2 && y1 !== y2 && (place[x1][y2] === 'O' || place[x2][y1] === 'O')) {
          return 0
        }
      }
    }
  }

  return 1
}

function search(place) {
  const seats = []
  for (let i = 0; i < 5; i++) {
    for (let j = 0; j < 5; j++) {
      if (place[i][j] === 'P') {
        seats.push([i, j])
      }
    }
  }
  return seats
}

function solution(places) {
  return places.map((place) => {
    const seats = search(place)
    return isWell(seats, place)
  })
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.42ms, 33.5MB)
// 테스트 2 〉	통과 (0.28ms, 33.4MB)
// 테스트 3 〉	통과 (0.30ms, 33.5MB)
// 테스트 4 〉	통과 (0.35ms, 33.4MB)
// 테스트 5 〉	통과 (0.27ms, 33.4MB)
// 테스트 6 〉	통과 (0.27ms, 33.4MB)
// 테스트 7 〉	통과 (0.27ms, 33.4MB)
// 테스트 8 〉	통과 (0.28ms, 33.4MB)
// 테스트 9 〉	통과 (0.29ms, 33.4MB)
// 테스트 10 〉	통과 (0.27ms, 33.4MB)
// 테스트 11 〉	통과 (0.30ms, 33.4MB)
// 테스트 12 〉	통과 (0.27ms, 33.4MB)
// 테스트 13 〉	통과 (0.44ms, 33.1MB)
// 테스트 14 〉	통과 (0.26ms, 33.4MB)
// 테스트 15 〉	통과 (0.25ms, 33.4MB)
// 테스트 16 〉	통과 (0.26ms, 33.5MB)
// 테스트 17 〉	통과 (0.29ms, 33.4MB)
// 테스트 18 〉	통과 (0.26ms, 33.4MB)
// 테스트 19 〉	통과 (0.27ms, 33.5MB)
// 테스트 20 〉	통과 (0.30ms, 33.4MB)
// 테스트 21 〉	통과 (0.27ms, 33.5MB)
// 테스트 22 〉	통과 (0.30ms, 33.4MB)
// 테스트 23 〉	통과 (0.20ms, 33.4MB)
// 테스트 24 〉	통과 (0.28ms, 33.6MB)
// 테스트 25 〉	통과 (0.21ms, 33.4MB)
// 테스트 26 〉	통과 (0.20ms, 33.4MB)
// 테스트 27 〉	통과 (0.32ms, 33.5MB)
// 테스트 28 〉	통과 (0.25ms, 33.3MB)
// 테스트 29 〉	통과 (0.36ms, 33.5MB)
// 테스트 30 〉	통과 (0.24ms, 33.4MB)
// 테스트 31 〉	통과 (0.25ms, 33.5MB)
