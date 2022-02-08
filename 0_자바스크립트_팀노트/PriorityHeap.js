class Node {
  constructor(prior, value) {
    this.prior = prior;
    this.value = value;
  }

  get extract() {
    return [this.prior, this.value];
  }
}

class PriorityHeap {
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
      if (this.items[i].prior < this.items[parent].prior) {
        let temp = this.items[parent];
        this.items[parent] = this.items[i];
        this.items[i] = temp;
      }
      i = parent;
      parent = Math.floor(i / 2);
    }
  }

  insert(prior, value) {
    const k = new Node(prior, value);
    this.items.push(k);
    this._percolateUp();
  }

  // pop heapify
  _percolateDown(idx) {
    let left = idx * 2;
    let right = idx * 2 + 1;
    let smallest = idx;

    if (
      left <= this.length &&
      this.items[left].prior < this.items[smallest].prior
    ) {
      smallest = left;
    }
    if (
      right < this.length &&
      this.items[right].prior < this.items[smallest].prior
    ) {
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
    if (q.length === 0) return;
    let extracted = this.items[1];
    this.items[1] = this.items[this.length];
    this.items.pop();
    this._percolateDown(1);
    return extracted.extract;
  }
}

const people = [
  [3, "lee"],
  [1, "yong"],
  [2, "kim"],
];

const q = new PriorityHeap();

for (const [prior, name] of people) {
  q.insert(prior, name);
}

while (q.length) {
  console.log(q.extract()); // [ 1, 'yong' ]  [ 2, 'kim' ]  [ 3, 'lee' ]
}
