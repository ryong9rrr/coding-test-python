// 원본배열 유지 정렬, 정직하게 합 계산
function solution(A, B) {
  const sorted = (array, reverse = false) => {
    if (reverse) {
      return [...array].sort((a, b) => b - a)
    }
    return [...array].sort((a, b) => a - b)
  }
  const n = A.length
  const a = sorted(A)
  const b = sorted(B, true)
  let total = 0

  for (let i = 0; i < n; i++) {
    total += a[i] * b[i]
  }

  return total
}

// 굳이 원본 배열을 유지할 필요가 없으니 그냥 정렬, reduce
function solution(A, B) {
  A.sort((a, b) => a - b)
  B.sort((a, b) => b - a)
  return A.reduce((acc, cur, i) => acc + cur * B[i], 0)
}

/*
정확성  테스트
테스트 1 〉	통과 (0.08ms, 30.1MB)
테스트 2 〉	통과 (0.11ms, 30.1MB)
테스트 3 〉	통과 (0.10ms, 30.1MB)
테스트 4 〉	통과 (0.14ms, 30.3MB)
테스트 5 〉	통과 (0.14ms, 30.1MB)
테스트 6 〉	통과 (0.11ms, 30.1MB)
테스트 7 〉	통과 (0.15ms, 30.2MB)
테스트 8 〉	통과 (0.14ms, 30.2MB)
테스트 9 〉	통과 (0.15ms, 30.2MB)
테스트 10 〉	통과 (0.13ms, 30.3MB)
테스트 11 〉	통과 (0.15ms, 30.1MB)
테스트 12 〉	통과 (0.14ms, 30.2MB)
테스트 13 〉	통과 (0.08ms, 30.3MB)
테스트 14 〉	통과 (0.10ms, 30.3MB)
테스트 15 〉	통과 (0.13ms, 30MB)
테스트 16 〉	통과 (0.13ms, 30.1MB)
효율성  테스트
테스트 1 〉	통과 (0.91ms, 29.9MB)
테스트 2 〉	통과 (0.95ms, 29.9MB)
테스트 3 〉	통과 (0.95ms, 30MB)
테스트 4 〉	통과 (0.93ms, 30.1MB)
*/
