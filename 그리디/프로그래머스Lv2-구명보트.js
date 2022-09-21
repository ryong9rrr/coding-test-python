function solution(people, limit) {
  people.sort((a, b) => a - b)

  let count = 0

  let left = 0
  let right = people.length - 1

  while (left <= right) {
    const weight = people[left] + people[right]
    if (weight <= limit) left++
    right--
    count++
  }

  return count
}
// 정확성  테스트
// 테스트 1 〉	통과 (3.27ms, 35.4MB)
// 테스트 2 〉	통과 (1.12ms, 33.6MB)
// 테스트 3 〉	통과 (1.49ms, 33.7MB)
// 테스트 4 〉	통과 (1.09ms, 33.5MB)
// 테스트 5 〉	통과 (1.14ms, 33.5MB)
// 테스트 6 〉	통과 (0.41ms, 33.6MB)
// 테스트 7 〉	통과 (0.63ms, 33.6MB)
// 테스트 8 〉	통과 (0.17ms, 33.5MB)
// 테스트 9 〉	통과 (0.21ms, 33.5MB)
// 테스트 10 〉	통과 (1.05ms, 33.5MB)
// 테스트 11 〉	통과 (0.95ms, 33.5MB)
// 테스트 12 〉	통과 (0.86ms, 33.5MB)
// 테스트 13 〉	통과 (1.05ms, 33.6MB)
// 테스트 14 〉	통과 (1.24ms, 33.8MB)
// 테스트 15 〉	통과 (0.22ms, 33.5MB)
// 효율성  테스트
// 테스트 1 〉	통과 (13.75ms, 38.2MB)
// 테스트 2 〉	통과 (13.26ms, 38.4MB)
// 테스트 3 〉	통과 (13.74ms, 38.1MB)
// 테스트 4 〉	통과 (11.89ms, 38.5MB)
// 테스트 5 〉	통과 (11.80ms, 38.1MB)
