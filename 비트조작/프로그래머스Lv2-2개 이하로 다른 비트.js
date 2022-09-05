function rfind(array, item) {
  for (let i = array.length - 1; i > -1; i--) {
    if (array[i] === item) return i
  }
  return -1
}

function f(n) {
  if (n % 2 === 0) {
    return n + 1
  }
  const binArr = [...('0' + n.toString(2))]
  const i = rfind(binArr, '0')
  binArr[i] = '1'
  binArr[i + 1] = '0'
  return parseInt(binArr.join(''), 2)
}

function solution(numbers) {
  return numbers.map((number) => f(number))
}
// 정확성 테스트
// 테스트 1 〉 통과 (0.78ms, 33.8MB)
// 테스트 2 〉 통과 (55.12ms, 51MB)
// 테스트 3 〉 통과 (0.24ms, 33.4MB)
// 테스트 4 〉 통과 (0.74ms, 33.8MB)
// 테스트 5 〉 통과 (0.91ms, 34MB)
// 테스트 6 〉 통과 (0.81ms, 33.8MB)
// 테스트 7 〉 통과 (177.99ms, 59.2MB)
// 테스트 8 〉 통과 (169.75ms, 58.6MB)
// 테스트 9 〉 통과 (163.67ms, 58.5MB)
// 테스트 10 〉 통과 (321.02ms, 60.2MB)
// 테스트 11 〉 통과 (329.33ms, 60.8MB)
