// 642ms(100%), 101.3MB(65%)
class MyNode {
  key: number | null
  val: number | null
  freq: number
  prev: MyNode | null
  next: MyNode | null
  constructor(key: number | null, val: number | null) {
    this.key = key
    this.val = val
    this.freq = 1
    this.prev = this.next = null
  }
}

class MyDLinkedList {
  private _sentinel: MyNode
  private _size: number
  constructor() {
    this._sentinel = new MyNode(null, null)
    this._sentinel.next = this._sentinel.prev = this._sentinel
    this._size = 0
  }

  get size() {
    return this._size
  }

  append(node: MyNode) {
    node.next = this._sentinel.next
    node.prev = this._sentinel
    node.next!.prev = node
    this._sentinel.next = node
    this._size += 1
  }

  pop(node: MyNode | null = null) {
    if (this._size === 0) {
      return null
    }

    if (!node) {
      node = this._sentinel.prev
    }

    node!.prev!.next = node!.next
    node!.next!.prev = node!.prev
    this._size -= 1
    return node
  }
}

class LFUCache {
  private _size: number
  private _capacity: number
  private _node: Record<number, MyNode>
  private _freq: Record<number, MyDLinkedList>
  private _minFreq: number

  constructor(capacity: number) {
    this._size = 0
    this._capacity = capacity
    this._node = {}
    this._freq = {}
    this._minFreq = 0
  }

  private update(node: MyNode) {
    const freq = node.freq
    this._freq[freq].pop(node)
    if (
      this._minFreq === freq &&
      (this._freq[freq].size === 0 || !this._freq[freq])
    ) {
      this._minFreq += 1
    }

    node.freq += 1
    const updatedFreq = node.freq
    if (!this._freq[updatedFreq]) {
      this._freq[updatedFreq] = new MyDLinkedList()
    }
    this._freq[updatedFreq].append(node)
  }

  private isFull() {
    return this._size === this._capacity
  }

  get(key: number): number {
    if (!(key in this._node)) {
      return -1
    }

    const node = this._node[key]
    this.update(node)
    return node.val!
  }

  put(key: number, value: number): void {
    if (this._capacity === 0) {
      return
    }

    if (key in this._node) {
      const node = this._node[key]
      this.update(node)
      node.val = value
      return
    }

    if (this.isFull()) {
      const node = this._freq[this._minFreq].pop() as MyNode
      delete this._node[node.key as number]
      this._size -= 1
    }
    const newNode = new MyNode(key, value)
    this._node[key] = newNode
    if (!this._freq[1]) {
      this._freq[1] = new MyDLinkedList()
    }
    this._freq[1].append(newNode)
    this._minFreq = 1
    this._size += 1
  }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * var obj = new LFUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
