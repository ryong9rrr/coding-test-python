// 힙 구현 : 125ms(58.71%), 51.5MB(33.71%)
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

function findCheapestPrice(
  n: number,
  flights: number[][],
  src: number,
  dst: number,
  k: number,
): number {
  const graph = {}
  for (const [v, w, cost] of flights) {
    if (!graph[v]) graph[v] = []
    graph[v].push([w, cost])
  }

  const costs = new Array(n).fill(Infinity)
  const rests = new Array(n).fill(k)
  const heap = new Heap<[number, number, number]>((a, b) => {
    if (a[0] !== b[0]) {
      return a[0] - b[0]
    }
    if (a[1] !== b[1]) {
      return a[1] - b[1]
    }
    return a[2] - b[2]
  })

  heap.add([0, k, src])

  while (heap.size > 0) {
    const [acc, rest, v] = heap.extract()
    if (v === dst) {
      return acc
    }
    if (rest < 0) {
      continue
    }

    if (!graph[v] || graph[v].length === 0) {
      continue
    }

    for (const [w, cost] of graph[v]) {
      const alt = acc + cost
      if (alt < costs[w] || rests[w] < rest) {
        costs[w] = alt
        rests[w] = rest - 1
        heap.add([alt, rest - 1, w])
      }
    }
  }

  return -1
}
