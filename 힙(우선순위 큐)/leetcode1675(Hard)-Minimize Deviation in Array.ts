// 최대 힙 풀이 : 180ms(100%), 62.3MB(100%)
class MaxHeap {
  private values: number[]

  constructor() {
    // this is where the array that represents our heap will be stored
    this.values = []
  }

  get size() {
    return this.values.length
  }

  add(element: number) {
    this.values.push(element)
    this.percolateUp(this.values.length - 1)
  }

  // removes and returns max element
  extractMax() {
    if (this.values.length < 1) {
      throw new Error("heap is empty")
    }

    // get max and last element
    const max = this.values[0]
    const end = this.values.pop() as number

    if (this.values.length > 0) {
      // reassign first element to the last element
      this.values[0] = end
      // heapify down until element is back in its correct position
      this.percolateDown(0)
    }

    // return the max
    return max
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

    // while we haven't reached the root node and the current element is greater than its parent node
    while (
      currentIndex > 0 &&
      this.values[currentIndex] > this.values[parentIndex]
    ) {
      // swap
      this.swap(currentIndex, parentIndex)
      // move up the binary heap
      currentIndex = parentIndex
      parentIndex = this.parent(parentIndex)
    }
  }

  private percolateDown(index: number) {
    // if the node at index has children
    if (!this.isLeaf(index)) {
      // get indices of children
      let leftChildIndex = this.leftChild(index)
      let rightChildIndex = this.rightChild(index)
      // start out largest index at parent index
      let largestIndex = index

      // if the left child > parent
      if (this.values[leftChildIndex] > this.values[largestIndex]) {
        // reassign largest index to left child index
        largestIndex = leftChildIndex
      }

      // if the right child > element at largest index (either parent or left child)
      if (this.values[rightChildIndex] >= this.values[largestIndex]) {
        // reassign largest index to right child index
        largestIndex = rightChildIndex
      }

      // if the largest index is not the parent index
      if (largestIndex !== index) {
        // swap
        this.swap(index, largestIndex)
        // recursively move down the heap
        this.percolateDown(largestIndex)
      }
    }
  }
}

function minimumDeviation(nums: number[]): number {
  let minValue = Infinity
  const heap = new MaxHeap()

  // 최솟값 설정 및 힙 구성
  Array.from(new Set(nums)).forEach((num) => {
    const value = num % 2 === 0 ? num : num * 2
    minValue = Math.min(minValue, value)
    heap.add(value)
  })

  let deviation = Infinity
  while (true) {
    let maxValue = heap.extractMax()
    deviation = Math.min(deviation, maxValue - minValue)
    if (maxValue % 2 === 1) {
      break
    }
    maxValue = maxValue / 2
    minValue = Math.min(minValue, maxValue)
    heap.add(maxValue)
  }

  return deviation
}
