class MinHeap {
  private values: number[]

  constructor() {
    // this is where the array that represents our heap will be stored
    this.values = []
  }

  get top() {
    return this.values.length > 0 ? this.values[0] : undefined
  }

  get size() {
    return this.values.length
  }

  add(element: number) {
    this.values.push(element)
    this.percolateUp(this.values.length - 1)
  }

  // removes and returns min element
  extract() {
    if (this.values.length < 1) {
      throw new Error("heap is empty")
    }

    // get top and last element
    const top = this.values[0]
    const end = this.values.pop() as number

    if (this.values.length > 0) {
      // reassign first element to the last element
      this.values[0] = end
      // heapify down until element is back in its correct position
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

    // while we haven't reached the root node and the current element is smaller than its parent node
    while (
      currentIndex > 0 &&
      this.values[currentIndex] < this.values[parentIndex]
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
      let smallestIndex = index

      // if the left child < parent
      if (this.values[leftChildIndex] < this.values[smallestIndex]) {
        // reassign largest index to left child index
        smallestIndex = leftChildIndex
      }

      // if the right child <= element at largest index (either parent or left child)
      if (this.values[rightChildIndex] < this.values[smallestIndex]) {
        // reassign largest index to right child index
        smallestIndex = rightChildIndex
      }

      // if the largest index is not the parent index
      if (smallestIndex !== index) {
        // swap
        this.swap(index, smallestIndex)
        // recursively move down the heap
        this.percolateDown(smallestIndex)
      }
    }
  }
}
