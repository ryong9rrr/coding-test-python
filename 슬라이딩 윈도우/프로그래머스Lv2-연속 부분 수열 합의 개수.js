const sum = (arr) => arr.reduce((a, b) => a + b, 0)

function solution(elements) {
  const numbers = elements.concat(elements)

  const result = new Set()

  for (let size = 1; size < elements.length + 1; size++) {
    for (let i = 0; i < elements.length; i++) {
      result.add(sum(numbers.slice(i, i + size)))
    }
  }

  return [...result].length
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.13ms, 33.5MB)
// 테스트 2 〉	통과 (18.86ms, 39.4MB)
// 테스트 3 〉	통과 (37.87ms, 42.4MB)
// 테스트 4 〉	통과 (76.99ms, 42.5MB)
// 테스트 5 〉	통과 (126.09ms, 46.6MB)
// 테스트 6 〉	통과 (209.74ms, 46.6MB)
// 테스트 7 〉	통과 (338.81ms, 52.1MB)
// 테스트 8 〉	통과 (458.26ms, 51.8MB)
// 테스트 9 〉	통과 (611.47ms, 51.8MB)
// 테스트 10 〉	통과 (834.17ms, 53MB)
// 테스트 11 〉	통과 (164.80ms, 46.8MB)
// 테스트 12 〉	통과 (199.83ms, 46.6MB)
// 테스트 13 〉	통과 (247.13ms, 46.6MB)
// 테스트 14 〉	통과 (335.89ms, 51.8MB)
// 테스트 15 〉	통과 (397.66ms, 51.9MB)
// 테스트 16 〉	통과 (443.83ms, 51.8MB)
// 테스트 17 〉	통과 (538.65ms, 52.8MB)
// 테스트 18 〉	통과 (648.57ms, 51.9MB)
// 테스트 19 〉	통과 (759.79ms, 51.8MB)
// 테스트 20 〉	통과 (840.55ms, 53MB)
