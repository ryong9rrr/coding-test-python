/*
<사용된 문제>
- 프로그래머스 Lv3 - 카카오 : 표 편집
*/
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

  // value가 일치하는 첫 번째 노드를 반환합니다.
  find(value) {
    let node = this.head
    while (node) {
      if (node.value === value) {
        return node
      }
      node = node.next
    }
    return undefined
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

  // 카카오 코딩테스트 Lv3: 표편집 문제를 풀기 위해 구현한 메서드,
  // 가장 최근에 삭제한 노드를 인자로 받아 복원한다.
  // 버그가 있는 상황이 생길 수도 있지만 문제에서 버그가 일어날 상황은 없다고 가정했기 때문에
  // 예외처리를 하지 않은 메서드임. 따라서 이 메서드는 테스트에서 제외한다.
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
