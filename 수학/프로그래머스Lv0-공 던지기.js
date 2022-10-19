function solution(numbers, k) {
  k = (2 * (k - 1)) % numbers.length
  return numbers[k]
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.02ms, 33.5MB)
// 테스트 2 〉	통과 (0.03ms, 33.4MB)
// 테스트 3 〉	통과 (0.02ms, 33.5MB)
// 테스트 4 〉	통과 (0.03ms, 33.5MB)
// 테스트 5 〉	통과 (0.02ms, 33.5MB)
// 테스트 6 〉	통과 (0.03ms, 33.4MB)
// 테스트 7 〉	통과 (0.03ms, 33.5MB)
