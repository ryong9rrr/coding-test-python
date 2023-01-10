function solution(bridge_length, weight, truck_weights) {
  const q = [...truck_weights]
  const bridge = []

  let bridgeWeight = 0
  let time = 0
  while (q.length > 0 || bridge.length > 0) {
    time += 1
    if (bridge.length > 0 && bridge[0][1] + bridge_length === time) {
      bridgeWeight -= bridge[0][0]
      bridge.shift()
    }
    if (q.length > 0 && bridgeWeight + q[0] <= weight) {
      const truck = q.shift()
      bridgeWeight += truck
      bridge.push([truck, time])
    }
  }

  return time
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.57ms, 33.5MB)
// 테스트 2 〉	통과 (7.25ms, 36.6MB)
// 테스트 3 〉	통과 (0.20ms, 33.4MB)
// 테스트 4 〉	통과 (4.18ms, 36.6MB)
// 테스트 5 〉	통과 (8.76ms, 36.6MB)
// 테스트 6 〉	통과 (5.77ms, 36.6MB)
// 테스트 7 〉	통과 (0.52ms, 33.4MB)
// 테스트 8 〉	통과 (0.22ms, 33.5MB)
// 테스트 9 〉	통과 (3.16ms, 36.6MB)
// 테스트 10 〉	통과 (0.27ms, 33.4MB)
// 테스트 11 〉	통과 (0.16ms, 33.5MB)
// 테스트 12 〉	통과 (0.27ms, 33.4MB)
// 테스트 13 〉	통과 (0.41ms, 33.5MB)
// 테스트 14 〉	통과 (0.14ms, 33.5MB)
