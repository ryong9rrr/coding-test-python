const getCount1 = (number) => {
  const binary = number.toString(2)
  return [...binary].filter((x) => x === '1').length
}

function solution(n) {
  const count1 = getCount1(n)

  while (n++) {
    if (getCount1(n) === count1) return n
  }
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.08ms, 33.5MB)
// 테스트 2 〉	통과 (0.05ms, 33.4MB)
// 테스트 3 〉	통과 (0.06ms, 33.4MB)
// 테스트 4 〉	통과 (0.06ms, 33.4MB)
// 테스트 5 〉	통과 (0.06ms, 33.4MB)
// 테스트 6 〉	통과 (0.05ms, 33.6MB)
// 테스트 7 〉	통과 (0.08ms, 33.6MB)
// 테스트 8 〉	통과 (0.05ms, 33.4MB)
// 테스트 9 〉	통과 (0.14ms, 33.5MB)
// 테스트 10 〉	통과 (0.13ms, 33.4MB)
// 테스트 11 〉	통과 (0.08ms, 33.4MB)
// 테스트 12 〉	통과 (0.06ms, 33.5MB)
// 테스트 13 〉	통과 (0.06ms, 33.5MB)
// 테스트 14 〉	통과 (0.05ms, 33.5MB)
// 효율성  테스트
// 테스트 1 〉	통과 (0.09ms, 33.4MB)
// 테스트 2 〉	통과 (0.06ms, 33.3MB)
// 테스트 3 〉	통과 (0.06ms, 33.4MB)
// 테스트 4 〉	통과 (0.05ms, 33.4MB)
// 테스트 5 〉	통과 (0.19ms, 33.1MB)
// 테스트 6 〉	통과 (0.08ms, 33.5MB)
