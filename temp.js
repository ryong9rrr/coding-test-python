class MyNode {
  constructor(value, prev = null, next = null) {
    this.value = value;
    this.prev = prev;
    this.next = next;
  }
}

class Deque {
  constructor(arr = []) {
    this._head = null;
    this._tail = null;
    this._length = 0;

    for (const value of arr) {
      this.push(value);
    }
  }

  get head() {
    return this._head ? this._head.value : null;
  }

  get tail() {
    return this._tail ? this._tail.value : null;
  }

  get length() {
    return this._length;
  }

  unshift(element) {
    const newNode = new MyNode(element, null, this._head);
    if (this._head) {
      this._head.prev = newNode;
    } else {
      this._tail = newNode;
    }
    this._head = newNode;
    this._length++;
  }

  push(element) {
    const newNode = new MyNode(element, this._tail, null);
    if (this._tail) {
      this._tail.next = newNode;
    } else {
      this._head = newNode;
    }
    this._tail = newNode;
    this._length++;
  }

  shift() {
    if (!this._head) {
      return null;
    }
    const removedNode = this._head;
    if (this._head === this._tail) {
      this._head = null;
      this._tail = null;
    } else {
      this._head = removedNode.next;
      this._head.prev = null;
    }
    this._length--;
    return removedNode.value;
  }

  pop() {
    if (!this._tail) {
      return null;
    }
    const removedNode = this._tail;
    if (this._head === this._tail) {
      this._head = null;
      this._tail = null;
    } else {
      this._tail = removedNode.prev;
      this._tail.next = null;
    }
    this._length--;
    return removedNode.value;
  }

  clear() {
    this._head = null;
    this._tail = null;
    this._length = 0;
  }

  desc() {
    const values = [];
    let node = this._head;
    while (node) {
      values.push(node.value);
      node = node.next;
    }
    return values;
  }
}

const brackets = {
  ')': '(',
  '}': '{',
  ']': '[',
};

function check(arr) {
  const stack = [];
  for (const value of arr) {
    if (!brackets[value]) {
      stack.push(value);
      continue;
    }

    if (stack.length === 0) {
      return false;
    }

    if (brackets[value] !== stack.pop()) {
      return false;
    }
  }
  return stack.length === 0;
}

function solution(s) {
  const q = new Deque([...s]);
  let result = 0;
  for (let i = 0; i < s.length; i += 1) {
    if (check(q.desc())) {
      result += 1;
    }
    q.push(q.shift());
  }
  return result;
}
