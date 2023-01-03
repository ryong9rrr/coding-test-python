const judgeValue = (index, n) => {
  const [a, b] = [Math.floor(index / n), index % n];
  return a < b ? b + 1 : a + 1;
};

function solution(n, left, right) {
  const length = right - left + 1;
  const slicedIndexArr = Array.from({ length }, (v, i) => i + left);
  return slicedIndexArr.map((index) => judgeValue(index, n));
}
// 정확성  테스트
// 테스트 1 〉	통과 (17.14ms, 44.3MB)
// 테스트 2 〉	통과 (12.32ms, 48.9MB)
// 테스트 3 〉	통과 (12.81ms, 48.8MB)
// 테스트 4 〉	통과 (0.32ms, 33.6MB)
// 테스트 5 〉	통과 (0.23ms, 33.4MB)
// 테스트 6 〉	통과 (15.39ms, 43MB)
// 테스트 7 〉	통과 (16.22ms, 42.9MB)
// 테스트 8 〉	통과 (12.22ms, 44.1MB)
// 테스트 9 〉	통과 (14.15ms, 45.2MB)
// 테스트 10 〉	통과 (21.22ms, 44.1MB)
// 테스트 11 〉	통과 (13.67ms, 45.1MB)
// 테스트 12 〉	통과 (15.73ms, 48.8MB)
// 테스트 13 〉	통과 (16.52ms, 47.9MB)
// 테스트 14 〉	통과 (21.57ms, 48.3MB)
// 테스트 15 〉	통과 (18.36ms, 49.9MB)
// 테스트 16 〉	통과 (18.83ms, 50.9MB)
// 테스트 17 〉	통과 (14.22ms, 47.5MB)
// 테스트 18 〉	통과 (15.52ms, 52.1MB)
// 테스트 19 〉	통과 (25.83ms, 49.7MB)
// 테스트 20 〉	통과 (19.71ms, 44.8MB)
