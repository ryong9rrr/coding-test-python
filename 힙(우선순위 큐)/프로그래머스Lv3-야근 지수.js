// 최대힙 모듈 사용
class MaxHeap {
  constructor() {
    this.values = []
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
      this.values[currentIndex] > this.values[parentIndex]
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

      if (this.values[leftChildIndex] > this.values[largestIndex]) {
        largestIndex = leftChildIndex
      }

      if (this.values[rightChildIndex] > this.values[largestIndex]) {
        largestIndex = rightChildIndex
      }

      if (largestIndex !== index) {
        this.swap(index, largestIndex)
        this.percolateDown(largestIndex)
      }
    }
  }
}

function solution(n, works) {
  if (works.reduce((acc, work) => acc + work, 0) <= n) {
    return 0
  }

  const maxHeap = new MaxHeap()
  works.forEach((work) => maxHeap.add(work))

  while (n--) {
    let maxValue = maxHeap.extract()
    maxValue -= 1
    maxHeap.add(maxValue)
  }

  let ans = 0
  while (maxHeap.size > 0) {
    const maxValue = maxHeap.extract()
    ans += maxValue ** 2
  }

  return ans
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.52ms, 33.4MB)
// 테스트 2 〉	통과 (0.46ms, 33.5MB)
// 테스트 3 〉	통과 (0.40ms, 33.5MB)
// 테스트 4 〉	통과 (0.45ms, 33.6MB)
// 테스트 5 〉	통과 (0.49ms, 33.4MB)
// 테스트 6 〉	통과 (0.47ms, 33.4MB)
// 테스트 7 〉	통과 (0.45ms, 33.4MB)
// 테스트 8 〉	통과 (4.89ms, 36.6MB)
// 테스트 9 〉	통과 (6.26ms, 37.2MB)
// 테스트 10 〉	통과 (0.47ms, 33.5MB)
// 테스트 11 〉	통과 (0.45ms, 33.4MB)
// 테스트 12 〉	통과 (0.50ms, 33.5MB)
// 테스트 13 〉	통과 (0.06ms, 33.5MB)
// 효율성  테스트
// 테스트 1 〉	통과 (140.09ms, 37.8MB)
// 테스트 2 〉	통과 (108.11ms, 38.6MB)

// 커스텀 힙 사용(전체로직 동일함)
class Heap {
  constructor(compareFn) {
    this.values = []

    this.compareFn = compareFn
  }

  compare(a, b) {
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

function solution(n, works) {
  if (works.reduce((acc, work) => acc + work, 0) <= n) {
    return 0
  }

  const maxHeap = new Heap((a, b) => b - a) // 여기빼고는 모두 동일(잘 만들었다 힙 모듈!!)
  works.forEach((work) => maxHeap.add(work))

  while (n--) {
    let maxValue = maxHeap.extract()
    maxValue -= 1
    maxHeap.add(maxValue)
  }

  let ans = 0
  while (maxHeap.size > 0) {
    const maxValue = maxHeap.extract()
    ans += maxValue ** 2
  }

  return ans
}
