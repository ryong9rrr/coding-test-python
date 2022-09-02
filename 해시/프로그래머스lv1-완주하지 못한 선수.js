// forEach는 return 값이 undefined라서 사용하면 안됨. 그래서 for-of 사용
function solution(participant, completion) {
  const table = completion.reduce((obj, person) => {
    if (!obj[person]) {
      obj[person] = 0
    }
    obj[person]++
    return obj
  }, {})

  for (const person of participant) {
    if (person in table) {
      table[person] -= 1
    } else {
      return person
    }

    if (table[person] < 0) return person
  }
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.25ms, 30.1MB)
// 테스트 2 〉	통과 (0.21ms, 30.1MB)
// 테스트 3 〉	통과 (0.38ms, 30MB)
// 테스트 4 〉	통과 (0.49ms, 30.2MB)
// 테스트 5 〉	통과 (0.49ms, 30.1MB)
// 효율성  테스트
// 테스트 1 〉	통과 (40.03ms, 45.7MB)
// 테스트 2 〉	통과 (50.36ms, 51.2MB)
// 테스트 3 〉	통과 (53.86ms, 54.4MB)
// 테스트 4 〉	통과 (59.00ms, 61.1MB)
// 테스트 5 〉	통과 (63.32ms, 64.3MB)
