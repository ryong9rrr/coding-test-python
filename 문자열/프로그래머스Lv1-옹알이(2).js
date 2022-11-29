const isPronounce = (targetWord) => {
  const BABY_WORDS = ["aya", "ye", "woo", "ma"];
  for (let i = 0; i < BABY_WORDS.length; i++) {
    const BABY_WORD = BABY_WORDS[i];
    const babyWordRegex = new RegExp(BABY_WORD, "g");
    targetWord = targetWord.replace(babyWordRegex, String(i));
    if (targetWord.includes(String(i).repeat(2))) {
      return false;
    }
  }
  return !Number.isNaN(Number(targetWord));
};

function solution(babbling) {
  let total = 0;
  for (const word of babbling) {
    if (isPronounce(word)) {
      total += 1;
    }
  }
  return total;
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.19ms, 33.5MB)
// 테스트 2 〉	통과 (0.22ms, 33.5MB)
// 테스트 3 〉	통과 (0.23ms, 33.5MB)
// 테스트 4 〉	통과 (0.23ms, 33.5MB)
// 테스트 5 〉	통과 (0.19ms, 33.5MB)
// 테스트 6 〉	통과 (0.20ms, 33.5MB)
// 테스트 7 〉	통과 (0.20ms, 33.4MB)
// 테스트 8 〉	통과 (0.18ms, 33.4MB)
// 테스트 9 〉	통과 (0.19ms, 33.5MB)
// 테스트 10 〉	통과 (0.19ms, 33.5MB)
// 테스트 11 〉	통과 (0.28ms, 33.4MB)
// 테스트 12 〉	통과 (0.34ms, 33.5MB)
// 테스트 13 〉	통과 (0.40ms, 33.5MB)
// 테스트 14 〉	통과 (0.37ms, 33.5MB)
// 테스트 15 〉	통과 (0.33ms, 33.5MB)
// 테스트 16 〉	통과 (0.39ms, 33.6MB)
// 테스트 17 〉	통과 (0.38ms, 33.6MB)
// 테스트 18 〉	통과 (0.35ms, 33.5MB)
// 테스트 19 〉	통과 (0.22ms, 33.5MB)
// 테스트 20 〉	통과 (0.29ms, 33.4MB)
