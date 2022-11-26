const getInclination = ([x1, y1], [x2, y2]) => {
  const dx = x2 - x1;
  const dy = y2 - y1;
  return dy / dx;
};

function solution(dots) {
  dots.sort((dotA, dotB) => dotA[0] - dotB[0]);
  const [a, b, c, d] = dots;
  const d1 = getInclination(a, b);
  const d2 = getInclination(c, d);
  return d2 === d1 ? 1 : 0;
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.10ms, 33.5MB)
// 테스트 2 〉	통과 (0.08ms, 33.6MB)
// 테스트 3 〉	통과 (0.13ms, 33.4MB)
// 테스트 4 〉	통과 (0.12ms, 33.5MB)
// 테스트 5 〉	통과 (0.11ms, 33.6MB)
// 테스트 6 〉	통과 (0.12ms, 33.6MB)
// 테스트 7 〉	통과 (0.11ms, 33.5MB)
// 테스트 8 〉	통과 (0.10ms, 33.4MB)
// 테스트 9 〉	통과 (0.09ms, 33.5MB)
// 테스트 10 〉	통과 (0.08ms, 33.5MB)
// 테스트 11 〉	통과 (0.08ms, 33.5MB)
