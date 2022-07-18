// String.prototype.padStart(길이, 채우고 싶은 값)
// padStart는 왼쪽에 0을 채운다.
const bin = (number, n) => number.toString(2).padStart(n, 0)

const makeHash = (bin) => [...bin].map((str) => (str === '1' ? '#' : ' ')).join('')

function solution(n, arr1, arr2) {
  const iters = Array.from({ length: n }, (_, i) => i)
  return iters.map((i) => makeHash(bin(arr1[i] | arr2[i], n)))
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.29ms, 30.4MB)
// 테스트 2 〉	통과 (0.17ms, 30.1MB)
// 테스트 3 〉	통과 (0.14ms, 30.2MB)
// 테스트 4 〉	통과 (0.15ms, 30.1MB)
// 테스트 5 〉	통과 (0.13ms, 29.9MB)
// 테스트 6 〉	통과 (0.31ms, 30.1MB)
// 테스트 7 〉	통과 (0.29ms, 30.1MB)
// 테스트 8 〉	통과 (0.14ms, 30.1MB)
