// 2236ms(59.28%), 99.2MB(50.71%)

class TrieNode {
  isWord: boolean
  children: Map<string, TrieNode>

  constructor() {
    this.isWord = false
    this.children = new Map()
  }
}

class WordDictionary {
  root: TrieNode

  constructor() {
    this.root = new TrieNode()
  }

  addWord(word: string): void {
    let node = this.root
    for (const char of word) {
      if (!node.children.has(char)) {
        node.children.set(char, new TrieNode())
      }
      node = node.children.get(char) as TrieNode
    }
    node.isWord = true
  }

  search(word: string): boolean {
    return this.match(this.root, 0, word)
  }

  // DFS
  private match(node: TrieNode, index: number, word: string): boolean {
    if (index === word.length) {
      return node.isWord
    }

    const char = word[index]
    if (char === ".") {
      for (const nextChar of node.children.keys()) {
        if (
          this.match(node.children.get(nextChar) as TrieNode, index + 1, word)
        ) {
          return true
        }
      }
      return false
    }

    return (
      node.children.has(char) &&
      this.match(node.children.get(char) as TrieNode, index + 1, word)
    )
  }
}
