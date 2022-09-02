function compare(a, b) {
  const [key1, value1] = a
  const [key2, value2] = b
  if (value1 < value2) return 1
  if (value1 > value2) return -1
  if (key1 <= key2) return -1
  return 1
}

function solution(N, stages) {
  const stageTable = stages.reduce((table, stage) => {
    if (stage <= N) {
      if (!table[stage]) {
        table[stage] = 0
      }
      table[stage] += 1
    }
    return table
  }, {})

  let allUsersLength = stages.length

  const failureTable = Array.from({ length: N }, (_, i) => i + 1).map((stage) => {
    if (!stageTable[stage]) stageTable[stage] = 0
    const failure = stageTable[stage] / allUsersLength
    allUsersLength -= stageTable[stage]
    if (allUsersLength < 0) throw new Error('범위를 벗어남')
    return [stage, failure]
  })
  return [...failureTable].sort(compare).map(([key, value]) => key)
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.35ms, 29.8MB)
// 테스트 2 〉	통과 (0.43ms, 30.1MB)
// 테스트 3 〉	통과 (4.34ms, 33.1MB)
// 테스트 4 〉	통과 (4.08ms, 34.2MB)
// 테스트 5 〉	통과 (8.80ms, 37.7MB)
// 테스트 6 〉	통과 (0.60ms, 30.4MB)
// 테스트 7 〉	통과 (1.73ms, 32.7MB)
// 테스트 8 〉	통과 (4.20ms, 34.2MB)
// 테스트 9 〉	통과 (7.53ms, 37.8MB)
// 테스트 10 〉	통과 (3.83ms, 34MB)
// 테스트 11 〉	통과 (4.26ms, 34.3MB)
// 테스트 12 〉	통과 (4.69ms, 35.5MB)
// 테스트 13 〉	통과 (5.71ms, 35.9MB)
// 테스트 14 〉	통과 (0.37ms, 30.1MB)
// 테스트 15 〉	통과 (3.12ms, 33.9MB)
// 테스트 16 〉	통과 (2.34ms, 32.6MB)
// 테스트 17 〉	통과 (2.95ms, 33.9MB)
// 테스트 18 〉	통과 (2.45ms, 32.8MB)
// 테스트 19 〉	통과 (0.77ms, 30.5MB)
// 테스트 20 〉	통과 (2.58ms, 32.4MB)
// 테스트 21 〉	통과 (3.52ms, 33.9MB)
// 테스트 22 〉	통과 (5.75ms, 37.2MB)
// 테스트 23 〉	통과 (6.11ms, 36.2MB)
// 테스트 24 〉	통과 (5.46ms, 36.6MB)
// 테스트 25 〉	통과 (0.35ms, 30.1MB)
// 테스트 26 〉	통과 (0.27ms, 30MB)
// 테스트 27 〉	통과 (0.14ms, 30.1MB)
