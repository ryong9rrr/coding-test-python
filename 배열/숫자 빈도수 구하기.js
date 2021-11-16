const input = [
  [129, 137],
  [1412, 1918],
  [4159, 9182],
];

function solution(array) {
  const a = array[0];
  const b = array[1];
  let result = Array.from({ length: 10 }, (v) => 0);
  let num = 0;
  for (let i = a; i <= b; i++) {
    num = i;
    while (num !== 0) {
      result[num % 10] += 1;
      num = parseInt(num / 10);
    }
  }

  return result;
}

input.forEach((x) => console.log(solution(x)));
/*
[
  1, 10, 2, 9, 1,
  1,  1, 1, 0, 1
]
[
  100, 614, 101, 101,
  189, 201, 201, 201,
  201, 119
]
[
  1503, 1527, 1503,
  1502, 2343, 2503,
  2512, 2512, 2505,
  1686
]
*/
