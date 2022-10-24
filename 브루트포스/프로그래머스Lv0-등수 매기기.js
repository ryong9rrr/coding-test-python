// js에서는 딕셔너리로 변환하는 과정에서 Key가 문자열이되고, 
// 소수점까지 잘 처리가 안될 수 있어서 2로 나누는 평균이 아닌 그냥 안나누고 합으로 했음.
function solution(score) {
  const table = {}
  score.forEach(([a, b]) => {
      const key = a + b
      if (!table[key]) table[key] = 0
      table[key]++
  })
  
  const ranks = {}
  let acc = 0
  Object.keys(table)
      .sort((a, b) => parseInt(b, 10) - parseInt(a, 10))
      .forEach(_score => {
      if (acc === 0) ranks[_score] = 1
      else ranks[_score] = acc + 1
      acc += table[_score]
  })
  
  return score.map(([a, b]) => {
      const key = a + b
      return ranks[key]
  })
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.12ms, 33.4MB)
// 테스트 2 〉	통과 (0.34ms, 33.5MB)
// 테스트 3 〉	통과 (0.14ms, 33.6MB)
// 테스트 4 〉	통과 (0.15ms, 33.4MB)
// 테스트 5 〉	통과 (0.18ms, 33.5MB)
// 테스트 6 〉	통과 (0.12ms, 33.4MB)
// 테스트 7 〉	통과 (0.13ms, 33.4MB)
// 테스트 8 〉	통과 (0.15ms, 33.5MB)
// 테스트 9 〉	통과 (0.16ms, 33.4MB)
// 테스트 10 〉	통과 (0.13ms, 33.6MB)
// 테스트 11 〉	통과 (0.20ms, 33.5MB)
// 테스트 12 〉	통과 (0.13ms, 33.6MB)