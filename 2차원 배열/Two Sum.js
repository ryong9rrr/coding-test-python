let array = [2, 7, 11, 15];
let number = 9;

// O(n^2)
let result1 = [];

for (let i = 0; i < array.length; i++) {
  for (let j = i + 1; j < array.length; j++) {
    if (array[i] + array[j] === number) {
      result1.push(i, j);
    }
  }
}

console.log(result1);
// [ 0, 1 ]

// O(n)
let map = {};
let result2 = [];

for (let i = 0; i < array.length; i++) {
  map[array[i]] = i;
  if (map[number - array[i]] != undefined) {
    result2.push(map[number - array[i]], i);
    break;
  }
}

console.log(result2);
// [ 0, 1 ]
