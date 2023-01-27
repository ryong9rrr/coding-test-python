// 2022 8월 프로그래머스 모의테스트 1회 2번문제
const makeCounter = (array) => {
  return array.reduce((obj, item) => {
    if (!obj[item]) obj[item] = 0
    obj[item] += 1
    return obj
  }, {})
}

function solution(want, number, discount) {
  const N = discount.length
  const iter = Array.from({ length: want.length }, (v, i) => i)

  const validate = (counter) => {
    return iter.every((i) => counter[want[i]] && counter[want[i]] >= number[i])
  }

  let result = 0
  for (let day = 0; day < N - 10 + 1; day += 1) {
    const counter = makeCounter(discount.slice(day, day + 10))
    if (validate(counter)) {
      result += 1
    }
  }

  return result
}
// 정확성  테스트
// 테스트 1 〉	통과 (67.29ms, 46.2MB)
// 테스트 2 〉	통과 (507.00ms, 74.2MB)
// 테스트 3 〉	통과 (66.65ms, 46MB)
// 테스트 4 〉	통과 (175.09ms, 55.8MB)
// 테스트 5 〉	통과 (183.70ms, 56.4MB)
// 테스트 6 〉	통과 (49.29ms, 42.3MB)
// 테스트 7 〉	통과 (142.57ms, 53MB)
// 테스트 8 〉	통과 (289.08ms, 69.3MB)
// 테스트 9 〉	통과 (58.23ms, 45.4MB)
// 테스트 10 〉	통과 (207.66ms, 56.9MB)
// 테스트 11 〉	통과 (14.92ms, 38.7MB)
// 테스트 12 〉	통과 (0.13ms, 33.6MB)
