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

Queue.prototype.isEmpty = function () {
  return this.array.length === 0;
};

function solution(priorities, location) {
  var answer = -1;
  // index
  let vq = new Queue();
  // 우선순위
  let pq = new Queue();

  for (let i = 0; i < priorities.length; i++) {
    vq.enqueue(i);
    pq.enqueue(priorities[i]);
  }
  let count = 0;
  while (!vq.isEmpty() || !pq.isEmpty()) {
    if (pq.front() === pq.max()) {
      count++;
      if (vq.front() === location) {
        answer = count;
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

  return answer;
}
