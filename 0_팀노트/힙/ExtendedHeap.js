class Heap {
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

  percolateUp(index) {}

  percolateDown(index) {}
}

class MaxHeap extends Heap {
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

class MinHeap extends Heap {
  percolateUp(index) {
    let currentIndex = index
    let parentIndex = this.parent(currentIndex)

    while (
      currentIndex > 0 &&
      this.values[currentIndex] < this.values[parentIndex]
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
      let smallestIndex = index

      if (this.values[leftChildIndex] < this.values[smallestIndex]) {
        smallestIndex = leftChildIndex
      }

      if (this.values[rightChildIndex] < this.values[smallestIndex]) {
        smallestIndex = rightChildIndex
      }

      if (smallestIndex !== index) {
        this.swap(index, smallestIndex)
        this.percolateDown(smallestIndex)
      }
    }
  }
}
