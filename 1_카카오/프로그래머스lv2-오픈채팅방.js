function solution(record) {
  const users = {}
  const tempRecords = []

  record.forEach((commands) => {
    // 값이 존재하지 않으면 undefined를 리턴함.
    const [command, id, name] = commands.split(' ')
    if (command === 'Change') {
      users[id] = name
    }
    if (command === 'Enter') {
      users[id] = name
      tempRecords.push(`Enter ${id}`)
    }
    if (command === 'Leave') tempRecords.push(`Leave ${id}`)
  })

  const result = tempRecords.map((commands) => {
    const [command, id] = commands.split(' ')
    if (command === 'Enter') return `${users[id]}님이 들어왔습니다.`
    if (command === 'Leave') return `${users[id]}님이 나갔습니다.`
  })
  return result
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.35ms, 30MB)
// 테스트 2 〉	통과 (0.18ms, 30.3MB)
// 테스트 3 〉	통과 (0.46ms, 30.3MB)
// 테스트 4 〉	통과 (0.69ms, 30.3MB)
// 테스트 5 〉	통과 (1.93ms, 30.3MB)
// 테스트 6 〉	통과 (2.06ms, 30.5MB)
// 테스트 7 〉	통과 (1.49ms, 30.3MB)
// 테스트 8 〉	통과 (3.08ms, 30.4MB)
// 테스트 9 〉	통과 (2.15ms, 30.4MB)
// 테스트 10 〉	통과 (1.76ms, 30.6MB)
// 테스트 11 〉	통과 (1.30ms, 30.4MB)
// 테스트 12 〉	통과 (1.16ms, 30.3MB)
// 테스트 13 〉	통과 (1.80ms, 30.3MB)
// 테스트 14 〉	통과 (1.89ms, 30.4MB)
// 테스트 15 〉	통과 (0.17ms, 30.4MB)
// 테스트 16 〉	통과 (0.17ms, 30.2MB)
// 테스트 17 〉	통과 (0.48ms, 30.2MB)
// 테스트 18 〉	통과 (0.67ms, 30.3MB)
// 테스트 19 〉	통과 (1.93ms, 30.5MB)
// 테스트 20 〉	통과 (1.50ms, 30.2MB)
// 테스트 21 〉	통과 (1.51ms, 30.2MB)
// 테스트 22 〉	통과 (1.62ms, 30.2MB)
// 테스트 23 〉	통과 (3.06ms, 30.3MB)
// 테스트 24 〉	통과 (3.23ms, 30.3MB)
// 테스트 25 〉	통과 (145.52ms, 73.4MB)
// 테스트 26 〉	통과 (219.54ms, 92.1MB)
// 테스트 27 〉	통과 (225.32ms, 101MB)
// 테스트 28 〉	통과 (240.99ms, 102MB)
// 테스트 29 〉	통과 (213.03ms, 101MB)
// 테스트 30 〉	통과 (205.28ms, 88MB)
// 테스트 31 〉	통과 (218.63ms, 107MB)
// 테스트 32 〉	통과 (158.15ms, 96.4MB)

// 22년 7월 풀이, 전체적인 방식은 예전과 비슷하지만 좀 더 깔끔해진듯.
const MESSAGE_MAP = {
  Enter: '님이 들어왔습니다.',
  Leave: '님이 나갔습니다.',
}

function solution(record) {
  const userTable = {}
  const userLog = []

  for (const command of record) {
    const [action, userId, username] = command.split(' ')
    if (action === 'Enter' || action === 'Change') {
      userTable[userId] = username
    }
    if (action !== 'Change') {
      userLog.push([action, userId])
    }
  }

  return userLog.map(([action, userId]) => {
    return `${userTable[userId]}${MESSAGE_MAP[action]}`
  })
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.38ms, 30MB)
// 테스트 2 〉	통과 (0.15ms, 29.9MB)
// 테스트 3 〉	통과 (0.42ms, 30MB)
// 테스트 4 〉	통과 (0.39ms, 30MB)
// 테스트 5 〉	통과 (1.22ms, 30.1MB)
// 테스트 6 〉	통과 (1.50ms, 30.1MB)
// 테스트 7 〉	통과 (2.17ms, 30.1MB)
// 테스트 8 〉	통과 (1.49ms, 30MB)
// 테스트 9 〉	통과 (1.64ms, 29.8MB)
// 테스트 10 〉	통과 (1.49ms, 30.2MB)
// 테스트 11 〉	통과 (0.99ms, 29.8MB)
// 테스트 12 〉	통과 (1.01ms, 30MB)
// 테스트 13 〉	통과 (1.53ms, 30MB)
// 테스트 14 〉	통과 (1.71ms, 30.1MB)
// 테스트 15 〉	통과 (0.29ms, 30MB)
// 테스트 16 〉	통과 (0.33ms, 30MB)
// 테스트 17 〉	통과 (0.27ms, 29.7MB)
// 테스트 18 〉	통과 (0.62ms, 29.9MB)
// 테스트 19 〉	통과 (1.37ms, 30MB)
// 테스트 20 〉	통과 (1.92ms, 29.8MB)
// 테스트 21 〉	통과 (1.79ms, 30.1MB)
// 테스트 22 〉	통과 (1.40ms, 29.9MB)
// 테스트 23 〉	통과 (2.38ms, 30.1MB)
// 테스트 24 〉	통과 (2.37ms, 30MB)
// 테스트 25 〉	통과 (208.27ms, 78.2MB)
// 테스트 26 〉	통과 (194.32ms, 91.8MB)
// 테스트 27 〉	통과 (195.63ms, 99.9MB)
// 테스트 28 〉	통과 (190.05ms, 102MB)
// 테스트 29 〉	통과 (179.98ms, 102MB)
// 테스트 30 〉	통과 (126.46ms, 82.6MB)
// 테스트 31 〉	통과 (209.87ms, 104MB)
// 테스트 32 〉	통과 (145.65ms, 94.7MB)
