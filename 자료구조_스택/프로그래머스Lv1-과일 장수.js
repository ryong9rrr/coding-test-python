function solution(k, m, score) {
  score.sort((a, b) => b - a);
  let total = 0;
  for (let i = m - 1; i < score.length; i += m) {
    total += score[i] * m;
  }
  return total;
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.14ms, 33.4MB)
// 테스트 2 〉	통과 (0.08ms, 33.4MB)
// 테스트 3 〉	통과 (0.14ms, 33.5MB)
// 테스트 4 〉	통과 (0.05ms, 33.4MB)
// 테스트 5 〉	통과 (0.06ms, 33.5MB)
// 테스트 6 〉	통과 (14.21ms, 39.5MB)
// 테스트 7 〉	통과 (17.40ms, 37.8MB)
// 테스트 8 〉	통과 (2.75ms, 35.9MB)
// 테스트 9 〉	통과 (16.08ms, 37.8MB)
// 테스트 10 〉	통과 (13.05ms, 38.9MB)
// 테스트 11 〉	통과 (217.84ms, 83.2MB)
// 테스트 12 〉	통과 (217.17ms, 83.7MB)
// 테스트 13 〉	통과 (257.75ms, 83.5MB)
// 테스트 14 〉	통과 (214.68ms, 82.3MB)
// 테스트 15 〉	통과 (212.79ms, 82.4MB)
// 테스트 16 〉	통과 (0.05ms, 33.4MB)
// 테스트 17 〉	통과 (0.06ms, 33.4MB)
// 테스트 18 〉	통과 (0.15ms, 33.5MB)
// 테스트 19 〉	통과 (0.14ms, 33.4MB)
// 테스트 20 〉	통과 (0.15ms, 33.4MB)
// 테스트 21 〉	통과 (0.08ms, 33.4MB)
// 테스트 22 〉	통과 (0.08ms, 33.4MB)
// 테스트 23 〉	통과 (0.08ms, 33.4MB)
// 테스트 24 〉	통과 (0.05ms, 33.4MB)
