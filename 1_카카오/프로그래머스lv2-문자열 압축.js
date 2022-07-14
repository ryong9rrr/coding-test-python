// unit: number, s: string => string[]
function divideString(unit, s) {
  let array = []
  for (let i = 0; i < s.length; i += unit) {
    array.push(s.slice(i, i + unit))
  }
  return array
}

function solution(s) {
  let result = s.length
  for (let unit = 1; unit < Math.floor(s.length / 2) + 1; unit++) {
    const array = divideString(unit, s)
    let temp = ''
    let count = 1
    let cur = array[0]
    for (let i = 1; i < array.length; i++) {
      if (cur === array[i]) {
        count++
      } else {
        if (count > 1) temp += String(count)
        temp += cur
        cur = array[i]
        count = 1
      }
    }
    if (count > 1) temp += String(count)
    temp += cur
    if (result > temp.length) {
      result = temp.length
    }
  }
  return result
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.17ms, 30.2MB)
// 테스트 2 〉	통과 (0.30ms, 30.1MB)
// 테스트 3 〉	통과 (0.21ms, 30.4MB)
// 테스트 4 〉	통과 (0.20ms, 30.3MB)
// 테스트 5 〉	통과 (0.06ms, 30.3MB)
// 테스트 6 〉	통과 (0.13ms, 30.4MB)
// 테스트 7 〉	통과 (0.33ms, 30.4MB)
// 테스트 8 〉	통과 (0.34ms, 30.3MB)
// 테스트 9 〉	통과 (0.49ms, 30.3MB)
// 테스트 10 〉	통과 (3.18ms, 32.6MB)
// 테스트 11 〉	통과 (0.18ms, 30MB)
// 테스트 12 〉	통과 (0.19ms, 30.3MB)
// 테스트 13 〉	통과 (0.19ms, 30.4MB)
// 테스트 14 〉	통과 (0.42ms, 30.2MB)
// 테스트 15 〉	통과 (0.16ms, 30.2MB)
// 테스트 16 〉	통과 (0.12ms, 30.1MB)
// 테스트 17 〉	통과 (1.29ms, 32.9MB)
// 테스트 18 〉	통과 (1.32ms, 33.1MB)
// 테스트 19 〉	통과 (1.37ms, 32.8MB)
// 테스트 20 〉	통과 (2.01ms, 32.8MB)
// 테스트 21 〉	통과 (1.94ms, 32.8MB)
// 테스트 22 〉	통과 (1.96ms, 32.7MB)
// 테스트 23 〉	통과 (1.97ms, 33MB)
// 테스트 24 〉	통과 (1.89ms, 32.7MB)
// 테스트 25 〉	통과 (1.94ms, 32.2MB)
// 테스트 26 〉	통과 (1.91ms, 32.9MB)
// 테스트 27 〉	통과 (2.00ms, 32.8MB)
// 테스트 28 〉	통과 (0.13ms, 30.2MB)

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
