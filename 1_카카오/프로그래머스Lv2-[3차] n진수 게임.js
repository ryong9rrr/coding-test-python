function solution(n, t, m, p) {
  let numbers = "0"
  for (let number = 1; number < t * m; number++) {
    numbers += number.toString(n).toUpperCase()
  }

  let result = ""
  let index = p - 1
  while (result.length < t) {
    result += numbers[index]
    index += m
  }
  return result
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.05ms, 33.6MB)
// 테스트 2 〉	통과 (0.13ms, 33.6MB)
// 테스트 3 〉	통과 (0.13ms, 33.3MB)
// 테스트 4 〉	통과 (0.14ms, 33.5MB)
// 테스트 5 〉	통과 (0.22ms, 33.5MB)
// 테스트 6 〉	통과 (0.24ms, 33.5MB)
// 테스트 7 〉	통과 (0.23ms, 33.6MB)
// 테스트 8 〉	통과 (0.20ms, 33.4MB)
// 테스트 9 〉	통과 (0.19ms, 33.4MB)
// 테스트 10 〉	통과 (0.20ms, 33.4MB)
// 테스트 11 〉	통과 (0.20ms, 33.4MB)
// 테스트 12 〉	통과 (0.20ms, 33.5MB)
// 테스트 13 〉	통과 (0.20ms, 33.6MB)
// 테스트 14 〉	통과 (26.10ms, 46.4MB)
// 테스트 15 〉	통과 (34.39ms, 46.3MB)
// 테스트 16 〉	통과 (26.07ms, 46.4MB)
// 테스트 17 〉	통과 (1.40ms, 33.8MB)
// 테스트 18 〉	통과 (0.93ms, 33.8MB)
// 테스트 19 〉	통과 (0.34ms, 33.7MB)
// 테스트 20 〉	통과 (0.76ms, 33.7MB)
// 테스트 21 〉	통과 (9.26ms, 38.6MB)
// 테스트 22 〉	통과 (2.37ms, 34.4MB)
// 테스트 23 〉	통과 (9.26ms, 39.1MB)
// 테스트 24 〉	통과 (19.61ms, 42.5MB)
// 테스트 25 〉	통과 (20.21ms, 41.7MB)
// 테스트 26 〉	통과 (4.63ms, 37.8MB)
