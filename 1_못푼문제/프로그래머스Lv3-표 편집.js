class Node {
  constructor(value) {
    this.value = value
    this.prev = this.next = null
  }
}

class DoubleLinkedList {
  constructor() {
    this.head = this.tail = null
    this.size = 0
  }

  clear() {
    this.head = this.tail = null
    this.size = 0
  }

  desc(inverse = false) {
    const nodes = []
    let currentNode = this.head
    while (currentNode !== null) {
      nodes.push(currentNode.value)
      currentNode = currentNode.next
    }
    return inverse ? nodes.reverse() : nodes
  }

  add(value) {
    const newNode = new Node(value)

    if (this.head === null) {
      this.head = newNode
      this.tail = newNode
    } else {
      this.tail.next = newNode
      newNode.prev = this.tail
      this.tail = newNode
    }

    this.size++
  }

  insert(position, value) {
    if (typeof position !== 'number' || position < 0 || position > this.size) {
      return
    }

    let newNode = new Node(value)

    if (position === 0) {
      if (this.head === null) {
        this.head = newNode
        this.tail = newNode
      } else {
        newNode.next = this.head
        this.head.prev = newNode
        this.head = newNode
      }
    } else if (position === this.size) {
      this.tail.next = newNode
      newNode.prev = this.tail
      this.tail = newNode
    } else {
      let index = 0
      let currentNode = this.head
      let prevNode
      while (index++ < position) {
        prevNode = currentNode
        currentNode = currentNode.next
      }
      newNode.next = currentNode
      prevNode.next = newNode
      currentNode.prev = newNode
      newNode.prev = prevNode
    }
    this.size++
  }

  remove(value) {
    let currentNode = this.head
    let prevNode = currentNode

    while (currentNode.value !== value && currentNode.next !== null) {
      prevNode = currentNode
      currentNode = currentNode.next
    }

    if (currentNode.value !== value) {
      return undefined
    }

    if (currentNode === this.head) {
      this.head = currentNode.next
      if (this.size === 1) {
        this.tail = null
      } else {
        this.head.prev = null
      }
    } else if (currentNode === this.tail) {
      this.tail = currentNode.prev
      this.tail.next = null
    } else {
      prevNode.next = currentNode.next
      currentNode.next.prev = prevNode
    }
    this.size--

    return currentNode
  }

  removeAt(position) {
    if (typeof position !== 'number' || position < 0 || position >= this.size) {
      return
    }

    let currentNode = this.head
    let index = 0
    let prevNode

    if (position === 0) {
      this.head = currentNode.next
      if (this.size === 1) {
        this.tail = null
      } else {
        this.head.prev = null
      }
    } else if (position === this.size - 1) {
      currentNode = this.tail
      this.tail = currentNode.prev
      this.tail.next = null
    } else {
      while (index++ < position) {
        prevNode = currentNode
        currentNode = currentNode.next
      }
      prevNode.next = currentNode.next
      currentNode.next.prev = prevNode
    }

    this.size--
    return currentNode
  }

  indexOf(value) {
    let currentNode = this.head
    let index = 0

    while (currentNode !== null) {
      if (currentNode.value === value) {
        return index
      }
      index++
      currentNode = currentNode.next
    }
    return -1
  }

  remove2(value) {
    const index = this.indexOf(value)
    return index > -1 ? this.removeAt(index) : undefined
  }
}

function solution(n, k, cmd) {
  const DL = new DoubleLinkedList()
  const snapshots = []
  for (let i = 0; i < n; i++) {
    DL.add(i)
  }

  for (const c of cmd) {
    const commands = c.split(' ')
    const command = commands[0]
    if (command === 'U' || command === 'D') {
      const shift = parseInt(commands[1], 10)
      if (command === 'U') {
        k - shift < 0 ? (k = 0) : (k -= shift)
      } else {
        k + shift > DL.size - 1 ? (k = DL.size - 1) : (k += shift)
      }
    } else if (command === 'C') {
      const removedNode = DL.removeAt(k)
      snapshots.push([k, removedNode.prev.value, removedNode.value])
      if (k > DL.size - 1) {
        k = DL.size - 1
      }
    } else {
      const [prevK, prevValue, removedValue] = snapshots.pop()
      DL.insert(prevK, removedValue)
      if (k > prevK) {
        k++
      }
    }
  }

  const result = Array.from({ length: n }, () => 'X')

  for (const v of DL.desc()) {
    result[v] = 'O'
  }

  return result.join('')
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.53ms, 30.1MB)
// 테스트 2 〉	실패 (런타임 에러)
// 테스트 3 〉	통과 (0.53ms, 30MB)
// 테스트 4 〉	통과 (0.55ms, 30.1MB)
// 테스트 5 〉	실패 (0.59ms, 30.1MB)
// 테스트 6 〉	통과 (0.63ms, 30.1MB)
// 테스트 7 〉	실패 (0.65ms, 30MB)
// 테스트 8 〉	실패 (0.61ms, 30MB)
// 테스트 9 〉	실패 (0.67ms, 30.1MB)
// 테스트 10 〉	실패 (런타임 에러)
// 테스트 11 〉	실패 (2.62ms, 32.5MB)
// 테스트 12 〉	실패 (2.87ms, 32.1MB)
// 테스트 13 〉	실패 (2.98ms, 32.3MB)
// 테스트 14 〉	실패 (런타임 에러)
// 테스트 15 〉	실패 (런타임 에러)
// 테스트 16 〉	실패 (런타임 에러)
// 테스트 17 〉	실패 (런타임 에러)
// 테스트 18 〉	실패 (런타임 에러)
// 테스트 19 〉	실패 (런타임 에러)
// 테스트 20 〉	실패 (런타임 에러)
// 테스트 21 〉	실패 (런타임 에러)
// 테스트 22 〉	실패 (런타임 에러)
// 테스트 23 〉	실패 (0.51ms, 30.2MB)
// 테스트 24 〉	실패 (0.52ms, 30MB)
// 테스트 25 〉	통과 (0.50ms, 29.9MB)
// 테스트 26 〉	실패 (런타임 에러)
// 테스트 27 〉	실패 (런타임 에러)
// 테스트 28 〉	실패 (런타임 에러)
// 테스트 29 〉	통과 (0.54ms, 29.9MB)
// 테스트 30 〉	실패 (0.53ms, 30MB)
// 효율성  테스트
// 테스트 1 〉	실패 (시간 초과)
// 테스트 2 〉	실패 (시간 초과)
// 테스트 3 〉	실패 (시간 초과)
// 테스트 4 〉	실패 (시간 초과)
// 테스트 5 〉	실패 (시간 초과)
// 테스트 6 〉	실패 (시간 초과)
// 테스트 7 〉	실패 (시간 초과)
// 테스트 8 〉	실패 (런타임 에러)
// 테스트 9 〉	실패 (시간 초과)
// 테스트 10 〉	실패 (시간 초과)
