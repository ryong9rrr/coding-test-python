const input = [
  ["enqueue 1", "enqueue 2", "dequeue", "dequeue", "dequeue"],
  [
    "enqueue 3",
    "enqueue 4",
    "enqueue 5",
    "enqueue 6",
    "front",
    "back",
    "dequeue",
    "size",
    "empty",
  ],
  [
    "enqueue 7",
    "enqueue 8",
    "front",
    "back",
    "size",
    "empty",
    "dequeue",
    "dequeue",
    "dequeue",
    "size",
    "empty",
    "dequeue",
    "enqueue 9",
    "empty",
    "front",
  ],
];

function Queue() {
  this.array = [];
}

Queue.prototype.enqueue = function (e) {
  this.array.push(e);
};

Queue.prototype.dequeue = function () {
  let r = this.array.shift();
  return r === undefined ? -1 : r;
};

Queue.prototype.size = function () {
  return this.array.length;
};

Queue.prototype.empty = function () {
  return this.array.length === 0 ? 1 : 0;
};

Queue.prototype.front = function () {
  return this.array.length === 0 ? -1 : this.array[0];
};

Queue.prototype.back = function () {
  return this.array.length === 0 ? -1 : this.array[this.array.length - 1];
};

function solution(cmds) {
  let result = [];
  let q = new Queue();

  for (let i = 0; i < cmds.length; i++) {
    let cmd = cmds[i].split(" ")[0];

    switch (cmd) {
      case "enqueue":
        q.enqueue(Number(cmds[i].split(" ")[1]));
        break;
      case "dequeue":
        result.push(q.dequeue());
        break;
      case "size":
        result.push(q.size());
        break;
      case "empty":
        result.push(q.empty());
        break;
      case "front":
        result.push(q.front());
        break;
      case "back":
        result.push(q.back());
        break;
    }
  }

  return result;
}

input.forEach((x) => console.log(solution(x)));
/*
[ 1, 2, -1 ]
[ 3, 6, 3, 3, 0 ]
[
  7,  8, 2, 0,  7,
  8, -1, 0, 1, -1,
  0,  9
]
*/
