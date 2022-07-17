function solution(numbers) {
  const SIZE = numbers.length
  const result = new Set()

  for (let i = 0; i < SIZE - 1; i++) {
    for (let j = i + 1; j < SIZE; j++) {
      const sum = numbers[i] + numbers[j]
      result.add(sum)
    }
  }

  return [...result].sort((a, b) => a - b)
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.05ms, 30MB)
// 테스트 2 〉	통과 (0.07ms, 30.1MB)
// 테스트 3 〉	통과 (0.07ms, 30.1MB)
// 테스트 4 〉	통과 (0.07ms, 29.9MB)
// 테스트 5 〉	통과 (0.10ms, 30MB)
// 테스트 6 〉	통과 (0.10ms, 29.8MB)
// 테스트 7 〉	통과 (0.45ms, 30.4MB)
// 테스트 8 〉	통과 (0.40ms, 30MB)
// 테스트 9 〉	통과 (0.34ms, 30.3MB)
