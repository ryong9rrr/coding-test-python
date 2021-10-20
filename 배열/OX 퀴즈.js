const input = [1, 0, 1, 1, 1, 0, 1, 1, 0, 0];

let result = 0;
let count = 0;

for (let i = 0; i < input.length; i++) {
  if (input[i] === 1) {
    result += ++count;
  } else {
    count = 0;
  }
}

console.log(result);
