const makeCounter = (array) => {
  return array.reduce((result, item) => {
    if (!result[item]) {
      result[item] = 0;
    }
    result[item] += 1;
    return result;
  }, {});
};

function solution(k, tangerine) {
  const counter = Object.values(makeCounter(tangerine)).sort((a, b) => b - a);

  let result = 0;
  for (const count of counter) {
    if (k <= 0) {
      return result;
    }
    k -= count;
    result += 1;
  }
  return result;
}
// 정확성  테스트
// 테스트 1 〉	통과 (2.90ms, 37.2MB)
// 테스트 2 〉	통과 (3.08ms, 37.2MB)
// 테스트 3 〉	통과 (3.10ms, 37.2MB)
// 테스트 4 〉	통과 (4.63ms, 37.1MB)
// 테스트 5 〉	통과 (3.04ms, 37.1MB)
// 테스트 6 〉	통과 (3.18ms, 37.2MB)
// 테스트 7 〉	통과 (4.93ms, 37.1MB)
// 테스트 8 〉	통과 (3.76ms, 37.1MB)
// 테스트 9 〉	통과 (3.13ms, 37.2MB)
// 테스트 10 〉	통과 (4.03ms, 37.2MB)
// 테스트 11 〉	통과 (0.26ms, 33.4MB)
// 테스트 12 〉	통과 (0.08ms, 33.4MB)
// 테스트 13 〉	통과 (0.08ms, 33.5MB)
// 테스트 14 〉	통과 (0.09ms, 33.5MB)
// 테스트 15 〉	통과 (0.09ms, 33.6MB)
// 테스트 16 〉	통과 (0.08ms, 33.5MB)
// 테스트 17 〉	통과 (0.09ms, 33.6MB)
// 테스트 18 〉	통과 (0.08ms, 33.4MB)
// 테스트 19 〉	통과 (0.08ms, 33.6MB)
// 테스트 20 〉	통과 (0.09ms, 33.3MB)
// 테스트 21 〉	통과 (0.22ms, 33.4MB)
// 테스트 22 〉	통과 (0.53ms, 33.5MB)
// 테스트 23 〉	통과 (0.35ms, 33.6MB)
// 테스트 24 〉	통과 (0.68ms, 33.7MB)
// 테스트 25 〉	통과 (3.51ms, 36.5MB)
// 테스트 26 〉	통과 (14.88ms, 40.9MB)
// 테스트 27 〉	통과 (94.83ms, 63.6MB)
// 테스트 28 〉	통과 (41.94ms, 46.5MB)
// 테스트 29 〉	통과 (65.88ms, 50.1MB)
// 테스트 30 〉	통과 (93.64ms, 63.5MB)
// 테스트 31 〉	통과 (14.20ms, 37.4MB)
// 테스트 32 〉	통과 (15.77ms, 37.8MB)
// 테스트 33 〉	통과 (80.43ms, 53.7MB)
// 테스트 34 〉	통과 (74.89ms, 50.7MB)
