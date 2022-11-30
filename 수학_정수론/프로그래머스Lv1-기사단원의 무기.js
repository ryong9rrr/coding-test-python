const getDivisors = (number) => {
  if (number <= 0) throw new Error("자연수가 아니에요.");
  const limit = Math.floor(Math.sqrt(number));
  const divisors = [];
  for (let left = 1; left < limit + 1; left++) {
    if (number % left === 0) {
      const right = number / left;
      divisors.push(left);
      if (left !== right) {
        divisors.push(right);
      }
    }
  }
  return divisors;
};

function solution(number, limit, power) {
  const people = Array.from({ length: number }, (_, i) => i + 1);

  const limitWeapon = (personNumber) => {
    const divisorCount = getDivisors(personNumber).length;
    return divisorCount > limit ? power : divisorCount;
  };

  return people.map(limitWeapon).reduce((a, b) => a + b);
}
// 정확성  테스트
// 테스트 1 〉	통과 (8.44ms, 38.2MB)
// 테스트 2 〉	통과 (3.17ms, 37.3MB)
// 테스트 3 〉	통과 (3.17ms, 37MB)
// 테스트 4 〉	통과 (3.39ms, 37.4MB)
// 테스트 5 〉	통과 (1.46ms, 36.9MB)
// 테스트 6 〉	통과 (8.96ms, 38.2MB)
// 테스트 7 〉	통과 (3.74ms, 37.2MB)
// 테스트 8 〉	통과 (3.58ms, 36.9MB)
// 테스트 9 〉	통과 (9.43ms, 38.1MB)
// 테스트 10 〉	통과 (1.93ms, 36.8MB)
// 테스트 11 〉	통과 (103.49ms, 40.5MB)
// 테스트 12 〉	통과 (109.34ms, 40.8MB)
// 테스트 13 〉	통과 (94.77ms, 40.6MB)
// 테스트 14 〉	통과 (98.23ms, 40.9MB)
// 테스트 15 〉	통과 (110.07ms, 40.6MB)
// 테스트 16 〉	통과 (132.77ms, 41.1MB)
// 테스트 17 〉	통과 (0.10ms, 33.4MB)
// 테스트 18 〉	통과 (105.99ms, 41.2MB)
// 테스트 19 〉	통과 (3.15ms, 37.1MB)
// 테스트 20 〉	통과 (3.68ms, 37.2MB)
// 테스트 21 〉	통과 (0.14ms, 33.4MB)
// 테스트 22 〉	통과 (0.11ms, 33.4MB)
// 테스트 23 〉	통과 (0.20ms, 33.4MB)
// 테스트 24 〉	통과 (107.02ms, 41.1MB)
// 테스트 25 〉	통과 (107.56ms, 40.8MB)
// 테스트 26 〉	통과 (2.08ms, 36.9MB)
// 테스트 27 〉	통과 (1.48ms, 36.9MB)
