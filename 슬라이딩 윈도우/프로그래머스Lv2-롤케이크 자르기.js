// 최적화하지 않으면 시간초과
function solution(topping) {
  const b = topping.reduce((obj, x) => {
    if (!obj[x]) obj[x] = 0
    obj[x] += 1
    return obj
  }, {})

  const bSet = new Set(topping)
  const aSet = new Set()

  let result = 0
  for (const x of topping) {
    aSet.add(x)
    b[x] -= 1
    if (b[x] === 0) {
      bSet.delete(x)
    }

    if ([...aSet].length === [...bSet].length) {
      result += 1
    }
  }

  return result
}
// 정확성  테스트
// 테스트 1 〉	통과 (61.86ms, 40.2MB)
// 테스트 2 〉	통과 (5345.07ms, 55.3MB)
// 테스트 3 〉	통과 (73.96ms, 38.4MB)
// 테스트 4 〉	통과 (13.12ms, 38.2MB)
// 테스트 5 〉	통과 (95.40ms, 65.7MB)
// 테스트 6 〉	실패 (시간 초과)
// 테스트 7 〉	실패 (시간 초과)
// 테스트 8 〉	실패 (시간 초과)
// 테스트 9 〉	실패 (시간 초과)
// 테스트 10 〉	실패 (시간 초과)
// 테스트 11 〉	통과 (77.68ms, 38.3MB)
// 테스트 12 〉	통과 (301.14ms, 52.7MB)
// 테스트 13 〉	실패 (시간 초과)
// 테스트 14 〉	통과 (5282.15ms, 71.2MB)
// 테스트 15 〉	실패 (시간 초과)
// 테스트 16 〉	통과 (5249.03ms, 71.3MB)
// 테스트 17 〉	통과 (7889.42ms, 71.2MB)
// 테스트 18 〉	통과 (6014.83ms, 71.4MB)
// 테스트 19 〉	통과 (7080.70ms, 71.6MB)
// 테스트 20 〉	실패 (시간 초과)

// 최적화된 코드
function solution(topping) {
  const b = topping.reduce((obj, x) => {
    if (!obj[x]) obj[x] = 0
    obj[x] += 1
    return obj
  }, {})

  const aSet = new Set()
  let aLength = 0
  let bLength = [...new Set(topping)].length

  let result = 0
  for (const x of topping) {
    if (!aSet.has(x)) {
      aSet.add(x)
      aLength += 1
    }
    b[x] -= 1
    if (b[x] === 0) {
      bLength -= 1
    }

    if (aLength > bLength) {
      break
    }

    if (aLength === bLength) {
      result += 1
    }
  }

  return result
}
// 정확성  테스트
// 테스트 1 〉	통과 (1.68ms, 34MB)
// 테스트 2 〉	통과 (14.49ms, 39.3MB)
// 테스트 3 〉	통과 (10.79ms, 38.4MB)
// 테스트 4 〉	통과 (8.35ms, 38.2MB)
// 테스트 5 〉	통과 (50.75ms, 65.7MB)
// 테스트 6 〉	통과 (94.30ms, 71.5MB)
// 테스트 7 〉	통과 (86.36ms, 71.4MB)
// 테스트 8 〉	통과 (106.29ms, 71.4MB)
// 테스트 9 〉	통과 (66.33ms, 71.2MB)
// 테스트 10 〉	통과 (70.82ms, 71.3MB)
// 테스트 11 〉	통과 (7.33ms, 37.6MB)
// 테스트 12 〉	통과 (5.29ms, 35.3MB)
// 테스트 13 〉	통과 (121.97ms, 71.4MB)
// 테스트 14 〉	통과 (113.31ms, 71.2MB)
// 테스트 15 〉	통과 (123.12ms, 71.3MB)
// 테스트 16 〉	통과 (102.36ms, 71.4MB)
// 테스트 17 〉	통과 (91.75ms, 71.2MB)
// 테스트 18 〉	통과 (93.98ms, 71.4MB)
// 테스트 19 〉	통과 (77.32ms, 71.4MB)
// 테스트 20 〉	통과 (79.56ms, 71.4MB)
