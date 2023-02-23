// 390ms(78.31%), 96.7MB(10.84%)
class MaxHeap {
  constructor() {
    // this is where the array that represents our heap will be stored
    this.values = []
  }

  get size() {
    return this.values.length
  }

  add(element) {
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
    const end = this.values.pop()

    if (this.values.length > 0) {
      // reassign first element to the last element
      this.values[0] = end
      // heapify down until element is back in its correct position
      this.percolateDown(0)
    }

    // return the max
    return max
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

  percolateDown(index) {
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

/**
 * @param {number} k
 * @param {number} w
 * @param {number[]} profits
 * @param {number[]} capital
 * @return {number}
 */
var findMaximizedCapital = function (k, w, profits, capital) {
  const n = profits.length
  const projects = Array.from({ length: n }, (v, i) => i)
    .map((i) => [capital[i], profits[i]])
    .sort((a, b) => a[0] - b[0])

  let index = 0
  const heap = new MaxHeap()

  const insertToHeap = () => {
    while (index < n) {
      const [cost, profit] = projects[index]
      if (cost <= w) {
        heap.add(profit)
        index += 1
      } else {
        break
      }
    }
  }

  insertToHeap()

  while (k > 0 && heap.size > 0) {
    w += heap.extractMax()
    k -= 1
    insertToHeap()
  }

  return w
}
