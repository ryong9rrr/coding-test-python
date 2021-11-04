const input = [
  [1, 5, 6, 7, 10, 12, 19, 29, 33],
  [25, 23, 11, 2, 18, 3, 28, 6, 37],
  [3, 37, 5, 36, 6, 22, 19, 2, 28],
];

function solution(array) {
  let faker = [];
  let sum = array.reduce((a, b) => a + b);

  const d = sum - 100;

  for (let i = 0; i < 9; i++) {
    for (let j = i + 1; j < 9; j++) {
      if (d - array[i] === array[j]) {
        faker.push(array[i], array[j]);
        break;
      }
    }
  }

  const result = array.filter((data) => data !== faker[0] && data !== faker[1]);

  return result;
}

input.forEach((data) => console.log(solution(data)));
/*
[
   1,  5,  6, 7,
  19, 29, 33
]
[
  23, 11,  2, 18,
   3,  6, 37
]
[
   3, 37,  5, 6,
  19,  2, 28
]
*/
