//자바스크립트 Set을 이용한 풀이
function solution(id_list, report, k) {
  const table = {}
  const banned = {}

  // 테이블 초기화
  id_list.forEach((user) => {
    table[user] = new Set()
    banned[user] = 0
  })

  // 전체 신고 현황 갱신
  report.forEach((info) => {
    const [user, rUser] = info.split(' ')
    table[user].add(rUser)
  })

  // 신고당한 유저 테이블 갱신
  id_list.forEach((user) => {
    ;[...table[user]].forEach((rUser) => (banned[rUser] += 1))
  })

  return id_list.map((user) => {
    let count = 0
    table[user].forEach((rUser) => {
      if (banned[rUser] >= k) count++
    })
    return count
  })
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.20ms, 30.3MB)
// 테스트 2 〉	통과 (0.22ms, 30MB)
// 테스트 3 〉	통과 (156.09ms, 79.2MB)
// 테스트 4 〉	통과 (0.45ms, 30MB)
// 테스트 5 〉	통과 (0.28ms, 30.2MB)
// 테스트 6 〉	통과 (2.19ms, 29.9MB)
// 테스트 7 〉	통과 (6.05ms, 32.6MB)
// 테스트 8 〉	통과 (9.02ms, 33.1MB)
// 테스트 9 〉	통과 (110.39ms, 56.8MB)
// 테스트 10 〉	통과 (79.59ms, 55.3MB)
// 테스트 11 〉	통과 (165.24ms, 79.1MB)
// 테스트 12 〉	통과 (0.70ms, 30.1MB)
// 테스트 13 〉	통과 (0.61ms, 30.1MB)
// 테스트 14 〉	통과 (77.72ms, 51.3MB)
// 테스트 15 〉	통과 (163.23ms, 59.1MB)
// 테스트 16 〉	통과 (0.46ms, 30MB)
// 테스트 17 〉	통과 (0.76ms, 29.9MB)
// 테스트 18 〉	통과 (0.80ms, 30.2MB)
// 테스트 19 〉	통과 (1.24ms, 30.3MB)
// 테스트 20 〉	통과 (84.69ms, 51.2MB)
// 테스트 21 〉	통과 (149.94ms, 59.1MB)
// 테스트 22 〉	통과 (0.41ms, 30.2MB)
// 테스트 23 〉	통과 (0.37ms, 30MB)
// 테스트 24 〉	통과 (0.18ms, 30.2MB)
