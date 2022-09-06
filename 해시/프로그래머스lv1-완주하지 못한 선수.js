// forEach는 return 값이 undefined라서 사용하면 안됨. 그래서 for-of 사용
function solution(participant, completion) {
  const people = {}

  completion.forEach((name) => {
    if (!people[name]) people[name] = 0
    people[name]++
  })

  for (const name of participant) {
    if (!people[name]) {
      return name
    }
    people[name]--
  }

  return undefined
}
// 정확성 테스트
// 테스트 1 〉 통과 (0.10ms, 33.4MB)
// 테스트 2 〉 통과 (0.12ms, 33.5MB)
// 테스트 3 〉 통과 (0.32ms, 33.5MB)
// 테스트 4 〉 통과 (0.73ms, 33.7MB)
// 테스트 5 〉 통과 (0.48ms, 33.7MB)
// 효율성 테스트
// 테스트 1 〉 통과 (17.04ms, 54.9MB)
// 테스트 2 〉 통과 (25.83ms, 58.4MB)
// 테스트 3 〉 통과 (26.39ms, 62MB)
// 테스트 4 〉 통과 (29.56ms, 69.2MB)
// 테스트 5 〉 통과 (40.69ms, 72.5MB)
