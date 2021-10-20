const input = [
  [1, 3, 7],
  [3, 1, 9, 6, 4],
  [6, 9, 7, 2, 1, 4, 3],
];

function File(number) {
  this.number = number;
  this.next = null;
}

function DoubleLinkedLikst() {
  this.head = null;
}

DoubleLinkedLikst.prototype.printNode = function () {
  for (let node = this.head; node != null; node = node.next) {
    process.stdout.write(`${node.number} -> `);
  }
  console.log("null");
};

DoubleLinkedLikst.prototype.makeFiles = function (files) {
  let current = this.head;
  let node;
  for (let i = 0; i < files.length; i++) {
    node = new File(files[i]);
    node.next = current;
    this.head = node;
    current = node;
  }
};

function solution(array) {
  let ll = new DoubleLinkedLikst();

  ll.makeFiles(array);

  let current = ll.head,
    prev = null,
    next;

  while (current != null) {
    next = current.next;
    current.next = prev;
    prev = current;
    current = next;
  }
  ll.head = prev;

  return ll;
}

input.forEach((x) => solution(x).printNode());
/*
1 -> 3 -> 7 -> null
3 -> 1 -> 9 -> 6 -> 4 -> null
6 -> 9 -> 7 -> 2 -> 1 -> 4 -> 3 -> null
*/
