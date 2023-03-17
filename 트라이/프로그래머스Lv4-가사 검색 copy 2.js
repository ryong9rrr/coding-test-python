// 정렬 + 이분탐색
function reverseString(string) {
  return [...string].reverse().join("")
}

function search(arr, target) {
  const lower = (arr, target) => {
    target = target.replace(/\?/g, "a")
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
    target = target.replace(/\?/g, "z")
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
    if (query[query.length - 1] === "?") {
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
class TrieNode {
  constructor() {
    this.count = 0
    this.children = new Map()
  }
}

class Trie {
  constructor() {
    this.root = new TrieNode()
  }

  insert(word) {
    let node = this.root
    for (const char of word) {
      if (!node.children.has(char)) {
        node.children.set(char, new TrieNode())
      }
      node = node.children.get(char)
      node.count += 1
    }
  }

  startsWithCount(prefix) {
    let node = this.root
    for (const char of prefix) {
      if (!node.children.has(char)) {
        return 0
      }
      node = node.children.get(char)
    }
    return node.count
  }
}

function solution(words, queries) {
  const trieTable = {}
  const trieTable2 = {}
  const counter = {}

  // initialize
  words.forEach((word) => {
    const key = word.length

    if (!trieTable[key]) trieTable[key] = new Trie()
    if (!trieTable2[key]) trieTable2[key] = new Trie()
    if (!counter[key]) counter[key] = 0

    trieTable[key].insert(word)
    trieTable2[key].insert([...word].reverse().join(""))
    counter[key] += 1
  })

  return queries.map((query) => {
    const key = query.length

    if (!counter[key]) {
      return 0
    }

    const q = query.replace(/\?/g, "")
    if (!q) {
      return counter[key]
    }
    if (query[0] === "?") {
      return trieTable2[key].startsWithCount([...q].reverse().join(""))
    }
    return trieTable[key].startsWithCount(q)
  })
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.87ms, 33.8MB)
// 테스트 2 〉	통과 (0.56ms, 33.5MB)
// 테스트 3 〉	통과 (0.63ms, 33.7MB)
// 테스트 4 〉	통과 (0.79ms, 33.7MB)
// 테스트 5 〉	통과 (0.58ms, 33.5MB)
// 테스트 6 〉	통과 (0.67ms, 33.6MB)
// 테스트 7 〉	통과 (6.15ms, 38.5MB)
// 테스트 8 〉	통과 (1.96ms, 34.4MB)
// 테스트 9 〉	통과 (5.72ms, 38.3MB)
// 테스트 10 〉	통과 (5.98ms, 38.8MB)
// 테스트 11 〉	통과 (1.90ms, 34.2MB)
// 테스트 12 〉	통과 (7.29ms, 38.8MB)
// 테스트 13 〉	통과 (19.19ms, 50.1MB)
// 테스트 14 〉	통과 (11.95ms, 42.1MB)
// 테스트 15 〉	통과 (17.49ms, 50.3MB)
// 테스트 16 〉	통과 (23.76ms, 50MB)
// 테스트 17 〉	통과 (11.02ms, 42.6MB)
// 테스트 18 〉	통과 (17.73ms, 50MB)
// 효율성  테스트
// 테스트 1 〉	통과 (647.23ms, 171MB)
// 테스트 2 〉	통과 (1477.69ms, 271MB)
// 테스트 3 〉	통과 (1246.18ms, 255MB)
// 테스트 4 〉	통과 (952.15ms, 285MB)
// 테스트 5 〉	통과 (2822.93ms, 493MB)
