const input = [
  [[3], 0],
  [[3, 4, 5, 6], 2],
  [[1, 1, 5, 1, 1, 1], 0],
];

function Queue() {
  this.array = [];
}

Queue.prototype.enqueue = function (e) {
  this.array.push(e);
};

Queue.prototype.dequeue = function () {
  return this.array.shift();
};

Queue.prototype.front = function () {
  return this.array[0];
};

Queue.prototype.max = function () {
  return Math.max(...this.array);
};

function solution(x) {
  let [priorities, select] = x;
  let result = -1;

  let vq = new Queue();
  let pq = new Queue();
  for (let i = 0; i < priorities.length; i++) {
    vq.enqueue(i);
    pq.enqueue(priorities[i]);
  }

  let count = 0;
  while (true) {
    if (pq.front() === pq.max()) {
      count++;
      if (vq.front() === select) {
        result = count;
        break;
      } else {
        vq.dequeue();
        pq.dequeue();
      }
    } else {
      vq.enqueue(vq.dequeue());
      pq.enqueue(pq.dequeue());
    }
  }

  return result;
}

input.forEach((x) => console.log(solution(x)));
/*
1
2
5
*/
