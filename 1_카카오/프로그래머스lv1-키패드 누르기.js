const PHONE = {
  1: [0, 0],
  2: [0, 1],
  3: [0, 2],
  4: [1, 0],
  5: [1, 1],
  6: [1, 2],
  7: [2, 0],
  8: [2, 1],
  9: [2, 2],
  '*': [3, 0],
  0: [3, 1],
  '#': [3, 2],
}

const getDistance = (number, currentHand) => {
  const [x1, y1] = PHONE[String(number)]
  const [x2, y2] = currentHand
  return Math.abs(x1 - x2) + Math.abs(y1 - y2)
}

function solution(numbers, hand) {
  let currentLeft = PHONE['*']
  let currentRight = PHONE['#']

  return numbers
    .map((number) => {
      if (number === 1 || number === 4 || number === 7) {
        currentLeft = PHONE[number]
        return 'L'
      }

      if (number === 3 || number === 6 || number === 9) {
        currentRight = PHONE[number]
        return 'R'
      }

      const leftDistance = getDistance(number, currentLeft)
      const rightDistance = getDistance(number, currentRight)

      if (leftDistance < rightDistance) {
        currentLeft = PHONE[number]
        return 'L'
      } else if (leftDistance > rightDistance) {
        currentRight = PHONE[number]
        return 'R'
      } else {
        if (hand === 'left') {
          currentLeft = PHONE[number]
          return 'L'
        } else {
          currentRight = PHONE[number]
          return 'R'
        }
      }
    })
    .join('')
}
// 정확성 테스트
// 테스트 1 〉 통과 (0.12ms, 30.3MB)
// 테스트 2 〉 통과 (0.15ms, 30.1MB)
// 테스트 3 〉 통과 (0.15ms, 30.3MB)
// 테스트 4 〉 통과 (0.09ms, 30.2MB)
// 테스트 5 〉 통과 (0.13ms, 30.2MB)
// 테스트 6 〉 통과 (0.15ms, 30.2MB)
// 테스트 7 〉 통과 (0.17ms, 30.1MB)
// 테스트 8 〉 통과 (0.16ms, 30.2MB)
// 테스트 9 〉 통과 (0.17ms, 30.1MB)
// 테스트 10 〉 통과 (0.18ms, 30.2MB)
// 테스트 11 〉 통과 (0.16ms, 30.3MB)
// 테스트 12 〉 통과 (0.19ms, 30.3MB)
// 테스트 13 〉 통과 (0.21ms, 30.3MB)
// 테스트 14 〉 통과 (0.25ms, 30.1MB)
// 테스트 15 〉 통과 (0.43ms, 30.3MB)
// 테스트 16 〉 통과 (0.40ms, 30.4MB)
// 테스트 17 〉 통과 (0.67ms, 30.3MB)
// 테스트 18 〉 통과 (0.62ms, 30.3MB)
// 테스트 19 〉 통과 (0.69ms, 30.3MB)
// 테스트 20 〉 통과 (0.67ms, 30.3MB)
