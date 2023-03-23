function solution(routes) {
  // 빠져나간 시점 순으로 정렬
  routes = routes.sort((a, b) => a[1] - b[1])
  const cameras = []
  const meet = (i, j) => {
    for (const x of cameras) {
      if (i <= x && x <= j) {
        return true
      }
    }
    return false
  }

  for (const [i, j] of routes) {
    if (!meet(i, j)) {
      cameras.push(j)
    }
  }

  return cameras.length
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.26ms, 33.7MB)
// 테스트 2 〉	통과 (0.27ms, 33.7MB)
// 테스트 3 〉	통과 (0.31ms, 33.6MB)
// 테스트 4 〉	통과 (0.29ms, 33.7MB)
// 테스트 5 〉	통과 (0.27ms, 33.6MB)
// 효율성  테스트
// 테스트 1 〉	통과 (4.23ms, 36.7MB)
// 테스트 2 〉	통과 (3.23ms, 36.9MB)
// 테스트 3 〉	통과 (5.67ms, 37MB)
// 테스트 4 〉	통과 (0.38ms, 33.5MB)
// 테스트 5 〉	통과 (6.56ms, 37.3MB)
