const divide = (n, i, j, arr) => {
  if (n <= 1) {
    return String(arr[i][j])
  }
  const mid = n / 2
  const a = divide(mid, i, j, arr)
  const b = divide(mid, i, j + mid, arr)
  const c = divide(mid, i + mid, j, arr)
  const d = divide(mid, i + mid, j + mid, arr)

  if (a.length === 1 && a === b && b === c && c === d) {
    return a
  }
  return `(${a + b + c + d})`
}

function solution(arr) {
  const result = divide(arr.length, 0, 0, arr)

  let countZero = 0
  let countOne = 0

  for (const i of result) {
    if (i === "0") {
      countZero += 1
    } else if (i === "1") {
      countOne += 1
    }
  }

  return [countZero, countOne]
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.36ms, 33.5MB)
// 테스트 2 〉	통과 (0.36ms, 33.5MB)
// 테스트 3 〉	통과 (0.26ms, 33.5MB)
// 테스트 4 〉	통과 (0.36ms, 33.4MB)
// 테스트 5 〉	통과 (32.86ms, 49.4MB)
// 테스트 6 〉	통과 (26.84ms, 43.2MB)
// 테스트 7 〉	통과 (21.81ms, 41.4MB)
// 테스트 8 〉	통과 (9.63ms, 40.8MB)
// 테스트 9 〉	통과 (9.33ms, 40.7MB)
// 테스트 10 〉	통과 (29.14ms, 74.6MB)
// 테스트 11 〉	통과 (0.18ms, 33.4MB)
// 테스트 12 〉	통과 (0.19ms, 33.6MB)
// 테스트 13 〉	통과 (7.84ms, 40.8MB)
// 테스트 14 〉	통과 (39.13ms, 74.8MB)
// 테스트 15 〉	통과 (31.35ms, 75.6MB)
// 테스트 16 〉	통과 (14.00ms, 41.7MB)
