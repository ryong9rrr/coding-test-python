function solution(n, times) {
  times = times.sort((a, b) => a - b)
  let left = times[0]
  let right = times[times.length - 1] * n

  const isEnough = (mid) => {
    let acc = 0
    for (const t of times) {
      acc += Math.floor(mid / t)
      if (acc >= n) {
        return true
      }
    }
    return false
  }

  while (left < right) {
    const mid = Math.floor(left / 2 + right / 2)
    if (isEnough(mid)) {
      right = mid
    } else {
      left = mid + 1
    }
  }

  return left
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.21ms, 33.5MB)
// 테스트 2 〉	통과 (0.29ms, 33.6MB)
// 테스트 3 〉	통과 (3.30ms, 37.7MB)
// 테스트 4 〉	통과 (52.87ms, 42.5MB)
// 테스트 5 〉	통과 (55.00ms, 40.7MB)
// 테스트 6 〉	통과 (49.63ms, 40.1MB)
// 테스트 7 〉	통과 (46.97ms, 42.6MB)
// 테스트 8 〉	통과 (55.60ms, 40.7MB)
// 테스트 9 〉	통과 (0.20ms, 33.4MB)
