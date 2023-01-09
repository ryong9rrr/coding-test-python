// 클로저를 활용한 가장 깔끔한 풀이
function LZW(word) {
  const table = {}
  const makeIndex = () => {
    let index = 1
    return () => index++
  }
  const index = makeIndex()

  // 1. 사전 초기화
  for (let ascii = 65; ascii <= 90; ascii += 1) {
    table[String.fromCharCode(ascii)] = index()
  }

  // 2. w를 찾는 함수
  const find = (word) => {
    const stack = [...word]
    while (stack.length > 0) {
      const w = stack.join("")
      if (table[w]) {
        return w
      }
      stack.pop()
    }
    return null
  }

  // 3. 3~5에 해당하는 알고리즘
  const result = []
  while (word) {
    const w = find(word)
    if (!w) {
      break
    }
    result.push(table[w])
    word = word.replace(w, "")
    if (!word) {
      break
    }
    const nextKey = w + word[0]
    table[nextKey] = index()
  }
  return result
}

function solution(msg) {
  return LZW(msg)
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.25ms, 33.4MB)
// 테스트 2 〉	통과 (0.44ms, 33.6MB)
// 테스트 3 〉	통과 (0.30ms, 33.5MB)
// 테스트 4 〉	통과 (179.25ms, 46.4MB)
// 테스트 5 〉	통과 (0.55ms, 33.6MB)
// 테스트 6 〉	통과 (1170.07ms, 50.3MB)
// 테스트 7 〉	통과 (257.23ms, 38.5MB)
// 테스트 8 〉	통과 (646.56ms, 42.7MB)
// 테스트 9 〉	통과 (0.15ms, 33.4MB)
// 테스트 10 〉	통과 (693.77ms, 42.8MB)
// 테스트 11 〉	통과 (211.73ms, 46.7MB)
// 테스트 12 〉	통과 (995.74ms, 51.3MB)
// 테스트 13 〉	통과 (2399.07ms, 52.4MB)
// 테스트 14 〉	통과 (2255.20ms, 53.4MB)
// 테스트 15 〉	통과 (2197.21ms, 52.4MB)
// 테스트 16 〉	통과 (1031.36ms, 53.1MB)
// 테스트 17 〉	통과 (779.48ms, 47.9MB)
// 테스트 18 〉	통과 (43.66ms, 39.8MB)
// 테스트 19 〉	통과 (93.19ms, 42.3MB)
// 테스트 20 〉	통과 (601.17ms, 50.1MB)

function initialize() {
  const table = {}
  let ascii = 65
  while (ascii <= 90) {
    table[String.fromCharCode(ascii)] = ascii - 65 + 1
    ascii += 1
  }
  return [table, ascii - 65]
}

function LZW(input) {
  const [table, lastIndex] = initialize()

  let index = lastIndex
  const getIndex = () => {
    index += 1
    return index
  }

  const find = (word) => {
    const stack = [...word]
    while (stack.length > 0) {
      const w = stack.join("")
      if (table[w]) {
        return w
      }
      stack.pop()
    }
    return null
  }

  const result = []
  while (input) {
    const w = find(input)
    if (!w) {
      break
    }
    result.push(table[w])
    input = input.replace(w, "")
    if (!input) {
      break
    }
    const nextKey = w + input[0]
    table[nextKey] = getIndex()
  }
  return result
}

function solution(msg) {
  return LZW(msg)
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.33ms, 33.5MB)
// 테스트 2 〉	통과 (0.72ms, 33.4MB)
// 테스트 3 〉	통과 (0.31ms, 33.5MB)
// 테스트 4 〉	통과 (199.61ms, 46.5MB)
// 테스트 5 〉	통과 (0.71ms, 33.4MB)
// 테스트 6 〉	통과 (1169.40ms, 49.8MB)
// 테스트 7 〉	통과 (357.65ms, 38.6MB)
// 테스트 8 〉	통과 (520.20ms, 42.7MB)
// 테스트 9 〉	통과 (0.24ms, 33.4MB)
// 테스트 10 〉	통과 (613.94ms, 42.8MB)
// 테스트 11 〉	통과 (189.47ms, 46.7MB)
// 테스트 12 〉	통과 (880.49ms, 51.2MB)
// 테스트 13 〉	통과 (2164.74ms, 52.3MB)
// 테스트 14 〉	통과 (1915.12ms, 53.6MB)
// 테스트 15 〉	통과 (1852.20ms, 52.4MB)
// 테스트 16 〉	통과 (942.98ms, 53.1MB)
// 테스트 17 〉	통과 (721.08ms, 48MB)
// 테스트 18 〉	통과 (44.73ms, 39.8MB)
// 테스트 19 〉	통과 (94.83ms, 42.1MB)
// 테스트 20 〉	통과 (532.56ms, 50.1MB)

// 클래스 풀이
class LZW {
  constructor(word) {
    this._index = 1
    this.word = word
    this.table = this.createTable()
  }

  index() {
    return this._index++
  }

  createTable() {
    const table = {}
    let ascii = 65
    while (ascii <= 90) {
      table[String.fromCharCode(ascii)] = this.index()
      ascii += 1
    }
    return table
  }

  find(word) {
    const stack = [...word]
    while (stack.length > 0) {
      const w = stack.join("")
      if (this.table[w]) {
        return w
      }
      stack.pop()
    }
    return null
  }

  compress() {
    const result = []
    while (this.word) {
      const w = this.find(this.word)
      if (!w) {
        break
      }
      result.push(this.table[w])
      this.word = this.word.replace(w, "")
      if (!this.word) {
        break
      }
      const nextKey = w + this.word[0]
      this.table[nextKey] = this.index()
    }
    return result
  }
}

function solution(msg) {
  const lzw = new LZW(msg)
  return lzw.compress()
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.27ms, 33.6MB)
// 테스트 2 〉	통과 (0.48ms, 33.6MB)
// 테스트 3 〉	통과 (0.31ms, 33.4MB)
// 테스트 4 〉	통과 (179.46ms, 46.5MB)
// 테스트 5 〉	통과 (0.56ms, 33.5MB)
// 테스트 6 〉	통과 (1006.43ms, 50.2MB)
// 테스트 7 〉	통과 (238.40ms, 38.5MB)
// 테스트 8 〉	통과 (507.46ms, 42.7MB)
// 테스트 9 〉	통과 (0.24ms, 33.4MB)
// 테스트 10 〉	통과 (636.34ms, 42.7MB)
// 테스트 11 〉	통과 (205.26ms, 46.7MB)
// 테스트 12 〉	통과 (916.96ms, 51.4MB)
// 테스트 13 〉	통과 (2206.55ms, 52.4MB)
// 테스트 14 〉	통과 (1964.98ms, 53.4MB)
// 테스트 15 〉	통과 (1994.24ms, 52.6MB)
// 테스트 16 〉	통과 (968.25ms, 53.3MB)
// 테스트 17 〉	통과 (733.65ms, 47.8MB)
// 테스트 18 〉	통과 (71.03ms, 39.8MB)
// 테스트 19 〉	통과 (95.33ms, 42.2MB)
// 테스트 20 〉	통과 (605.31ms, 50.3MB)
