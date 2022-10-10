// 정렬 + 이분탐색
function reverseString(string) {
  return [...string].reverse().join('')
}

function search(arr, target) {
  const lower = (arr, target) => {
    target = target.replace(/\?/g, 'a')
    let lo = 0
    let hi = arr.length
    while (lo < hi) {
      const mid = Math.floor((lo + hi) / 2)
      if (target <= arr[mid]) {
        hi = mid
      } else {
        lo = mid + 1
      }
    }
    return lo
  }

  const upper = (arr, target) => {
    target = target.replace(/\?/g, 'z')
    let lo = 0
    let hi = arr.length
    while (lo < hi) {
      const mid = Math.floor((lo + hi) / 2)
      if (target < arr[mid]) {
        hi = mid
      } else {
        lo = mid + 1
      }
    }
    return lo
  }

  const lo = lower(arr, target)
  const hi = upper(arr, target)
  return hi - lo >= 0 ? hi - lo : 0
}

function solution(words, queries) {
  const table = {}
  const reverseTable = {}
  words.forEach((word) => {
    const key = word.length
    if (!table[key]) table[key] = []
    if (!reverseTable[key]) reverseTable[key] = []
    table[key].push(word)
    reverseTable[key].push(reverseString(word))
  })

  for (const key in table) {
    table[key].sort()
    reverseTable[key].sort()
  }

  return queries.map((query) => {
    const key = query.length
    if (!table[key]) {
      return 0
    }
    if (query[query.length - 1] === '?') {
      return search(table[key], query)
    }
    return search(reverseTable[key], reverseString(query))
  })
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.74ms, 33.5MB)
// 테스트 2 〉	통과 (0.41ms, 33.5MB)
// 테스트 3 〉	통과 (0.67ms, 33.5MB)
// 테스트 4 〉	통과 (0.46ms, 33.5MB)
// 테스트 5 〉	통과 (0.43ms, 33.7MB)
// 테스트 6 〉	통과 (0.69ms, 33.5MB)
// 테스트 7 〉	통과 (2.26ms, 33.9MB)
// 테스트 8 〉	통과 (1.40ms, 33.8MB)
// 테스트 9 〉	통과 (3.05ms, 34MB)
// 테스트 10 〉	통과 (1.29ms, 33.9MB)
// 테스트 11 〉	통과 (1.03ms, 33.7MB)
// 테스트 12 〉	통과 (1.39ms, 34MB)
// 테스트 13 〉	통과 (6.28ms, 35MB)
// 테스트 14 〉	통과 (4.94ms, 36.7MB)
// 테스트 15 〉	통과 (6.37ms, 35MB)
// 테스트 16 〉	통과 (10.17ms, 35MB)
// 테스트 17 〉	통과 (4.30ms, 34.7MB)
// 테스트 18 〉	통과 (6.03ms, 35MB)
// 효율성  테스트
// 테스트 1 〉	통과 (189.45ms, 62MB)
// 테스트 2 〉	통과 (418.92ms, 70.4MB)
// 테스트 3 〉	통과 (205.42ms, 74.2MB)
// 테스트 4 〉	통과 (92.51ms, 45.2MB)
// 테스트 5 〉	통과 (83.86ms, 47MB)

/////////////////////////////  트라이 풀이  //////////////////////////////
class Node {
  constructor(value = '') {
    this.value = value
    this.children = new Map()
    this.word = false
    this.count = 0
  }
}

class Trie {
  constructor() {
    this.root = new Node()
  }

  insert(string) {
    let currentNode = this.root
    for (const char of string) {
      if (!currentNode.children.has(char)) {
        currentNode.children.set(char, new Node(currentNode.value + char))
      }
      currentNode = currentNode.children.get(char)
      currentNode.count++
    }
    // 검색된 단어 데이터 업데이트
    currentNode.word = true
  }

  startsWithCount(prefix) {
    let currentNode = this.root
    for (const char of prefix) {
      if (!currentNode.children.has(char)) {
        return 0
      }
      currentNode = currentNode.children.get(char)
    }
    return currentNode.count
  }
}

function reverseString(string) {
  return [...string].reverse().join('')
}

function solution(words, queries) {
  const table = {}
  const reverseTable = {}
  const counter = {}

  words.forEach((word) => {
    const key = word.length
    if (!table[key]) table[key] = new Trie()
    if (!reverseTable[key]) reverseTable[key] = new Trie()
    table[key].insert(word)
    reverseTable[key].insert(reverseString(word))
    if (counter[key] === undefined) counter[key] = 0
    counter[key]++
  })

  return queries.map((query) => {
    const key = query.length
    if (!table[key]) {
      return 0
    }
    const tQuery = query.replace(/\?/g, '')
    if (!tQuery) {
      return counter[key]
    }
    if (query[query.length - 1] === '?') {
      return table[key].startsWithCount(tQuery)
    }
    return reverseTable[key].startsWithCount(reverseString(tQuery))
  })
}
// 정확성  테스트
// 테스트 1 〉	통과 (1.00ms, 33.8MB)
// 테스트 2 〉	통과 (0.61ms, 33.6MB)
// 테스트 3 〉	통과 (0.74ms, 33.7MB)
// 테스트 4 〉	통과 (0.68ms, 33.6MB)
// 테스트 5 〉	통과 (0.63ms, 33.6MB)
// 테스트 6 〉	통과 (0.76ms, 33.6MB)
// 테스트 7 〉	통과 (29.37ms, 38.1MB)
// 테스트 8 〉	통과 (2.12ms, 34.4MB)
// 테스트 9 〉	통과 (27.26ms, 38MB)
// 테스트 10 〉	통과 (32.67ms, 37.9MB)
// 테스트 11 〉	통과 (2.10ms, 34.4MB)
// 테스트 12 〉	통과 (31.31ms, 38.1MB)
// 테스트 13 〉	통과 (21.61ms, 50MB)
// 테스트 14 〉	통과 (38.17ms, 42.3MB)
// 테스트 15 〉	통과 (20.81ms, 50.5MB)
// 테스트 16 〉	통과 (18.36ms, 50.4MB)
// 테스트 17 〉	통과 (12.00ms, 42.5MB)
// 테스트 18 〉	통과 (18.61ms, 50.3MB)
// 효율성  테스트
// 테스트 1 〉	통과 (650.53ms, 192MB)
// 테스트 2 〉	통과 (1507.84ms, 313MB)
// 테스트 3 〉	통과 (1423.04ms, 299MB)
// 테스트 4 〉	통과 (1527.54ms, 332MB)
// 테스트 5 〉	통과 (2688.26ms, 586MB)
