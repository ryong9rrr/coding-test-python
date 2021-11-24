const input = [
  [8, 2, 3],
  [10, 2, 3],
  [20, 5, 7],
];

function CircularQueue(size) {
  this.array = new Array(size);
  this.size = this.array.length;
  this.length = 0;
  this.head = 0;
  this.tail = 0;
}

CircularQueue.prototype.enqueue = function (e) {
  this.length++;
  this.array[this.tail++ % this.size] = e;
};

CircularQueue.prototype.dequeue = function () {
  this.length--;
  return this.array[this.head++ % this.size];
};

function solution(array) {
  let [n, m, k] = array;
  let result = [];

  // 원탁에 후보 세팅
  let cq = new CircularQueue(n);
  for (let i = 1; i <= n; i++) {
    cq.enqueue(i);
  }

  // 원형 큐에서 index 설정 팁
  cq.tail = cq.head = (n + m - 1) % n;

  let count;
  result.push(cq.dequeue());
  while (cq.length != 0) {
    count = k - 1;
    while (count--) {
      cq.enqueue(cq.dequeue());
    }
    result.push(cq.dequeue());
  }

  return result;
}

input.forEach((x) => console.log(solution(x)));
/*
[
  2, 5, 8, 4,
  1, 7, 3, 6
]
[
   2, 5, 8, 1, 6,
  10, 7, 4, 9, 3
]
[
   5, 12, 19,  7, 15, 3, 13,
   2, 14,  6, 18, 11, 9,  8,
  10, 17,  4, 16, 20, 1
]
*/
