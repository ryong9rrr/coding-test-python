/*
<사용된 문제>
- 프로그래머스 Lv4 - 카카오 : 가사 검색
*/
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

  has(string) {
    let currentNode = this.root
    for (const char of string) {
      if (!currentNode.children.has(char)) {
        return false
      }
      currentNode = currentNode.children.get(char)
    }
    return true
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
