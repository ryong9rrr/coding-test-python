class Heap {
  constructor(compareFn) {
    this.values = []

    this.compareFn = compareFn
  }

  compare(a, b) {
    if (a === undefined || b === undefined) {
      return false
    }
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

  add(element) {
    this.values.push(element)
    this.percolateUp(this.values.length - 1)
  }

  extract() {
    if (this.values.length < 1) {
      throw new Error("heap is empty")
    }

    const top = this.values[0]
    const end = this.values.pop()

    if (this.values.length > 0) {
      this.values[0] = end
      this.percolateDown(0)
    }

    // return the top
    return top
  }

  swap(aIndex, bIndex) {
    ;[this.values[aIndex], this.values[bIndex]] = [
      this.values[bIndex],
      this.values[aIndex],
    ]
  }

  parent(index) {
    return Math.floor(Math.floor((index - 1) / 2))
  }

  leftChild(index) {
    return index * 2 + 1
  }

  rightChild(index) {
    return index * 2 + 2
  }

  isLeaf(index) {
    return (
      index >= Math.floor(this.values.length / 2) &&
      index <= this.values.length - 1
    )
  }

  percolateUp(index) {
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

  percolateDown(index) {
    if (!this.isLeaf(index)) {
      let leftChildIndex = this.leftChild(index)
      let rightChildIndex = this.rightChild(index)
      let largestIndex = index

      if (
        this.compare(this.values[leftChildIndex], this.values[largestIndex])
      ) {
        largestIndex = leftChildIndex
      }

      if (
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
}

class Counter {
  constructor() {
    this.table = {}
  }

  get(key) {
    if (!this.table[key]) {
      this.table[key] = 0
    }
    return this.table[key]
  }

  increase(key, value = 1) {
    if (!this.table[key]) {
      this.table[key] = 0
    }
    this.table[key] += value
  }

  decrease(key, value = 1) {
    if (!this.table[key]) {
      this.table[key] = 0
    }
    this.table[key] -= value
  }
}

function solution(operations) {
  const maxHeap = new Heap((a, b) => b - a)
  const minHeap = new Heap((a, b) => a - b)
  const counter = new Counter()

  for (const operation of operations) {
    const [command, x] = operation.split(" ")

    if (command === "I") {
      const number = parseInt(x, 10)
      maxHeap.add(number)
      minHeap.add(number)
      counter.increase(number)
      continue
    }

    if (x === "1" && maxHeap.size > 0) {
      const maxNumber = maxHeap.extract()
      counter.decrease(maxNumber)
    }

    if (x === "-1" && minHeap.size > 0) {
      const minNumber = minHeap.extract()
      counter.decrease(minNumber)
    }

    while (maxHeap.size > 0 && counter.get(maxHeap.top) <= 0) {
      maxHeap.extract()
    }

    while (minHeap.size > 0 && counter.get(minHeap.top) <= 0) {
      minHeap.extract()
    }
  }

  const maxNumber = maxHeap.size > 0 ? maxHeap.top : 0
  const minNumber = minHeap.size > 0 ? minHeap.top : 0

  return [maxNumber, minNumber]
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.74ms, 33.5MB)
// 테스트 2 〉	통과 (0.56ms, 33.7MB)
// 테스트 3 〉	통과 (0.78ms, 33.6MB)
// 테스트 4 〉	통과 (0.17ms, 33.5MB)
// 테스트 5 〉	통과 (0.44ms, 33.5MB)
// 테스트 6 〉	통과 (0.68ms, 33.7MB)
