class MyNode {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class MyQueue {
  constructor(array = []) {
    this.front = this.tail = null;
    this.length = 0;

    for (const el of array) {
      this.push(el);
    }
  }

  get head() {
    return !this.front || !this.tail ? undefined : this.front.value;
  }

  push(value) {
    const node = new MyNode(value);
    if (!this.front) {
      this.front = this.tail = node;
    } else {
      this.tail = this.tail.next = node;
    }
    this.length += 1;
  }

  shift() {
    if (!this.front) {
      return undefined;
    }
    const result = this.front.value;
    this.front = this.front.next;
    this.length -= 1;
    return result;
  }
}
