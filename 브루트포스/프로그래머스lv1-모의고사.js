/*** 2021년 3월 25일의 풀이 */
function solution(answers) {
  const Children = {
    A: [1, 2, 3, 4, 5],
    B: [2, 1, 2, 3, 2, 4, 2, 5],
    C: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
  }

  const returnScore = (arr) => {
    var i = 0
    var j = 0
    var score = 0
    while (i < answers.length) {
      if (answers[i] == arr[j]) {
        score++
      }
      i++
      j++
      if (j === arr.length) {
        j = 0
      }
    }
    return score
  }

  let score = []

  score.push(returnScore(Children.A))
  score.push(returnScore(Children.B))
  score.push(returnScore(Children.C))

  let result = []

  for (var i = 0; i < score.length; i++) {
    if (Math.max(...score) == score[i]) {
      result.push(i + 1)
    }
  }
  return result
}
/*
통과 (0.16ms, 29.9MB)
테스트 2 〉	통과 (0.23ms, 30.2MB)
테스트 3 〉	통과 (0.15ms, 30.1MB)
테스트 4 〉	통과 (0.13ms, 30.1MB)
테스트 5 〉	통과 (0.17ms, 29.9MB)
테스트 6 〉	통과 (0.17ms, 30.1MB)
테스트 7 〉	통과 (16.92ms, 32.5MB)
테스트 8 〉	통과 (0.61ms, 29.9MB)
테스트 9 〉	통과 (4.81ms, 32.8MB)
테스트 10 〉	통과 (4.70ms, 33MB)
테스트 11 〉	통과 (4.73ms, 32.3MB)
테스트 12 〉	통과 (4.90ms, 32.9MB)
테스트 13 〉	통과 (0.35ms, 29.9MB)
테스트 14 〉	통과 (4.77ms, 32.9MB)
*/

// 2021년 10월 29일, 개선된 풀이(반복문을 1번만에 끝내면서 2배 빨리진 성능)
function solution(answers) {
  const a = [1, 2, 3, 4, 5]
  const b = [2, 1, 2, 3, 2, 4, 2, 5]
  const c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
  let score = [0, 0, 0]
  let aIdx = 0
  let bIdx = 0
  let cIdx = 0
  answers.forEach((v, i) => {
    if (v === a[aIdx++]) score[0]++
    if (v === b[bIdx++]) score[1]++
    if (v === c[cIdx++]) score[2]++

    if (aIdx === 5) aIdx = 0
    if (bIdx === 8) bIdx = 0
    if (cIdx === 10) cIdx = 0
  })

  const max = Math.max(...score)
  const result = []
  for (let i = 0; i < 3; i++) {
    if (score[i] === max) result.push(i + 1)
  }

  return result
}
/*
테스트 1 〉	통과 (0.12ms, 30.2MB)
테스트 2 〉	통과 (0.13ms, 30.3MB)
테스트 3 〉	통과 (0.10ms, 30.5MB)
테스트 4 〉	통과 (0.12ms, 30.4MB)
테스트 5 〉	통과 (0.11ms, 30.3MB)
테스트 6 〉	통과 (0.15ms, 30.3MB)
테스트 7 〉	통과 (1.84ms, 33.3MB)
테스트 8 〉	통과 (0.42ms, 30.3MB)
테스트 9 〉	통과 (2.53ms, 33.1MB)
테스트 10 〉	통과 (1.61ms, 32.9MB)
테스트 11 〉	통과 (2.55ms, 33.2MB)
테스트 12 〉	통과 (2.47ms, 32.8MB)
테스트 13 〉	통과 (0.23ms, 30.4MB)
테스트 14 〉	통과 (2.67ms, 33MB)
*/

// 여기서 더 smart 한 방법
function solution(answers) {
  const a = [1, 2, 3, 4, 5]
  const b = [2, 1, 2, 3, 2, 4, 2, 5]
  const c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
  let score = [0, 0, 0]
  answers.forEach((v, i) => {
    if (v === a[i % 5]) score[0]++
    if (v === b[i % 8]) score[1]++
    if (v === c[i % 10]) score[2]++
  })

  const max = Math.max(...score)
  const result = []
  for (let i = 0; i < 3; i++) {
    if (score[i] === max) result.push(i + 1)
  }

  return result
}
/*
정확성  테스트
테스트 1 〉	통과 (0.08ms, 30.3MB)
테스트 2 〉	통과 (0.08ms, 30MB)
테스트 3 〉	통과 (0.08ms, 30.1MB)
테스트 4 〉	통과 (0.09ms, 30.2MB)
테스트 5 〉	통과 (0.10ms, 30.4MB)
테스트 6 〉	통과 (0.13ms, 30.4MB)
테스트 7 〉	통과 (0.76ms, 30.1MB)
테스트 8 〉	통과 (0.35ms, 30.3MB)
테스트 9 〉	통과 (1.86ms, 33.2MB)
테스트 10 〉	통과 (0.63ms, 30.4MB)
테스트 11 〉	통과 (3.33ms, 33MB)
테스트 12 〉	통과 (1.81ms, 32.9MB)
테스트 13 〉	통과 (0.20ms, 30.3MB)
테스트 14 〉	통과 (1.98ms, 33.2MB)
*/

// 2022년 7월 풀이
// 위 풀이들처럼 하나하나 인덱스로 접근하면 당연히 시간복잡도를 줄일 수 있다.
// 문제와는 관련이 없지만 학생들이 많아질 경우 저렇게 코드를 짤 수는 없음. 따라서 어쩔 수없이 2중 루프를 선택해야 할 것이다.
function solution(answers) {
  const N = 3
  const table = [
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
  ]

  const result = Array.from({ length: N + 1 }, (v, i) => 0)

  answers.forEach((answer, i) => {
    table.forEach((x, j) => {
      if (x[i % x.length] === answer) result[j + 1]++
    })
  })

  const mostValue = Math.max(...result)
  const iter = Array.from({ length: N }, (v, i) => i + 1)

  // 이미 정렬되어있으므로 다시 정렬시킬 필요는 없음.
  return iter.reduce((acc, cur) => {
    if (mostValue === result[cur]) {
      acc.push(cur)
    }
    return acc
  }, [])
}

/*
정확성 테스트
테스트 1 〉 통과 (0.22ms, 33.4MB)
테스트 2 〉 통과 (0.21ms, 33.4MB)
테스트 3 〉 통과 (0.13ms, 33.5MB)
테스트 4 〉 통과 (0.13ms, 33.4MB)
테스트 5 〉 통과 (0.34ms, 33.5MB)
테스트 6 〉 통과 (0.26ms, 33.5MB)
테스트 7 〉 통과 (1.96ms, 36.3MB)
테스트 8 〉 통과 (0.60ms, 33.7MB)
테스트 9 〉 통과 (4.19ms, 36.7MB)
테스트 10 〉 통과 (2.03ms, 36.3MB)
테스트 11 〉 통과 (2.83ms, 36.8MB)
테스트 12 〉 통과 (3.19ms, 37.2MB)
테스트 13 〉 통과 (0.34ms, 33.5MB)
테스트 14 〉 통과 (3.04ms, 36.9MB)

*/
