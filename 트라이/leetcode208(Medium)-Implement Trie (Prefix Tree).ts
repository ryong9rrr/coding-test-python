// 1. Map을 사용해서 구현했을 경우
class TrieNode {
  isWord: boolean
  children: Map<string, TrieNode>

  constructor() {
    this.isWord = false
    this.children = new Map()
  }
}

class Trie {
  root: TrieNode

  constructor() {
    this.root = new TrieNode()
  }

  insert(word: string): void {
    let node = this.root
    for (const char of word) {
      if (!node.children.has(char)) {
        node.children.set(char, new TrieNode())
      }
      node = node.children.get(char) as TrieNode
    }
    node.isWord = true
  }

  searchPrefixNode(word: string): TrieNode | null {
    let node = this.root
    for (const char of word) {
      if (!node.children.has(char)) {
        return null
      }
      node = node.children.get(char) as TrieNode
    }
    return node
  }

  search(word: string): boolean {
    const node = this.searchPrefixNode(word)
    return node ? node.isWord : false
  }

  startsWith(prefix: string): boolean {
    const node = this.searchPrefixNode(prefix)
    return node ? true : false
  }
}
