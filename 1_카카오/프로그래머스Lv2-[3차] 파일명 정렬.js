// isNumber()는 이렇게 써야한다.
const isNumber = (s) => {
  return !Number.isNaN(parseInt(s, 10))
}

const convertFile = (file) => {
  const N = file.length
  let HEAD = ""
  let NUMBER = "0"
  let HEAD_OK = false
  let NUMBER_OK = false
  for (let i = 0; i < N; i += 1) {
    const s = file[i]
    if (HEAD_OK && NUMBER_OK) {
      break
    }
    if (!HEAD_OK) {
      HEAD += s
      if (i < N - 1 && isNumber(file[i + 1])) {
        HEAD_OK = true
      }
      continue
    }
    NUMBER += s
    if (i < N - 1 && !isNumber(file[i + 1])) {
      NUMBER_OK = true
    }
  }
  return [HEAD, NUMBER]
}

const compare = (a, b) => {
  const [aHEAD, aNUMBER, aIndex] = a
  const [bHEAD, bNUMBER, bIndex] = b
  if (aHEAD !== bHEAD) {
    return aHEAD < bHEAD ? -1 : 1
  }
  if (aNUMBER !== bNUMBER) {
    return aNUMBER - bNUMBER
  }
  return aIndex - bIndex
}

function solution(files) {
  return files
    .map((file, i) => {
      const [HEAD, STRING_NUMBER] = convertFile(file.toLowerCase())
      return [HEAD, Number(STRING_NUMBER), i]
    })
    .sort(compare)
    .map(([, , index]) => files[index])
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.46ms, 33.4MB)
// 테스트 2 〉	통과 (0.30ms, 33.4MB)
// 테스트 3 〉	통과 (13.05ms, 37.8MB)
// 테스트 4 〉	통과 (8.06ms, 38.1MB)
// 테스트 5 〉	통과 (6.37ms, 37.9MB)
// 테스트 6 〉	통과 (6.44ms, 37.7MB)
// 테스트 7 〉	통과 (8.51ms, 37.7MB)
// 테스트 8 〉	통과 (6.66ms, 37.9MB)
// 테스트 9 〉	통과 (6.96ms, 37.7MB)
// 테스트 10 〉	통과 (7.26ms, 37.9MB)
// 테스트 11 〉	통과 (6.35ms, 38.9MB)
// 테스트 12 〉	통과 (7.38ms, 39.2MB)
// 테스트 13 〉	통과 (6.39ms, 37.4MB)
// 테스트 14 〉	통과 (4.76ms, 37.6MB)
// 테스트 15 〉	통과 (4.29ms, 37.7MB)
// 테스트 16 〉	통과 (9.70ms, 37.9MB)
// 테스트 17 〉	통과 (4.18ms, 37.5MB)
// 테스트 18 〉	통과 (5.84ms, 37.8MB)
// 테스트 19 〉	통과 (6.63ms, 39.1MB)
// 테스트 20 〉	통과 (7.94ms, 37.7MB)

// 정규표현식 match
const compare = (a, b) => {
  const [aHEAD, aNUMBER, aIndex] = a
  const [bHEAD, bNUMBER, bIndex] = b
  if (aHEAD !== bHEAD) {
    return aHEAD < bHEAD ? -1 : 1
  }
  if (aNUMBER !== bNUMBER) {
    return aNUMBER - bNUMBER
  }
  return aIndex - bIndex
}

function solution(files) {
  const regExp = /\D+(\d{1,5})/i

  return files
    .map((file, index) => {
      const [searched, STRING_NUMBER] = file.match(regExp)
      const HEAD = searched.replace(STRING_NUMBER, "").toLowerCase()
      return [HEAD, parseInt(STRING_NUMBER, 10), index]
    })
    .sort(compare)
    .map((x) => files[x[2]])
}
// 정확성  테스트
// 테스트 1 〉	통과 (1.72ms, 33.6MB)
// 테스트 2 〉	통과 (1.88ms, 33.6MB)
// 테스트 3 〉	통과 (13.23ms, 37.7MB)
// 테스트 4 〉	통과 (8.92ms, 37.9MB)
// 테스트 5 〉	통과 (10.77ms, 37.7MB)
// 테스트 6 〉	통과 (6.30ms, 37.8MB)
// 테스트 7 〉	통과 (6.50ms, 37.7MB)
// 테스트 8 〉	통과 (7.16ms, 37.7MB)
// 테스트 9 〉	통과 (10.36ms, 37.7MB)
// 테스트 10 〉	통과 (6.23ms, 37.8MB)
// 테스트 11 〉	통과 (6.01ms, 37.8MB)
// 테스트 12 〉	통과 (8.14ms, 37.8MB)
// 테스트 13 〉	통과 (4.19ms, 34.6MB)
// 테스트 14 〉	통과 (3.89ms, 34.6MB)
// 테스트 15 〉	통과 (3.12ms, 34.7MB)
// 테스트 16 〉	통과 (7.14ms, 37.8MB)
// 테스트 17 〉	통과 (5.68ms, 34.5MB)
// 테스트 18 〉	통과 (5.65ms, 37.9MB)
// 테스트 19 〉	통과 (7.45ms, 37.7MB)
// 테스트 20 〉	통과 (5.93ms, 37.7MB)

// 정규표현식 기준으로 문자열 split : 이런 것도 된다... ㄷㄷ
const compare = (a, b) => {
  const [aHEAD, aNUMBER, aIndex] = a
  const [bHEAD, bNUMBER, bIndex] = b
  if (aHEAD !== bHEAD) {
    return aHEAD < bHEAD ? -1 : 1
  }
  if (aNUMBER !== bNUMBER) {
    return aNUMBER - bNUMBER
  }
  return aIndex - bIndex
}

function solution(files) {
  const regExp = /^(\D+)(\d{1,5})/i

  return files
    .map((file, index) => {
      const [, HEAD, STRING_NUMBER] = file.split(regExp)
      return [HEAD.toLowerCase(), parseInt(STRING_NUMBER, 10), index]
    })
    .sort(compare)
    .map((x) => files[x[2]])
}
