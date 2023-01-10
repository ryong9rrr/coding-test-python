class MyNode {
  constructor(value) {
    this.value = value
    this.prev = null
    this.next = null
  }
}

class MyDoubleLinkedList {
  constructor() {
    this.head = this.tail = null
    this._size = 0
  }

  get size() {
    return this._size
  }

  // 편의상 구현한 메서드
  desc(reverse = false) {
    const nodes = []
    if (!reverse) {
      let node = this.head
      while (node) {
        nodes.push(node.value)
        node = node.next
      }
    } else {
      let node = this.tail
      while (node) {
        nodes.push(node.value)
        node = node.prev
      }
    }
    return nodes
  }

  add(newNode) {
    if (!(newNode instanceof MyNode)) {
      return
    }
    if (!this.head || !this.tail) {
      this.head = newNode
      this.tail = newNode
    } else {
      this.tail.next = newNode
      newNode.prev = this.tail
      this.tail = newNode
    }
    this._size += 1
  }

  remove(targetNode) {
    if (!(targetNode instanceof MyNode)) {
      throw new Error("node's instance must be MyNode")
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
    this._size -= 1
  }

  restore(targetNode) {
    if (!(targetNode instanceof MyNode)) {
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
    this._size += 1
  }
}

function solution(n, k, cmd) {
  const dll = new MyDoubleLinkedList()
  const stack = []
  let currentNode = null
  for (let index = 0; index < n; index++) {
    const newNode = new MyNode(index)
    if (index === k) {
      currentNode = newNode
    }
    dll.add(newNode)
  }

  for (const strings of cmd) {
    const [command, s] = strings.split(" ")
    let shift = parseInt(s, 10)

    switch (command) {
      case "C": {
        stack.push(currentNode)
        if (currentNode === dll.tail) {
          dll.remove(currentNode)
          currentNode = dll.tail
        } else {
          dll.remove(currentNode)
          currentNode = currentNode.next
        }
        break
      }
      case "Z": {
        if (stack.length > 0) {
          dll.restore(stack.pop())
        }
        break
      }
      case "U": {
        while (shift--) {
          currentNode = currentNode.prev
        }
        break
      }
      case "D": {
        while (shift--) {
          currentNode = currentNode.next
        }
        break
      }
    }
  }

  const result = Array.from({ length: n }, () => "X")
  dll.desc().forEach((x) => (result[x] = "O"))
  return result.join("")
}
