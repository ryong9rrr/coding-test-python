Set.prototype.intersection = function (setB) {
  var intersection = new Set()
  for (var elem of setB) {
    if (this.has(elem)) {
      intersection.add(elem)
    }
  }
  return intersection
}

function makeTable(strings) {
  const table = {}
  Array.from(strings).forEach((s) => {
    if (!table[s]) table[s] = 0
    table[s]++
  })
  return table
}

function solution(X, Y) {
  const table_x = makeTable(X)
  const table_y = makeTable(Y)

  const set_x = new Set(Object.keys(table_x))
  const set_y = new Set(Object.keys(table_y))

  const intersection = set_x.intersection(set_y)

  let strings = ''
  Array.from(intersection).forEach((n) => {
    const count = Math.min(table_x[n], table_y[n])
    strings += n.repeat(count)
  })

  const result = Array.from(strings).sort().reverse().join('')

  if (result === '') {
    return '-1'
  }

  if (result[0] === '0') {
    return '0'
  }

  return result
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.15ms, 33.5MB)
// 테스트 2 〉	통과 (0.16ms, 33.4MB)
// 테스트 3 〉	통과 (0.22ms, 33.6MB)
// 테스트 4 〉	통과 (0.16ms, 33.4MB)
// 테스트 5 〉	통과 (0.24ms, 33.4MB)
// 테스트 6 〉	통과 (0.43ms, 33.5MB)
// 테스트 7 〉	통과 (0.34ms, 33.4MB)
// 테스트 8 〉	통과 (0.40ms, 33.5MB)
// 테스트 9 〉	통과 (0.32ms, 33.5MB)
// 테스트 10 〉	통과 (0.37ms, 33.5MB)
// 테스트 11 〉	통과 (555.18ms, 127MB)
// 테스트 12 〉	통과 (546.51ms, 127MB)
// 테스트 13 〉	통과 (739.57ms, 127MB)
// 테스트 14 〉	통과 (527.89ms, 127MB)
// 테스트 15 〉	통과 (685.18ms, 127MB)
// 테스트 16 〉	통과 (0.17ms, 33.5MB)
// 테스트 17 〉	통과 (0.18ms, 33.4MB)
// 테스트 18 〉	통과 (0.21ms, 33.5MB)
// 테스트 19 〉	통과 (0.14ms, 33.5MB)
