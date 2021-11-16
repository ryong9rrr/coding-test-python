const input = [
  "(a+b)",
  "(a*(b+c)+d)",
  "(a*(b+c)+d+(e)",
  "(a*(b+c)+d)+e)",
  "(a*(b+c)+d)+(e*(f+g))",
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

function solution(str) {
  let result = [];
  let stack = [];
  for (let i = 0; i < str.length; i++) {
    if (str[i] == "(") {
      stack.push(i);
    } else if (str[i] == ")") {
      if (stack.isEmpty()) {
        return [];
      }

      result.push([stack.pop(), i]);
    }
  }

  if (!stack.isEmpty()) {
    return [];
  }

  return result;
}

input.forEach((x) => console.log(solution(x)));
/*
[ [ 0, 4 ] ]
[ [ 3, 7 ], [ 0, 10 ] ]
[]
[]
[ [ 3, 7 ], [ 0, 10 ], [ 15, 19 ], [ 12, 20 ] ]
*/
