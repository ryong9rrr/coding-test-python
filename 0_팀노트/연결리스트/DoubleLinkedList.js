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
