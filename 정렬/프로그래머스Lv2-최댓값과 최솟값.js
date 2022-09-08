function solution(s) {
  const numbers = s.split(' ').sort((a, b) => parseInt(a, 10) - parseInt(b, 10))
  return `${numbers[0]} ${numbers[numbers.length - 1]}`
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.09ms, 33.7MB)
// 테스트 2 〉	통과 (0.12ms, 33.6MB)
// 테스트 3 〉	통과 (0.05ms, 33.5MB)
// 테스트 4 〉	통과 (0.08ms, 33.7MB)
// 테스트 5 〉	통과 (0.12ms, 33.6MB)
// 테스트 6 〉	통과 (0.11ms, 33.7MB)
// 테스트 7 〉	통과 (0.05ms, 33.5MB)
// 테스트 8 〉	통과 (0.08ms, 33.6MB)
// 테스트 9 〉	통과 (0.06ms, 33.6MB)
// 테스트 10 〉	통과 (0.10ms, 33.6MB)
// 테스트 11 〉	통과 (0.06ms, 33.6MB)
// 테스트 12 〉	통과 (0.13ms, 33.6MB)
