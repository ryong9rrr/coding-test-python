const input = [
  [8, 2, 3],
  [10, 2, 3],
  [20, 5, 7],
];

function Node(data) {
  this.data = data;
  this.next = null;
}

function CircularLinkedList() {
  this.head = null;
}

function solution(array) {
  let result = [];
  let [n, m, k] = array;
  let cll = new CircularLinkedList();

  // 1. Circular Linked List 생성
  let current, prev;
  for (let i = 1; i <= n; i++) {
    current = new Node(i);

    if (i === 1) {
      cll.head = current;
    } else {
      prev.next = current;
    }

    prev = current;
  }
  current.next = cll.head;

  // 2. Start node 위치 설정
  current = cll.head;
  while (--m) {
    prev = current;
    current = current.next;
  }

  // 3. 후보자들 중 k만큼 움직이면서 제거
  let count;
  while (current.next != current) {
    result.push(current.data);
    prev.next = current.next;

    count = k;
    while (count--) {
      prev = current;
      current = current.next;
    }
  }

  // 4. node가 하나 남았을 때
  result.push(current.data);
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
