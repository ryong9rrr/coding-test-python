function solution(numbers, target) {
  let count = 0

  const dfs = (index, total) => {
    if (index === numbers.length) {
      if (total === target) {
        count += 1
      }
      return
    }

    dfs(index + 1, total + numbers[index])
    dfs(index + 1, total - numbers[index])
  }

  dfs(0, 0)
  return count
}
// 정확성  테스트
// 테스트 1 〉	통과 (17.84ms, 31.8MB)
// 테스트 2 〉	통과 (24.77ms, 32.1MB)
// 테스트 3 〉	통과 (0.33ms, 29.7MB)
// 테스트 4 〉	통과 (1.05ms, 29.9MB)
// 테스트 5 〉	통과 (3.43ms, 31.4MB)
// 테스트 6 〉	통과 (0.47ms, 30MB)
// 테스트 7 〉	통과 (0.33ms, 30MB)
// 테스트 8 〉	통과 (2.00ms, 31.6MB)
