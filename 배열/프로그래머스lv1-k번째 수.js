function solution(array, commands) {
  return commands.map(([i, j, k]) => {
    const arr = array.slice(i - 1, j).sort((a, b) => a - b)
    return arr[k - 1]
  })
}
// 정확성 테스트
// 테스트 1 〉 통과 (0.07ms, 33.5MB)
// 테스트 2 〉 통과 (0.08ms, 33.5MB)
// 테스트 3 〉 통과 (0.12ms, 33.6MB)
// 테스트 4 〉 통과 (0.11ms, 33.6MB)
// 테스트 5 〉 통과 (0.08ms, 33.4MB)
// 테스트 6 〉 통과 (0.07ms, 33.5MB)
// 테스트 7 〉 통과 (0.12ms, 33.5MB)
