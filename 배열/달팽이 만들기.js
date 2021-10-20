let number = 4;

/*
let result = Array.from({ length: number }, (v) =>
  Array.from({ length: number }, (v) => 0)
);
*/
let result = [];
for (let i = 0; i < number; i++) {
  result[i] = [];
}

let direction = 1;
let num = 0;
let n = 0;
let m = -1;
while (true) {
  for (let i = 0; i < number; i++) {
    m += direction;
    result[n][m] = ++num;
  }

  number--;
  if (number == 0) break;

  for (let j = 0; j < number; j++) {
    n += direction;
    result[n][m] = ++num;
  }
  direction *= -1;
}

console.log(result);
/*
[
  [ 1, 2, 3, 4 ],
  [ 12, 13, 14, 5 ],
  [ 11, 16, 15, 6 ],
  [ 10, 9, 8, 7 ]
]
*/
