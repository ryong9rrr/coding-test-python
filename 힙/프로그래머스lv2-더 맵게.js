// 자바스크립트를 지원하지 않는 문제라서 직접 테스트케이스 넣기..
const TEST_CASE = [[[1, 2, 3, 9, 10, 12], 7, 2]]

class BinaryHeap {
  constructor() {
    this.items = [null]
  }

  get length() {
    return this.items.length - 1
  }

  get head() {
    if (this.items.length < 2) return undefined
    return this.items[1]
  }

  // insert heapify
  _percolateUp() {
    let i = this.length
    let parent = Math.floor(i / 2)
    while (parent > 0) {
      if (this.items[i] < this.items[parent]) {
        let temp = this.items[parent]
        this.items[parent] = this.items[i]
        this.items[i] = temp
      }
      i = parent
      parent = Math.floor(i / 2)
    }
  }

  insert(k) {
    this.items.push(k)
    this._percolateUp()
  }

  // pop heapify
  _percolateDown(idx) {
    let left = idx * 2
    let right = idx * 2 + 1
    let smallest = idx

    if (left <= this.length && this.items[left] < this.items[smallest]) {
      smallest = left
    }
    if (right < this.length && this.items[right] < this.items[smallest]) {
      smallest = right
    }
    if (smallest !== idx) {
      let temp = this.items[idx]
      this.items[idx] = this.items[smallest]
      this.items[smallest] = temp
      this._percolateDown(smallest)
    }
  }

  extract() {
    let extracted = this.items[1]
    this.items[1] = this.items[this.length]
    this.items.pop()
    this._percolateDown(1)
    return extracted
  }
}

function solution(scoville, K, _return) {
  const heap = new BinaryHeap()
  for (const x of scoville) {
    heap.insert(x)
  }
  let count = 0

  while (heap.head < K) {
    if (heap.length < 2) return -1
    const first = heap.extract()
    const second = heap.extract()
    const _new = first + 2 * second
    count++
    heap.insert(_new)
  }
  return count
}

for (const [scoville, K, _return] of TEST_CASE) {
  const result = solution(scoville, K, _return)
  console.log(result === _return)
}

// true
