function solution(numbers, target) {
  let count = 0

  function dfs(total, index) {
    if (index < numbers.length) {
      dfs(total + numbers[index], index + 1)
      dfs(total - numbers[index], index + 1)
      return
    } else if (index === numbers.length && total === target) {
      return count++
    }
  }

  dfs(0, 0)

  return count
}

// 정확성  테스트
// 테스트 1 〉	통과 (14.44ms, 32.7MB)
// 테스트 2 〉	통과 (13.42ms, 32MB)
// 테스트 3 〉	통과 (0.22ms, 30.4MB)
// 테스트 4 〉	통과 (1.30ms, 32.1MB)
// 테스트 5 〉	통과 (2.36ms, 31.9MB)
// 테스트 6 〉	통과 (0.36ms, 30.2MB)
// 테스트 7 〉	통과 (0.23ms, 30.2MB)
// 테스트 8 〉	통과 (1.90ms, 32MB)
