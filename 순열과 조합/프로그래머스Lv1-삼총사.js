function combine(array, k) {
  const results = []
  function dfs(elements, start, k) {
    if (k === 0) {
      results.push([...elements])
      return
    }
    for (let i = start; i < array.length; i++) {
      elements.push(array[i])
      dfs(elements, i + 1, k - 1)
      elements.pop()
    }
  }
  dfs([], 0, k)
  return results
}

function sum(array) {
  return array.reduce((a, b) => a + b, 0)
}

function solution(number) {
  const combis = combine(number, 3)
  let count = 0
  for (const numbers of combis) {
    if (sum(numbers) === 0) {
      count++
    }
  }
  return count
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.32ms, 33.6MB)
// 테스트 2 〉	통과 (0.21ms, 33.5MB)
// 테스트 3 〉	통과 (0.23ms, 33.5MB)
// 테스트 4 〉	통과 (0.27ms, 33.5MB)
// 테스트 5 〉	통과 (0.28ms, 33.5MB)
// 테스트 6 〉	통과 (0.29ms, 33.5MB)
// 테스트 7 〉	통과 (0.33ms, 33.5MB)
// 테스트 8 〉	통과 (0.33ms, 33.5MB)
// 테스트 9 〉	통과 (0.33ms, 33.6MB)
// 테스트 10 〉	통과 (0.33ms, 33.6MB)
// 테스트 11 〉	통과 (0.27ms, 33.5MB)
// 테스트 12 〉	통과 (0.28ms, 33.6MB)
// 테스트 13 〉	통과 (0.28ms, 33.5MB)
