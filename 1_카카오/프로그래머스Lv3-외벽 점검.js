function permute(array, k) {
  if (k > array.length) return null
  const results = []
  prevElements = []
  function dfs(elements, k) {
    if (k === 0) {
      results.push([...prevElements])
      return
    }

    for (let i = 0; i < elements.length; i++) {
      nextElements = [...elements]
      nextElements.splice(i, 1)

      prevElements.push(elements[i])
      dfs(nextElements, k - 1)
      prevElements.pop()
    }
  }
  dfs(array, k)
  return results
}

function solution(n, weak, dist) {
  const W_LENGTH = weak.length
  const PEOPLE_LENGTH = dist.length
  const weaks = [...weak]
  weak.forEach((w) => weaks.push(w + n))

  const permutations = permute(dist, PEOPLE_LENGTH)

  let result = 999

  for (let i = 0; i < W_LENGTH; i++) {
    for (const people of permutations) {
      let count = 1
      let distance = weaks[i] + people[count - 1]
      for (let j = i; j < i + W_LENGTH; j++) {
        if (distance < weaks[j]) {
          count++
          if (count > PEOPLE_LENGTH) break
          distance = weaks[j] + people[count - 1]
        }
      }
      result = Math.min(result, count)
    }
  }

  return result > PEOPLE_LENGTH ? -1 : result
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.46ms, 33.4MB)
// 테스트 2 〉	통과 (0.44ms, 33.4MB)
// 테스트 3 〉	통과 (55.52ms, 49.3MB)
// 테스트 4 〉	통과 (48.44ms, 49.2MB)
// 테스트 5 〉	통과 (0.97ms, 33.5MB)
// 테스트 6 〉	통과 (16.18ms, 38.7MB)
// 테스트 7 〉	통과 (0.26ms, 33.5MB)
// 테스트 8 〉	통과 (0.70ms, 33.6MB)
// 테스트 9 〉	통과 (0.41ms, 33.4MB)
// 테스트 10 〉	통과 (53.86ms, 49.1MB)
// 테스트 11 〉	통과 (54.64ms, 49.2MB)
// 테스트 12 〉	통과 (55.32ms, 49.1MB)
// 테스트 13 〉	통과 (55.07ms, 49.2MB)
// 테스트 14 〉	통과 (60.96ms, 49.2MB)
// 테스트 15 〉	통과 (56.34ms, 49.2MB)
// 테스트 16 〉	통과 (51.57ms, 49.4MB)
// 테스트 17 〉	통과 (69.47ms, 49.1MB)
// 테스트 18 〉	통과 (70.08ms, 49MB)
// 테스트 19 〉	통과 (75.56ms, 49.2MB)
// 테스트 20 〉	통과 (51.45ms, 48.9MB)
// 테스트 21 〉	통과 (68.20ms, 49.3MB)
// 테스트 22 〉	통과 (0.68ms, 33.4MB)
// 테스트 23 〉	통과 (0.41ms, 33.4MB)
// 테스트 24 〉	통과 (0.48ms, 33.4MB)
// 테스트 25 〉	통과 (39.70ms, 49.2MB)
