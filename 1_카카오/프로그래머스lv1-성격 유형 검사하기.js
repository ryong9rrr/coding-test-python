const matchKind = {
  R: 'T',
  C: 'F',
  J: 'M',
  A: 'N',
}

function solution(survey, choices) {
  const N = survey.length
  const score = {
    R: 0,
    T: 0,
    C: 0,
    F: 0,
    J: 0,
    M: 0,
    A: 0,
    N: 0,
  }

  for (let i = 0; i < N; i++) {
    const [x, y] = [...survey[i]]
    const choice = choices[i]
    if (1 <= choice && choice <= 3) {
      score[x] += 4 - choice
    } else if (4 <= choice && choice <= 7) {
      score[y] += choice - 4
    }
  }

  let result = ''
  for (const kind of ['R', 'C', 'J', 'A']) {
    const a = kind
    const b = matchKind[kind]
    if (score[a] > score[b]) {
      result += a
    } else if (score[a] < score[b]) {
      result += b
    } else {
      const minChar = a < b ? a : b
      result += minChar
    }
  }
  return result
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.11ms, 30MB)
// 테스트 2 〉	통과 (0.28ms, 29.9MB)
// 테스트 3 〉	통과 (0.28ms, 30.1MB)
// 테스트 4 〉	통과 (0.29ms, 30.1MB)
// 테스트 5 〉	통과 (0.27ms, 30.2MB)
// 테스트 6 〉	통과 (0.30ms, 30.1MB)
// 테스트 7 〉	통과 (0.28ms, 29.7MB)
// 테스트 8 〉	통과 (0.16ms, 29.9MB)
// 테스트 9 〉	통과 (0.29ms, 30MB)
// 테스트 10 〉	통과 (0.28ms, 29.9MB)
// 테스트 11 〉	통과 (0.32ms, 30.1MB)
// 테스트 12 〉	통과 (0.39ms, 30MB)
// 테스트 13 〉	통과 (0.29ms, 30MB)
// 테스트 14 〉	통과 (0.52ms, 30MB)
// 테스트 15 〉	통과 (0.56ms, 30.1MB)
// 테스트 16 〉	통과 (0.67ms, 30.1MB)
// 테스트 17 〉	통과 (0.59ms, 30MB)
// 테스트 18 〉	통과 (0.60ms, 30.1MB)
// 테스트 19 〉	통과 (0.44ms, 30.1MB)
// 테스트 20 〉	통과 (0.44ms, 30MB)
