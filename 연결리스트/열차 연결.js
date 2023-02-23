const input = [
  [4, 7, 1, 10, 6],
  [3, 10, 6, 9, 11, 3, 4],
  [5, 8, 7, 3, 4, 1, 2, 7, 10, 7],
];

function Train(number) {
  this.number = number;
  this.next = null;
}

function LinkedLikst() {
  this.head = null;
}

LinkedLikst.prototype.printNode = function () {
  for (let node = this.head; node != null; node = node.next) {
    process.stdout.write(`${node.number} -> `);
  }
  console.log("null");
};

function solution(array) {
  let ll = new LinkedLikst();
  let current, prev;
  array.forEach((node, i) => {
    current = new Train(node);

    if (i === 0) {
      ll.head = current;
    } else {
      prev.next = current;
    }
    prev = current;
  });

  return ll;
}

input.forEach((x) => solution(x).printNode());
/*
4 -> 7 -> 1 -> 10 -> 6 -> null
3 -> 10 -> 6 -> 9 -> 11 -> 3 -> 4 -> null
5 -> 8 -> 7 -> 3 -> 4 -> 1 -> 2 -> 7 -> 10 -> 7 -> null
*/
