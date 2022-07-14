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

  const changeHand = (number, hand) => {
    if (hand === 'L') {
      currentLeft = PHONE[String(number)]
      return 'L'
    }

    if (hand === 'R') {
      currentRight = PHONE[String(number)]
      return 'R'
    }
  }

  return numbers
    .map((number) => {
      if (number === 1 || number === 4 || number === 7) {
        return changeHand(number, 'L')
      }

      if (number === 3 || number === 6 || number === 9) {
        return changeHand(number, 'R')
      }

      const leftDistance = getDistance(number, currentLeft)
      const rightDistance = getDistance(number, currentRight)

      if (leftDistance < rightDistance) {
        return changeHand(number, 'L')
      } else if (leftDistance > rightDistance) {
        return changeHand(number, 'R')
      } else {
        return hand === 'left' ? changeHand(number, 'L') : changeHand(number, 'R')
      }
    })
    .join('')
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.15ms, 29.7MB)
// 테스트 2 〉	통과 (0.18ms, 30.2MB)
// 테스트 3 〉	통과 (0.18ms, 30.2MB)
// 테스트 4 〉	통과 (0.13ms, 29.9MB)
// 테스트 5 〉	통과 (0.17ms, 30.2MB)
// 테스트 6 〉	통과 (0.17ms, 30.1MB)
// 테스트 7 〉	통과 (0.18ms, 30.2MB)
// 테스트 8 〉	통과 (0.20ms, 29.7MB)
// 테스트 9 〉	통과 (0.19ms, 29.9MB)
// 테스트 10 〉	통과 (0.19ms, 29.6MB)
// 테스트 11 〉	통과 (0.22ms, 30MB)
// 테스트 12 〉	통과 (0.25ms, 30.2MB)
// 테스트 13 〉	통과 (0.23ms, 30.1MB)
// 테스트 14 〉	통과 (0.31ms, 30MB)
// 테스트 15 〉	통과 (0.51ms, 30MB)
// 테스트 16 〉	통과 (0.48ms, 30.1MB)
// 테스트 17 〉	통과 (0.78ms, 30.1MB)
// 테스트 18 〉	통과 (0.72ms, 30.2MB)
// 테스트 19 〉	통과 (0.79ms, 30MB)
// 테스트 20 〉	통과 (0.81ms, 30MB)
