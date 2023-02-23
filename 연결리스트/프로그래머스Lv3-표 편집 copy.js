class Node {
  constructor(data) {
    this.data = data
    this.prev = null
    this.next = null
  }
}

class DoubleLinkedList {
  constructor() {
    this.head = this.tail = null
  }

  desc(reverse = false) {
    const nodes = []
    if (!reverse) {
      let node = this.head
      while (node) {
        nodes.push(node.data)
        node = node.next
      }
    } else {
      let node = this.tail
      while (node) {
        nodes.push(node.data)
        node = node.prev
      }
    }
    return nodes
  }

  add(newNode) {
    if (!newNode instanceof Node) {
      return
    }
    if (!this.head) {
      this.head = newNode
      this.tail = newNode
    } else {
      this.tail.next = newNode
      newNode.prev = this.tail
      this.tail = newNode
    }
  }

  remove(targetNode) {
    if (!targetNode instanceof Node) {
      return
    }
    if (this.head === targetNode) {
      this.head = this.head.next
      this.head.prev = null
    } else if (this.tail === targetNode) {
      this.tail = this.tail.prev
      this.tail.next = null
    } else {
      const prevNode = targetNode.prev
      const nextNode = targetNode.next
      prevNode.next = nextNode
      nextNode.prev = prevNode
    }
  }

  insert(targetNode) {
    if (!targetNode instanceof Node) {
      return
    }
    if (targetNode.prev === null) {
      this.head.prev = targetNode
      this.head = targetNode
    } else if (targetNode.next === null) {
      this.tail.next = targetNode
      this.tail = targetNode
    } else {
      const node = targetNode.prev
      node.next.prev = targetNode
      node.next = targetNode
    }
  }
}

function solution(n, k, cmd) {
  const dl = new DoubleLinkedList()
  const stack = []
  let currentNode = null
  for (let index = 0; index < n; index++) {
    const newNode = new Node(index)
    if (index === k) {
      currentNode = newNode
    }
    dl.add(newNode)
  }

  for (const strings of cmd) {
    const [command, s] = strings.split(' ')
    let shift = parseInt(s, 10)

    switch (command) {
      case 'C': {
        stack.push(currentNode)
        if (currentNode === dl.tail) {
          dl.remove(currentNode)
          currentNode = dl.tail
        } else {
          dl.remove(currentNode)
          currentNode = currentNode.next
        }
        break
      }
      case 'Z': {
        if (stack.length > 0) {
          dl.insert(stack.pop())
        }
        break
      }
      case 'U': {
        while (shift--) {
          currentNode = currentNode.prev
        }
        break
      }
      case 'D': {
        while (shift--) {
          currentNode = currentNode.next
        }
        break
      }
    }
  }

  const result = Array.from({ length: n }, () => 'X')
  dl.desc().forEach((x) => (result[x] = 'O'))
  return result.join('')
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.35ms, 33.4MB)
// 테스트 2 〉	통과 (0.35ms, 33.5MB)
// 테스트 3 〉	통과 (0.39ms, 33.6MB)
// 테스트 4 〉	통과 (0.36ms, 33.4MB)
// 테스트 5 〉	통과 (0.52ms, 33.6MB)
// 테스트 6 〉	통과 (0.52ms, 33.5MB)
// 테스트 7 〉	통과 (0.53ms, 33.4MB)
// 테스트 8 〉	통과 (0.57ms, 33.5MB)
// 테스트 9 〉	통과 (0.52ms, 33.5MB)
// 테스트 10 〉	통과 (0.54ms, 33.5MB)
// 테스트 11 〉	통과 (0.95ms, 33.6MB)
// 테스트 12 〉	통과 (0.90ms, 33.6MB)
// 테스트 13 〉	통과 (0.99ms, 33.6MB)
// 테스트 14 〉	통과 (1.14ms, 33.7MB)
// 테스트 15 〉	통과 (1.13ms, 33.7MB)
// 테스트 16 〉	통과 (1.11ms, 33.6MB)
// 테스트 17 〉	통과 (2.23ms, 33.8MB)
// 테스트 18 〉	통과 (2.27ms, 33.7MB)
// 테스트 19 〉	통과 (2.31ms, 33.8MB)
// 테스트 20 〉	통과 (1.71ms, 33.9MB)
// 테스트 21 〉	통과 (1.68ms, 33.7MB)
// 테스트 22 〉	통과 (1.65ms, 33.7MB)
// 테스트 23 〉	통과 (0.28ms, 33.5MB)
// 테스트 24 〉	통과 (0.28ms, 33.4MB)
// 테스트 25 〉	통과 (0.27ms, 33.4MB)
// 테스트 26 〉	통과 (0.27ms, 33.4MB)
// 테스트 27 〉	통과 (0.44ms, 33.6MB)
// 테스트 28 〉	통과 (0.44ms, 33.4MB)
// 테스트 29 〉	통과 (0.47ms, 33.6MB)
// 테스트 30 〉	통과 (0.48ms, 33.6MB)
// 효율성  테스트
// 테스트 1 〉	통과 (435.72ms, 161MB)
// 테스트 2 〉	통과 (480.71ms, 161MB)
// 테스트 3 〉	통과 (474.73ms, 161MB)
// 테스트 4 〉	통과 (489.18ms, 162MB)
// 테스트 5 〉	통과 (465.84ms, 162MB)
// 테스트 6 〉	통과 (428.33ms, 162MB)
// 테스트 7 〉	통과 (156.13ms, 72.8MB)
// 테스트 8 〉	통과 (151.71ms, 76.4MB)
// 테스트 9 〉	통과 (431.10ms, 163MB)
// 테스트 10 〉	통과 (422.27ms, 163MB)
