//하나의 큐 + reduce
function solution(bridge_length, weight, truck_weights) {
  const bridge = []

  let time = 0

  while (bridge.length > 0 || truck_weights.length > 0) {
    time++
    if (bridge.length > 0 && bridge[0][1] + bridge_length === time) {
      bridge.shift()
    }

    let total = bridge.reduce((cur, acc) => cur + acc[0], 0)

    if (truck_weights.length > 0 && truck_weights[truck_weights.length - 1] + total <= weight) {
      bridge.push([truck_weights.pop(), time])
    }
  }

  return time
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.74ms, 29.9MB)
// 테스트 2 〉	통과 (6.22ms, 33MB)
// 테스트 3 〉	통과 (0.13ms, 29.8MB)
// 테스트 4 〉	통과 (7.60ms, 32.2MB)
// 테스트 5 〉	통과 (15.51ms, 32.1MB)
// 테스트 6 〉	통과 (10.11ms, 32.2MB)
// 테스트 7 〉	통과 (0.52ms, 30.2MB)
// 테스트 8 〉	통과 (0.20ms, 30.1MB)
// 테스트 9 〉	통과 (3.86ms, 32.9MB)
// 테스트 10 〉	통과 (0.17ms, 29.5MB)
// 테스트 11 〉	통과 (0.10ms, 30.1MB)
// 테스트 12 〉	통과 (0.29ms, 30MB)
// 테스트 13 〉	통과 (0.76ms, 30.2MB)
// 테스트 14 〉	통과 (0.14ms, 29.9MB)

// 하나의 큐 + reduce 사용안함
function solution(bridge_length, weight, truck_weights) {
  const bridge = []

  let time = 0
  let total = 0

  while (bridge.length > 0 || truck_weights.length > 0) {
    time++
    if (bridge.length > 0 && bridge[0][1] + bridge_length === time) {
      total -= bridge[0][0]
      bridge.shift()
    }

    if (truck_weights.length > 0 && truck_weights[truck_weights.length - 1] + total <= weight) {
      total += truck_weights[truck_weights.length - 1]
      bridge.push([truck_weights.pop(), time])
    }
  }

  return time
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.34ms, 30.1MB)
// 테스트 2 〉	통과 (4.69ms, 33MB)
// 테스트 3 〉	통과 (0.08ms, 30.2MB)
// 테스트 4 〉	통과 (3.49ms, 32.8MB)
// 테스트 5 〉	통과 (5.10ms, 32.7MB)
// 테스트 6 〉	통과 (3.86ms, 32.8MB)
// 테스트 7 〉	통과 (0.27ms, 30.1MB)
// 테스트 8 〉	통과 (0.11ms, 30.1MB)
// 테스트 9 〉	통과 (3.56ms, 32.6MB)
// 테스트 10 〉	통과 (0.12ms, 29.8MB)
// 테스트 11 〉	통과 (0.08ms, 30.1MB)
// 테스트 12 〉	통과 (0.17ms, 29.9MB)
// 테스트 13 〉	통과 (0.37ms, 30.2MB)
// 테스트 14 〉	통과 (0.08ms, 30.1MB)
