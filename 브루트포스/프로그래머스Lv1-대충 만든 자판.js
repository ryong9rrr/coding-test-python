function solution(keymap, targets) {
  const keytable = keymap.reduce((obj, keys) => {
    ;[...keys].forEach((key, i) => {
      if (obj[key]) {
        obj[key] = Math.min(obj[key], i + 1)
      } else {
        obj[key] = i + 1
      }
    })
    return obj
  }, {})

  return targets.map((target) => {
    let clicked = 0
    for (const key of [...target]) {
      if (!keytable[key]) {
        clicked = -1
        break
      }
      clicked += keytable[key]
    }
    return clicked
  })
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.35ms, 33.5MB)
// 테스트 2 〉	통과 (0.35ms, 33.5MB)
// 테스트 3 〉	통과 (0.32ms, 33.4MB)
// 테스트 4 〉	통과 (0.39ms, 33.5MB)
// 테스트 5 〉	통과 (0.34ms, 33.6MB)
// 테스트 6 〉	통과 (0.38ms, 33.5MB)
// 테스트 7 〉	통과 (0.34ms, 33.5MB)
// 테스트 8 〉	통과 (0.34ms, 33.5MB)
// 테스트 9 〉	통과 (0.33ms, 33.5MB)
// 테스트 10 〉	통과 (0.33ms, 33.6MB)
// 테스트 11 〉	통과 (0.15ms, 33.5MB)
// 테스트 12 〉	통과 (0.13ms, 33.5MB)
// 테스트 13 〉	통과 (0.11ms, 33.4MB)
