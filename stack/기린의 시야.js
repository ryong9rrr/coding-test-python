const input = [
  [10, 3, 7, 4, 12, 2],
  [7, 4, 12, 1, 13, 11, 12, 6],
  [20, 1, 19, 18, 15, 4, 6, 8, 3, 3],
];

if (!Array.prototype.peek) {
  Array.prototype.peek = function () {
    return this[this.length - 1];
  };
}

if (!Array.prototype.isEmpty) {
  Array.prototype.isEmpty = function () {
    return this.length == 0;
  };
}

function solution(array) {
  let result = 0;

  let stack = [];
  array.push(Number.MAX_SAFE_INTEGER);
  for (let i = 0; i < array.length; i++) {
    while (!stack.isEmpty() && stack.peek()["h"] < array[i]) {
      result += i - stack.pop()["i"] - 1;
    }
    stack.push({ h: array[i], i: i });
  }

  return result;
}

input.forEach((x) => console.log(solution(x)));
/*
5
6
30
*/
