const sumMatrix = (arr1, arr2) => {
  const n = arr1.length
  const m = arr1[0].length

  const result = []
  for (let i = 0; i < n; i++) {
    const temp = []
    for (let j = 0; j < m; j++) {
      const x = arr1[i][j]
      const y = arr2[i][j]
      temp.push(x + y)
    }
    result.push(temp)
  }
  return result
}

function solution(arr1, arr2) {
  return sumMatrix(arr1, arr2)
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.08ms, 29.8MB)
// 테스트 2 〉	통과 (0.11ms, 30.1MB)
// 테스트 3 〉	통과 (0.24ms, 30.2MB)
// 테스트 4 〉	통과 (0.16ms, 29.9MB)
// 테스트 5 〉	통과 (0.12ms, 30.1MB)
// 테스트 6 〉	통과 (0.15ms, 30.1MB)
// 테스트 7 〉	통과 (0.07ms, 30MB)
// 테스트 8 〉	통과 (0.13ms, 30.1MB)
// 테스트 9 〉	통과 (0.74ms, 33.8MB)
// 테스트 10 〉	통과 (0.59ms, 33.6MB)
// 테스트 11 〉	통과 (0.42ms, 34MB)
// 테스트 12 〉	통과 (0.46ms, 33.7MB)
// 테스트 13 〉	통과 (0.66ms, 33.8MB)
// 테스트 14 〉	통과 (0.47ms, 33.7MB)
// 테스트 15 〉	통과 (0.86ms, 33.7MB)
// 테스트 16 〉	통과 (0.56ms, 33.9MB)
// 테스트 17 〉	통과 (13.03ms, 64.8MB)
