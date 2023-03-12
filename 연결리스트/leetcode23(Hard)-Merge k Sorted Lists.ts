class ListNode {
  val: number
  next: ListNode | null
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val
    this.next = next === undefined ? null : next
  }
}

// 접근 1 : 정렬을 사용한 풀이
// - 시간복잡도 O(N * logN) : k개 연결리스트의 모든 노드의 개수를 N이라고 할 때,
// 모든 노드를 한 번 순회하고 그만큼 정렬하는 시간이 필요하므로
// - 공간복잡도 O(N) : k개 연결리스트의 모든 노드의 개수를 저장해야하므로
function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
  const numbers: number[] = []
  for (const head of lists) {
    let node = head
    while (node) {
      numbers.push(node.val)
      node = node.next
    }
  }

  numbers.sort((a, b) => a - b)

  let head: ListNode | null = null
  while (numbers.length > 0) {
    const number = numbers.pop()
    const node = new ListNode(number)
    node.next = head
    head = node
  }

  return head
}

// 접근 2 : 우선순위 큐(힙)
// - 시간복잡도 : N개의 노드를 heapify 하므로 O(N * logN)
// - 공간복잡도 : N개의 노드를 저장하므로 O(N)

// 이 문제는 <파이썬 알고리즘 인터뷰> 에도 나온 문제임 (우선순위 큐 - k개 정렬리스트의 병합)

class Heap<T> {
  private values: T[]

  private compareFn: (a: T, b: T) => boolean | number

  constructor(compareFn: (a: T, b: T) => boolean | number) {
    this.values = []

    this.compareFn = compareFn
  }

  private compare(a: T, b: T) {
    const result = this.compareFn(a, b)
    if (typeof result === "boolean") {
      return result
    }
    return result < 0 ? true : false
  }

  get top() {
    return this.values.length > 0 ? this.values[0] : undefined
  }

  get size() {
    return this.values.length
  }

  add(element: T) {
    this.values.push(element)
    this.percolateUp(this.values.length - 1)
  }

  extract() {
    if (this.values.length < 1) {
      throw new Error("heap is empty")
    }

    const top = this.values[0]
    const end = this.values.pop() as T

    if (this.values.length > 0) {
      this.values[0] = end
      this.percolateDown(0)
    }

    // return the top
    return top
  }

  private swap(aIndex: number, bIndex: number) {
    ;[this.values[aIndex], this.values[bIndex]] = [
      this.values[bIndex],
      this.values[aIndex],
    ]
  }

  private parent(index: number) {
    return Math.floor(Math.floor((index - 1) / 2))
  }

  private leftChild(index: number) {
    return index * 2 + 1
  }

  private rightChild(index: number) {
    return index * 2 + 2
  }

  private isLeaf(index: number) {
    return (
      index >= Math.floor(this.values.length / 2) &&
      index <= this.values.length - 1
    )
  }

  private percolateUp(index: number) {
    let currentIndex = index
    let parentIndex = this.parent(currentIndex)

    while (
      currentIndex > 0 &&
      this.compare(this.values[currentIndex], this.values[parentIndex])
    ) {
      this.swap(currentIndex, parentIndex)
      currentIndex = parentIndex
      parentIndex = this.parent(parentIndex)
    }
  }

  private percolateDown(index: number) {
    if (this.isLeaf(index)) {
      return
    }

    let leftChildIndex = this.leftChild(index)
    let rightChildIndex = this.rightChild(index)
    let largestIndex = index

    if (
      leftChildIndex < this.values.length &&
      this.compare(this.values[leftChildIndex], this.values[largestIndex])
    ) {
      largestIndex = leftChildIndex
    }

    if (
      rightChildIndex < this.values.length &&
      this.compare(this.values[rightChildIndex], this.values[largestIndex])
    ) {
      largestIndex = rightChildIndex
    }

    if (largestIndex !== index) {
      this.swap(index, largestIndex)
      this.percolateDown(largestIndex)
    }
  }
}

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
  const root = new ListNode(0)
  const heap = new Heap<[number, number, ListNode | null]>((a, b) => {
    if (a[0] === b[0]) {
      return a[1] - b[1]
    }
    return a[0] - b[0]
  })

  lists.forEach((head, i) => {
    if (head) {
      heap.add([head.val, i, head])
    }
  })

  let head: ListNode | null = root
  while (heap.size > 0) {
    const [, i, node] = heap.extract()

    head!.next = node
    head = head!.next

    const nextNode = node!.next
    if (nextNode) {
      heap.add([nextNode.val, i, nextNode])
    }
  }

  return root.next
}

// (참고 : 이 힙모듈은 객체형태로도 사용가능)
function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
  const root = new ListNode(0)
  const heap = new Heap<{
    val: number
    idx: number
    node: ListNode | null
  }>((a, b) => {
    if (a.val === b.val) {
      return a.idx - b.idx
    }
    return a.val - b.val
  })

  lists.forEach((head, i) => {
    if (head) {
      heap.add({
        val: head.val,
        idx: i,
        node: head,
      })
    }
  })

  let head: ListNode | null = root
  while (heap.size > 0) {
    const { idx, node } = heap.extract()

    head!.next = node
    head = head!.next

    const nextNode = node!.next
    if (nextNode) {
      heap.add({
        val: nextNode.val,
        idx,
        node: nextNode,
      })
    }
  }

  return root.next
}

// 접근 3 : 재귀적으로 병합
// - 시간복잡도 : O(N * logN)
// - 공간복잡도 : O(1)

// 콜스택이 터지는 문제가 발생하여 이 풀이는 생략.
