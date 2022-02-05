class BinaryHeap {
  constructor() {
    this.items = [null];
  }

  get length() {
    return this.items.length - 1;
  }

  // insert heapify
  _percolateUp() {
    let i = this.length;
    let parent = Math.floor(i / 2);
    while (parent > 0) {
      if (this.items[i] < this.items[parent]) {
        let temp = this.items[parent];
        this.items[parent] = this.items[i];
        this.items[i] = temp;
      }
      i = parent;
      parent = Math.floor(i / 2);
    }
  }

  insert(k) {
    this.items.push(k);
    this._percolateUp();
  }

  // pop heapify
  _percolateDown(idx) {
    let left = idx * 2;
    let right = idx * 2 + 1;
    let smallest = idx;

    if (left <= this.length && this.items[left] < this.items[smallest]) {
      smallest = left;
    }
    if (right < this.length && this.items[right] < this.items[smallest]) {
      smallest = right;
    }
    if (smallest !== idx) {
      let temp = this.items[idx];
      this.items[idx] = this.items[smallest];
      this.items[smallest] = temp;
      this._percolateDown(smallest);
    }
  }

  extract() {
    let extracted = this.items[1];
    this.items[1] = this.items[this.length];
    this.items.pop();
    this._percolateDown(1);
    return extracted;
  }
}

const numbers = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9];

const heap = new BinaryHeap();

for (const number of numbers) {
  heap.insert(number);
}

console.log(heap.items); // [null, 1, 2, 4, ... 10, 7, 9]

for (let i = 0; i < numbers.length; i++) {
  console.log(heap.extract()); // 1 2 3 4 5 6 7 8 9 10
}
