function solution(n, times) {
  const sortedTimes = times.sort((a, b) => a - b)
  let left = sortedTimes[0]
  let right = sortedTimes[sortedTimes.length - 1] * n

  while (left <= right) {
    const mid = Math.floor((left + right) / 2)
    const total = times.reduce((acc, time) => acc + Math.floor(mid / time), 0)

    if (total < n) {
      left = mid + 1
    } else {
      right = mid - 1
    }
  }

  return left
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.10ms, 29.9MB)
// 테스트 2 〉	통과 (0.28ms, 30.1MB)
// 테스트 3 〉	통과 (27.49ms, 31.7MB)
// 테스트 4 〉	통과 (136.87ms, 42.1MB)
// 테스트 5 〉	통과 (160.08ms, 40.2MB)
// 테스트 6 〉	통과 (168.47ms, 42.9MB)
// 테스트 7 〉	통과 (154.91ms, 43.6MB)
// 테스트 8 〉	통과 (154.65ms, 43.7MB)
// 테스트 9 〉	통과 (0.16ms, 29.9MB)

// 합을 구하는 곳에서 최적화
function solution(n, times) {
  const sortedTimes = times.sort((a, b) => a - b)
  let left = sortedTimes[0]
  let right = sortedTimes[sortedTimes.length - 1] * n

  while (left <= right) {
    const mid = Math.floor((left + right) / 2)
    let total = 0
    for (const time of times) {
      total += Math.floor(mid / time)
      if (total >= n) {
        break
      }
    }

    if (total < n) {
      left = mid + 1
    } else {
      right = mid - 1
    }
  }

  return left
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.12ms, 30.1MB)
// 테스트 2 〉	통과 (0.20ms, 30.3MB)
// 테스트 3 〉	통과 (4.27ms, 33MB)
// 테스트 4 〉	통과 (54.69ms, 40.9MB)
// 테스트 5 〉	통과 (63.79ms, 41.4MB)
// 테스트 6 〉	통과 (53.30ms, 39.7MB)
// 테스트 7 〉	통과 (56.74ms, 39.5MB)
// 테스트 8 〉	통과 (60.63ms, 39.4MB)
// 테스트 9 〉	통과 (0.11ms, 30.1MB)
