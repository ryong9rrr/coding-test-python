// matrix: string[][] => [number, number][]
function getSeats(matrix) {
  const seats = []
  for (let n = 0; n < 5; n++) {
    for (let m = 0; m < 5; m++) {
      if (matrix[n][m] === 'P') {
        seats.push([n, m])
      }
    }
  }
  return seats
}

// seats: [number, number][], place: string[][] => number
function checkMht(seats, place) {
  const n = seats.length
  for (let i = 0; i < n - 1; i++) {
    for (let j = i + 1; j < n; j++) {
      const [x1, y1] = seats[i]
      const [x2, y2] = seats[j]
      const mht = Math.abs(x1 - x2) + Math.abs(y1 - y2)
      if (mht === 1) return 0
      else if (mht === 2) {
        if (x1 === x2 && place[x1][y2 - 1] === 'O') return 0
        else if (y1 === y2 && place[x2 - 1][y1] === 'O') return 0
        else if (place[x1][y2] === 'O' || place[x2][y1] === 'O') return 0
      }
    }
  }
  return 1
}

function solution(places) {
  const result = []
  places.forEach((place) => {
    const peopleSeats = getSeats(place)
    result.push(checkMht(peopleSeats, place))
  })
  return result
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.24ms, 30.2MB)
// 테스트 2 〉	통과 (0.20ms, 30.3MB)
// 테스트 3 〉	통과 (0.22ms, 30.1MB)
// 테스트 4 〉	통과 (0.18ms, 30.3MB)
// 테스트 5 〉	통과 (0.21ms, 30.3MB)
// 테스트 6 〉	통과 (0.20ms, 30.2MB)
// 테스트 7 〉	통과 (0.18ms, 30.2MB)
// 테스트 8 〉	통과 (0.21ms, 30.2MB)
// 테스트 9 〉	통과 (0.21ms, 30.3MB)
// 테스트 10 〉	통과 (0.20ms, 30.1MB)
// 테스트 11 〉	통과 (0.20ms, 29.9MB)
// 테스트 12 〉	통과 (0.20ms, 30.2MB)
// 테스트 13 〉	통과 (0.20ms, 30.2MB)
// 테스트 14 〉	통과 (0.21ms, 30.1MB)
// 테스트 15 〉	통과 (0.20ms, 30.1MB)
// 테스트 16 〉	통과 (0.17ms, 30.2MB)
// 테스트 17 〉	통과 (0.20ms, 30MB)
// 테스트 18 〉	통과 (0.22ms, 30.1MB)
// 테스트 19 〉	통과 (0.19ms, 29.9MB)
// 테스트 20 〉	통과 (0.21ms, 30.1MB)
// 테스트 21 〉	통과 (0.20ms, 30MB)
// 테스트 22 〉	통과 (0.20ms, 30MB)
// 테스트 23 〉	통과 (0.18ms, 30.3MB)
// 테스트 24 〉	통과 (0.20ms, 29.9MB)
// 테스트 25 〉	통과 (0.16ms, 30.1MB)
// 테스트 26 〉	통과 (0.18ms, 30.3MB)
// 테스트 27 〉	통과 (0.19ms, 30.1MB)
// 테스트 28 〉	통과 (0.19ms, 30.1MB)
// 테스트 29 〉	통과 (0.19ms, 30.3MB)
// 테스트 30 〉	통과 (0.16ms, 30MB)

//22년 8월 풀이 - 조합 함수를 이용
function combine(nums, k) {
  const results = []

  function dfs(elements, start, k) {
    if (k === 0) {
      results.push([...elements])
      return
    }

    for (let i = start; i < nums.length; i++) {
      elements.push(nums[i])
      dfs(elements, i + 1, k - 1)
      elements.pop()
    }
  }
  dfs([], 0, k)
  return results
}

const checkMht = (people, place) => {
  for (const [a, b] of people) {
    const [x1, y1] = a
    const [x2, y2] = b
    const mht = Math.abs(x1 - x2) + Math.abs(y1 - y2)
    if (mht < 2) {
      return 0
    }
    if (mht === 2) {
      if (x1 === x2 && place[x1][Math.max(y1, y2) - 1] === 'O') {
        return 0
      }
      if (y1 === y2 && place[Math.max(x1, x2) - 1][y1] === 'O') {
        return 0
      }
      if (place[x2][y1] === 'O' || place[x1][y2] === 'O') {
        return 0
      }
    }
  }
  return 1
}

const getPeople = (place) => {
  const people = []
  for (let i = 0; i < 5; i++) {
    for (let j = 0; j < 5; j++) {
      if (place[i][j] === 'P') {
        people.push([i, j])
      }
    }
  }
  return people
}

function solution(places) {
  return places.map((place) => {
    const people = getPeople(place)
    const combinations = combine(people, 2)
    return checkMht(combinations, place)
  })
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.37ms, 30MB)
// 테스트 2 〉	통과 (0.28ms, 29.7MB)
// 테스트 3 〉	통과 (0.28ms, 30MB)
// 테스트 4 〉	통과 (0.26ms, 30MB)
// 테스트 5 〉	통과 (0.34ms, 30MB)
// 테스트 6 〉	통과 (0.29ms, 30MB)
// 테스트 7 〉	통과 (0.29ms, 29.8MB)
// 테스트 8 〉	통과 (0.28ms, 30.1MB)
// 테스트 9 〉	통과 (0.30ms, 29.9MB)
// 테스트 10 〉	통과 (0.30ms, 30MB)
// 테스트 11 〉	통과 (0.43ms, 29.9MB)
// 테스트 12 〉	통과 (0.28ms, 30.1MB)
// 테스트 13 〉	통과 (0.31ms, 30MB)
// 테스트 14 〉	통과 (0.26ms, 30MB)
// 테스트 15 〉	통과 (0.28ms, 30MB)
// 테스트 16 〉	통과 (0.33ms, 30MB)
// 테스트 17 〉	통과 (0.31ms, 30MB)
// 테스트 18 〉	통과 (0.30ms, 30.1MB)
// 테스트 19 〉	통과 (0.29ms, 29.9MB)
// 테스트 20 〉	통과 (0.30ms, 29.9MB)
// 테스트 21 〉	통과 (0.33ms, 30MB)
// 테스트 22 〉	통과 (0.30ms, 30MB)
// 테스트 23 〉	통과 (0.21ms, 29.9MB)
// 테스트 24 〉	통과 (0.55ms, 29.8MB)
// 테스트 25 〉	통과 (0.25ms, 30MB)
// 테스트 26 〉	통과 (0.21ms, 29.9MB)
// 테스트 27 〉	통과 (0.27ms, 30.1MB)
// 테스트 28 〉	통과 (0.26ms, 30MB)
// 테스트 29 〉	통과 (0.26ms, 30.2MB)
// 테스트 30 〉	통과 (0.25ms, 30MB)
// 테스트 31 〉	통과 (0.30ms, 29.9MB)
