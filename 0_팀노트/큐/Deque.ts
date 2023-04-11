class Node<T> {
  value: T
  prev: Node<T> | null
  next: Node<T> | null

  constructor(
    value: T,
    prev: Node<T> | null = null,
    next: Node<T> | null = null,
  ) {
    this.value = value
    this.prev = prev
    this.next = next
  }
}

class Deque<T> {
  private _head: Node<T> | null
  private _tail: Node<T> | null
  private _length: number

  constructor() {
    this._head = null
    this._tail = null
    this._length = 0
  }

  // Returns the element at the front of the deque without removing it
  get head() {
    return this._head ? this._head.value : null
  }

  // Returns the element at the back of the deque without removing it
  get tail() {
    return this._tail ? this._tail.value : null
  }

  // Returns the number of elements in the deque
  get length() {
    return this._length
  }

  // Adds an element to the front of the deque
  unshift(element: T) {
    const newNode = new Node(element, null, this._head)
    if (this._head) {
      this._head.prev = newNode
    } else {
      this._tail = newNode
    }
    this._head = newNode
    this._length++
  }

  // Adds an element to the back of the deque
  push(element: T) {
    const newNode = new Node(element, this._tail, null)
    if (this._tail) {
      this._tail.next = newNode
    } else {
      this._head = newNode
    }
    this._tail = newNode
    this._length++
  }

  // Removes and returns the element at the front of the deque
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
      this._head!.prev = null
    }
    this._length--
    return removedNode.value
  }

  // Removes and returns the element at the back of the deque
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
      this._tail!.next = null
    }
    this._length--
    return removedNode.value
  }

  // Clears the deque of all elements
  clear() {
    this._head = null
    this._tail = null
    this._length = 0
  }
}
