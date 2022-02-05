/* 
얕은 복사

sort()는 원본 배열을 바꾸므로 원본 배열을 유지하고 싶을 때
*/
const sorted = (array, reverse = false) => {
  if (reverse) {
    return [...array].sort((a, b) => b - a);
  }
  return [...array].sort((a, b) => a - b);
};

const A = [1, 4, 2];

console.log(sorted(A)); // [1, 2, 4]
console.log(sorted(A, true)); // [4, 2, 1]
console.log(A); // [1, 4, 2]
