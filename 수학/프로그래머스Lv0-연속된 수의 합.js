function solution(num, total) {
  let x = (total - ((num * (num - 1) / 2))) / num
  const result = []
  for (let i = 0; i < num; i++){
      result.push(x++)
  }
  return result
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.05ms, 33.6MB)
// 테스트 2 〉	통과 (0.04ms, 33.4MB)
// 테스트 3 〉	통과 (0.04ms, 33.5MB)
// 테스트 4 〉	통과 (0.04ms, 33.5MB)
// 테스트 5 〉	통과 (0.06ms, 33.5MB)
// 테스트 6 〉	통과 (0.08ms, 33.5MB)
// 테스트 7 〉	통과 (0.04ms, 33.5MB)
// 테스트 8 〉	통과 (0.06ms, 33.5MB)
// 테스트 9 〉	통과 (0.09ms, 33.5MB)
// 테스트 10 〉	통과 (0.08ms, 33.6MB)