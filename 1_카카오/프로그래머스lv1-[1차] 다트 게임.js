const pow = (type, number) => {
  if (type === 'D') return number ** 2
  if (type === 'T') return number ** 3
  return number
}

const isNumber = (string) => !Number.isNaN(Number(string))

function solution(dartResult) {
  // JS의 replace를 사용할 때 replace("10", 'k') 라고 사용하면 맨 처음 해당하는 요소 1개만 바뀜!!
  // 따라서 문자열이 아닌 정규표현식으로 사용해야 전체 문자열을 대상으로 바꿀 수 있다.
  const markedDarts = Array.from(dartResult.replace(/10/g, 'k'))
  const darts = markedDarts.reduce((array, dart) => {
    if (dart === 'k') {
      return [...array, 10]
    }
    if (isNumber(dart)) {
      return [...array, parseInt(dart, 10)]
    }
    if (dart === '*' || dart === '#') {
      return [...array, dart]
    }
    const prevScore = array.pop()
    return [...array, pow(dart, prevScore)]
  }, [])

  const scores = darts.reduce((array, dart) => {
    const tail = array.length - 1
    if (typeof dart === 'number') {
      return [...array, dart]
    }
    if (dart === '#') {
      array[tail] *= -1
      return array
    }
    // dart 가 *일 경우
    array[tail] *= 2
    if (array[tail - 1]) {
      array[tail - 1] *= 2
    }
    return array
  }, [])

  return scores.reduce((a, b) => a + b)
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.17ms, 30.1MB)
// 테스트 2 〉	통과 (0.17ms, 29.8MB)
// 테스트 3 〉	통과 (0.17ms, 30.1MB)
// 테스트 4 〉	통과 (0.19ms, 29.8MB)
// 테스트 5 〉	통과 (0.18ms, 30MB)
// 테스트 6 〉	통과 (0.18ms, 30.2MB)
// 테스트 7 〉	통과 (0.22ms, 29.8MB)
// 테스트 8 〉	통과 (0.17ms, 30MB)
// 테스트 9 〉	통과 (0.23ms, 30MB)
// 테스트 10 〉	통과 (0.19ms, 30.1MB)
// 테스트 11 〉	통과 (0.21ms, 30.2MB)
// 테스트 12 〉	통과 (0.18ms, 30.1MB)
// 테스트 13 〉	통과 (0.18ms, 30.2MB)
// 테스트 14 〉	통과 (0.18ms, 30.1MB)
// 테스트 15 〉	통과 (0.18ms, 30.1MB)
// 테스트 16 〉	통과 (0.18ms, 30MB)
// 테스트 17 〉	통과 (0.18ms, 30.2MB)
// 테스트 18 〉	통과 (0.18ms, 30.3MB)
// 테스트 19 〉	통과 (0.15ms, 30.2MB)
// 테스트 20 〉	통과 (0.20ms, 30.2MB)
// 테스트 21 〉	통과 (0.19ms, 30.1MB)
// 테스트 22 〉	통과 (0.18ms, 30.1MB)
// 테스트 23 〉	통과 (0.20ms, 30.3MB)
// 테스트 24 〉	통과 (0.18ms, 30.3MB)
// 테스트 25 〉	통과 (0.16ms, 30MB)
// 테스트 26 〉	통과 (0.18ms, 30.1MB)
// 테스트 27 〉	통과 (0.18ms, 30.1MB)
// 테스트 28 〉	통과 (0.18ms, 30.2MB)
// 테스트 29 〉	통과 (0.18ms, 30.1MB)
// 테스트 30 〉	통과 (0.19ms, 30.1MB)
// 테스트 31 〉	통과 (0.20ms, 30MB)
// 테스트 32 〉	통과 (0.18ms, 30.1MB)
