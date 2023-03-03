// 199ms(90%), 63.7MB(46.67%)
class Heap<T> {
  private values: T[]

  private compareFn: (a: T, b: T) => boolean | number

  constructor(compareFn: (a: T, b: T) => boolean | number) {
    this.values = []

    this.compareFn = compareFn
  }

  private compare(a: T, b: T) {
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

function minimumDeviation(nums: number[]): number {
  let minValue = Infinity
  const maxHeap = new Heap<number>((a, b) => b - a)

  // 최솟값 설정 및 힙 구성
  Array.from(new Set(nums)).forEach((num) => {
    const value = num % 2 === 0 ? num : num * 2
    minValue = Math.min(minValue, value)
    maxHeap.add(value)
  })

  let deviation = Infinity
  while (true) {
    let maxValue = maxHeap.extract()
    deviation = Math.min(deviation, maxValue - minValue)
    if (maxValue % 2 === 1) {
      break
    }
    maxValue = maxValue / 2
    minValue = Math.min(minValue, maxValue)
    maxHeap.add(maxValue)
  }

  return deviation
}
