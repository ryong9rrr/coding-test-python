// 배열을 이용한 풀이 (마지막에 0번째 인덱스는 제거해야한다)
function solution(n, lost, reserve) {
  const table = Array.from({ length: n + 1 }, (_, i) => 1)
  lost.forEach((i) => (table[i] -= 1))
  reserve.forEach((i) => (table[i] += 1))

  const ID_LIST = Array.from({ length: n }, (_, i) => i + 1)
  ID_LIST.forEach((i) => {
    if (table[i] === 0) {
      if (i > 0 && table[i - 1] > 1) {
        table[i - 1] -= 1
        table[i] += 1
      } else if (i < n && table[i + 1] > 1) {
        table[i + 1] -= 1
        table[i] += 1
      }
    }
  })

  // 0번째 인덱스 제거
  return table.filter((id) => id !== 0).length - 1
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.45ms, 30MB)
// 테스트 2 〉	통과 (0.32ms, 30MB)
// 테스트 3 〉	통과 (0.41ms, 30MB)
// 테스트 4 〉	통과 (0.32ms, 30.2MB)
// 테스트 5 〉	통과 (0.17ms, 30.3MB)
// 테스트 6 〉	통과 (0.17ms, 30.1MB)
// 테스트 7 〉	통과 (0.20ms, 29.9MB)
// 테스트 8 〉	통과 (0.17ms, 30MB)
// 테스트 9 〉	통과 (0.43ms, 29.8MB)
// 테스트 10 〉	통과 (0.18ms, 30.2MB)
// 테스트 11 〉	통과 (0.15ms, 29.9MB)
// 테스트 12 〉	통과 (0.35ms, 29.7MB)
// 테스트 13 〉	통과 (0.29ms, 30.1MB)
// 테스트 14 〉	통과 (0.13ms, 29.7MB)
// 테스트 15 〉	통과 (0.16ms, 29.9MB)
// 테스트 16 〉	통과 (0.14ms, 30.1MB)
// 테스트 17 〉	통과 (0.34ms, 30.1MB)
// 테스트 18 〉	통과 (0.17ms, 30.2MB)
// 테스트 19 〉	통과 (0.14ms, 30MB)
// 테스트 20 〉	통과 (0.30ms, 30MB)

// 그냥 1개의 배열로 풀 수 있음.
function solution(n, lost, reserve) {
  const students = Array.from({ length: n + 1 }, (v, i) => 1)

  lost.forEach((i) => (students[i] -= 1))
  reserve.forEach((i) => (students[i] += 1))

  for (let i = 1; i < n + 1; i++) {
    if (students[i] !== 0) {
      continue
    }
    if (i > 1 && students[i - 1] > 1) {
      students[i - 1] -= 1
      students[i] += 1
      continue
    }
    if (i < n && students[i + 1] > 1) {
      students[i + 1] -= 1
      students[i] += 1
    }
  }

  return students.slice(1).filter((x) => x > 0).length
}
// 정확성 테스트
// 테스트 1 〉 통과 (0.18ms, 33.5MB)
// 테스트 2 〉 통과 (0.18ms, 33.5MB)
// 테스트 3 〉 통과 (0.18ms, 33.4MB)
// 테스트 4 〉 통과 (0.11ms, 33.6MB)
// 테스트 5 〉 통과 (0.19ms, 33.5MB)
// 테스트 6 〉 통과 (0.10ms, 33.5MB)
// 테스트 7 〉 통과 (0.20ms, 33.5MB)
// 테스트 8 〉 통과 (0.11ms, 33.4MB)
// 테스트 9 〉 통과 (0.11ms, 33.5MB)
// 테스트 10 〉 통과 (0.18ms, 33.6MB)
// 테스트 11 〉 통과 (0.10ms, 33.6MB)
// 테스트 12 〉 통과 (0.10ms, 33.5MB)
// 테스트 13 〉 통과 (0.10ms, 33.4MB)
// 테스트 14 〉 통과 (0.11ms, 33.5MB)
// 테스트 15 〉 통과 (0.10ms, 33.5MB)
// 테스트 16 〉 통과 (0.12ms, 33.5MB)
// 테스트 17 〉 통과 (0.10ms, 33.6MB)
// 테스트 18 〉 통과 (0.10ms, 33.4MB)
// 테스트 19 〉 통과 (0.10ms, 33.5MB)
// 테스트 20 〉 통과 (0.10ms, 33.5MB)
