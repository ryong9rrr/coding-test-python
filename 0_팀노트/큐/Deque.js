class Node {
  constructor(value, prev = null, next = null) {
    this.value = value
    this.prev = prev
    this.next = next
  }
}

class Deque {
  constructor() {
    this._head = null
    this._tail = null
    this._length = 0
  }

  get head() {
    return this._head ? this._head.value : null
  }

  get tail() {
    return this._tail ? this._tail.value : null
  }

  get length() {
    return this._length
  }

  unshift(element) {
    const newNode = new Node(element, null, this._head)
    if (this._head) {
      this._head.prev = newNode
    } else {
      this._tail = newNode
    }
    this._head = newNode
    this._length++
  }

  push(element) {
    const newNode = new Node(element, this._tail, null)
    if (this._tail) {
      this._tail.next = newNode
    } else {
      this._head = newNode
    }
    this._tail = newNode
    this._length++
  }

  shift() {
    if (!this._head) {
      return null
    }
    const removedNode = this._head
    if (this._head === this._tail) {
      this._head = null
      this._tail = null
    } else {
      this._head = removedNode.next
      this._head.prev = null
    }
    this._length--
    return removedNode.value
  }

  pop() {
    if (!this._tail) {
      return null
    }
    const removedNode = this._tail
    if (this._head === this._tail) {
      this._head = null
      this._tail = null
    } else {
      this._tail = removedNode.prev
      this._tail.next = null
    }
    this._length--
    return removedNode.value
  }

  clear() {
    this._head = null
    this._tail = null
    this._length = 0
  }
}
