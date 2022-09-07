// 2021 KAKAO BLIND RECRUITMENT

// 브루트포스, 효율성에서 시간초과
function solution(info, query) {
  const QUERIES = ['language', 'group', 'career', 'food', 'score']
  const PEOPLE_INFO = {}
  info.forEach((v, i) => {
    const [language, group, career, food, score] = v.split(' ')
    PEOPLE_INFO[i] = { language, group, career, food, score }
  })

  const queries = query.map((q, i) => {
    const arr = q.split(' ').filter((v) => v !== 'and')
    return arr.reduce((acc, cur, i) => {
      if (cur !== '-') acc[QUERIES[i]] = cur
      return acc
    }, {})
  })

  const check = (person, queryArray) => {
    for (const [key, value] of queryArray) {
      if (key === 'score') {
        if (Number(person['score']) < Number(value)) {
          return false
        }
        continue
      }
      if (person[key] !== value) {
        return false
      }
    }
    return true
  }

  return queries.map((v) => {
    const queryArray = Object.entries(v)
    const matched = Object.values(PEOPLE_INFO).filter((person) => check(person, queryArray))
    return matched.length
  })
}
// 정확성 테스트
// 테스트 1 〉 통과 (0.65ms, 33.5MB)
// 테스트 2 〉 통과 (0.64ms, 33.6MB)
// 테스트 3 〉 통과 (2.39ms, 36.9MB)
// 테스트 4 〉 통과 (15.68ms, 38MB)
// 테스트 5 〉 통과 (14.40ms, 38MB)
// 테스트 6 〉 통과 (23.54ms, 37.9MB)
// 테스트 7 〉 통과 (17.50ms, 37.9MB)
// 테스트 8 〉 통과 (40.45ms, 40.9MB)
// 테스트 9 〉 통과 (44.69ms, 41.4MB)
// 테스트 10 〉 통과 (53.32ms, 41.8MB)
// 테스트 11 〉 통과 (14.72ms, 37.9MB)
// 테스트 12 〉 통과 (36.61ms, 37.8MB)
// 테스트 13 〉 통과 (27.62ms, 38.2MB)
// 테스트 14 〉 통과 (39.90ms, 38.9MB)
// 테스트 15 〉 통과 (40.35ms, 39.1MB)
// 테스트 16 〉 통과 (15.20ms, 37.9MB)
// 테스트 17 〉 통과 (23.18ms, 37.9MB)
// 테스트 18 〉 통과 (39.03ms, 39.2MB)
// 효율성 테스트
// 테스트 1 〉 실패 (시간 초과)
// 테스트 2 〉 실패 (시간 초과)
// 테스트 3 〉 실패 (시간 초과)
// 테스트 4 〉 실패 (시간 초과)

// 먼저 테이블을 모두 만들어놓고 시작하기. 아니 이게 안돼...?
function solution(info, query) {
  // 코딩테스트 점수는 무조건 포함되어있다.
  const LANGUAGE = ['-', 'cpp', 'java', 'python']
  const GROUP = ['-', 'backend', 'frontend']
  const CAREER = ['-', 'junior', 'senior']
  const FOOD = ['-', 'chicken', 'pizza']
  TABLE = {}

  for (const a of LANGUAGE) {
    for (const b of GROUP) {
      for (const c of CAREER) {
        for (const d of FOOD) {
          const key = `${a} and ${b} and ${c} and ${d}`
          TABLE[key] = []
        }
      }
    }
  }

  info.forEach((v, i) => {
    const [language, group, career, food, score] = v.split(' ')
    for (const a of ['-', language]) {
      for (const b of ['-', group]) {
        for (const c of ['-', career]) {
          for (const d of ['-', food]) {
            const key = `${a} and ${b} and ${c} and ${d}`
            TABLE[key].push({
              id: i,
              score: parseInt(score, 10),
            })
          }
        }
      }
    }
  })

  return query.map((q, i) => {
    const temp = q.split(' ')
    const score = parseInt(temp.pop(), 10)
    const key = temp.join(' ')
    const count = TABLE[key].filter((person) => person.score >= score).length
    return count
  })
}
// 정확성 테스트
// 테스트 1 〉 통과 (1.03ms, 33.7MB)
// 테스트 2 〉 통과 (1.02ms, 33.7MB)
// 테스트 3 〉 통과 (1.54ms, 33.9MB)
// 테스트 4 〉 통과 (3.23ms, 34.6MB)
// 테스트 5 〉 통과 (4.92ms, 34.9MB)
// 테스트 6 〉 통과 (11.98ms, 39MB)
// 테스트 7 〉 통과 (6.74ms, 35.2MB)
// 테스트 8 〉 통과 (79.12ms, 49.1MB)
// 테스트 9 〉 통과 (103.31ms, 50.9MB)
// 테스트 10 〉 통과 (52.36ms, 51.6MB)
// 테스트 11 〉 통과 (6.27ms, 38.7MB)
// 테스트 12 〉 통과 (12.01ms, 38.9MB)
// 테스트 13 〉 통과 (6.76ms, 35.2MB)
// 테스트 14 〉 통과 (30.18ms, 44.2MB)
// 테스트 15 〉 통과 (29.62ms, 42.6MB)
// 테스트 16 〉 통과 (6.21ms, 38.7MB)
// 테스트 17 〉 통과 (16.38ms, 39MB)
// 테스트 18 〉 통과 (36.15ms, 43MB)
// 효율성 테스트
// 테스트 1 〉 실패 (시간 초과)
// 테스트 2 〉 실패 (시간 초과)
// 테스트 3 〉 실패 (시간 초과)
// 테스트 4 〉 실패 (시간 초과)
