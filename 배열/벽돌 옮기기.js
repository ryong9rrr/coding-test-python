const input = [
  [5, 2, 4, 1, 7, 5],
  [12, 8, 10, 11, 9, 5, 8],
  [27, 14, 19, 11, 26, 25, 23, 15],
];

function solution(array) {
  let sum = array.reduce((a, b) => a + b);
  const avg = sum / array.length;
  let result = 0;
  array.forEach((x) => {
    if (Math.abs(x - avg) !== 0) {
      result += Math.abs(x - avg);
    }
  });
  return result / 2;
}

input.forEach((x) => console.log(solution(x)));
