const input = [4, 7, 10];

function Queue() {
  this.array = [];
}

Queue.prototype.enqueue = function (e) {
  this.array.push(e);
};

Queue.prototype.dequeue = function () {
  return this.array.shift();
};

function solution(n) {
  let result = [];

  let q = new Queue();
  for (let i = 1; i <= n; i++) {
    q.enqueue(i);
  }

  while (q.array.length != 0) {
    result.push(q.dequeue());
    if (q.array.length != 0) {
      q.enqueue(q.dequeue());
    }
  }

  return result;
}

input.forEach((x) => console.log(solution(x)));
/*
[ 1, 3, 2, 4 ]
[
  1, 3, 5, 7,
  4, 2, 6
]
[
  1, 3,  5, 7, 9,
  2, 6, 10, 8, 4
]

*/
