function solution(babbling) {
  let total = 0;
  const possibleWords = ["aya", "ye", "woo", "ma"];

  babbling.forEach((word) => {
    possibleWords.forEach((possibleWord) => {
      word = word.replace(possibleWord, " ");
    });
    if (word.trim() === "") {
      total += 1;
    }
  });

  return total;
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.18ms, 33.5MB)
// 테스트 2 〉	통과 (0.23ms, 33.5MB)
// 테스트 3 〉	통과 (0.21ms, 33.4MB)
// 테스트 4 〉	통과 (0.21ms, 33.5MB)
// 테스트 5 〉	통과 (0.23ms, 33.4MB)
// 테스트 6 〉	통과 (0.19ms, 33.5MB)
// 테스트 7 〉	통과 (0.19ms, 33.5MB)
// 테스트 8 〉	통과 (0.24ms, 33.5MB)
// 테스트 9 〉	통과 (0.18ms, 33.4MB)
// 테스트 10 〉	통과 (0.17ms, 33.6MB)
// 테스트 11 〉	통과 (0.16ms, 33.6MB)
// 테스트 12 〉	통과 (0.11ms, 33.5MB)
