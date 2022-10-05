function solution(N, stages) {
  let k = stages.length
  const table = Array.from({ length: N + 2 }, () => 0)
  stages.forEach((stage) => (table[stage] += 1))

  const failures = []
  for (let stage = 1; stage < N + 1; stage++) {
    const failure = table[stage] > 0 ? table[stage] / k : 0
    failures.push([failure, stage])
    k -= table[stage]
  }

  return [...failures].sort((a, b) => b[0] - a[0]).map((x) => x[1])
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.20ms, 33.5MB)
// 테스트 2 〉	통과 (0.31ms, 33.5MB)
// 테스트 3 〉	통과 (1.78ms, 34.3MB)
// 테스트 4 〉	통과 (11.47ms, 38MB)
// 테스트 5 〉	통과 (26.49ms, 40.9MB)
// 테스트 6 〉	통과 (0.45ms, 33.6MB)
// 테스트 7 〉	통과 (2.54ms, 34MB)
// 테스트 8 〉	통과 (10.88ms, 38MB)
// 테스트 9 〉	통과 (20.13ms, 40.8MB)
// 테스트 10 〉	통과 (9.87ms, 37.9MB)
// 테스트 11 〉	통과 (18.41ms, 38.1MB)
// 테스트 12 〉	통과 (22.49ms, 38.8MB)
// 테스트 13 〉	통과 (14.36ms, 39.5MB)
// 테스트 14 〉	통과 (0.22ms, 33.4MB)
// 테스트 15 〉	통과 (6.85ms, 36.8MB)
// 테스트 16 〉	통과 (4.13ms, 37.1MB)
// 테스트 17 〉	통과 (6.90ms, 36.9MB)
// 테스트 18 〉	통과 (3.83ms, 37.1MB)
// 테스트 19 〉	통과 (0.87ms, 33.7MB)
// 테스트 20 〉	통과 (5.20ms, 37.7MB)
// 테스트 21 〉	통과 (9.29ms, 37.4MB)
// 테스트 22 〉	통과 (18.57ms, 40.7MB)
// 테스트 23 〉	통과 (17.13ms, 39.9MB)
// 테스트 24 〉	통과 (17.94ms, 40.1MB)
// 테스트 25 〉	통과 (0.10ms, 33.6MB)
// 테스트 26 〉	통과 (0.10ms, 33.5MB)
// 테스트 27 〉	통과 (0.10ms, 33.4MB)
