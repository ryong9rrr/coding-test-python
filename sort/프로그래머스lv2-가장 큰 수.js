function compare(a, b) {
  return Number(a + b) < Number(b + a) ? 1 : -1
}

function solution(numbers) {
  const nums = numbers
    .map((n) => String(n))
    .sort(compare)
    .join('')
  return nums[0] === '0' ? '0' : nums
}

// 정확성  테스트
// 테스트 1 〉	통과 (112.48ms, 39.7MB)
// 테스트 2 〉	통과 (63.04ms, 36.8MB)
// 테스트 3 〉	통과 (147.01ms, 46.1MB)
// 테스트 4 〉	통과 (4.26ms, 32.3MB)
// 테스트 5 〉	통과 (128.66ms, 38MB)
// 테스트 6 〉	통과 (87.31ms, 38.7MB)
// 테스트 7 〉	통과 (0.09ms, 30.1MB)
// 테스트 8 〉	통과 (0.11ms, 30.1MB)
// 테스트 9 〉	통과 (0.11ms, 30.2MB)
// 테스트 10 〉	통과 (0.10ms, 30.2MB)
// 테스트 11 〉	통과 (0.09ms, 30.2MB)
// 테스트 12 〉	통과 (0.06ms, 29.9MB)
// 테스트 13 〉	통과 (0.07ms, 30MB)
// 테스트 14 〉	통과 (0.13ms, 30.1MB)
// 테스트 15 〉	통과 (0.09ms, 30.1MB)
