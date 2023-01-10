// 순열 DFS
function permute(array, k) {
  if (k > array.length) return null
  const results = []
  const prevElements = []
  function dfs(elements, k) {
    if (k === 0) {
      results.push([...prevElements])
      return
    }

    for (let i = 0; i < elements.length; i++) {
      const nextElements = [...elements]
      nextElements.splice(i, 1)

      prevElements.push(elements[i])
      dfs(nextElements, k - 1)
      prevElements.pop()
    }
  }
  dfs(array, k)
  return results
}

function solution(k, dungeons) {
  let result = 0

  permute(dungeons, dungeons.length).forEach((dungeon) => {
    let count = 0
    let myP = k
    while (dungeon.length > 0 && myP > 0) {
      const [minP, p] = dungeon.pop()
      if (minP > myP) {
        continue
      }
      count += 1
      myP -= p
    }
    result = Math.max(result, count)
  })

  return result
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.27ms, 33.1MB)
// 테스트 2 〉	통과 (0.27ms, 33.3MB)
// 테스트 3 〉	통과 (0.75ms, 33.5MB)
// 테스트 4 〉	통과 (0.48ms, 33.6MB)
// 테스트 5 〉	통과 (2.64ms, 37.2MB)
// 테스트 6 〉	통과 (9.95ms, 39MB)
// 테스트 7 〉	통과 (32.22ms, 49.3MB)
// 테스트 8 〉	통과 (37.30ms, 48.9MB)
// 테스트 9 〉	통과 (0.51ms, 33.6MB)
// 테스트 10 〉	통과 (8.69ms, 39.4MB)
// 테스트 11 〉	통과 (0.27ms, 33.4MB)
// 테스트 12 〉	통과 (30.61ms, 48.9MB)
// 테스트 13 〉	통과 (45.06ms, 48.9MB)
// 테스트 14 〉	통과 (37.46ms, 49.4MB)
// 테스트 15 〉	통과 (38.02ms, 48.6MB)
// 테스트 16 〉	통과 (9.22ms, 39.3MB)
// 테스트 17 〉	통과 (31.76ms, 49MB)
// 테스트 18 〉	통과 (0.29ms, 33.5MB)
// 테스트 19 〉	통과 (0.49ms, 33.6MB)

// 백트래킹
function solution(k, dungeons) {
  const N = dungeons.length
  const visited = new Array(N).fill(0)
  let result = 0

  function dfs(myP, count) {
    result = Math.max(result, count)

    for (let i = 0; i < N; i += 1) {
      const [minP, p] = dungeons[i]
      if (myP >= minP && !visited[i]) {
        visited[i] = 1
        dfs(myP - p, count + 1)
        visited[i] = 0
      }
    }
  }

  dfs(k, 0)
  return result
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.21ms, 33.4MB)
// 테스트 2 〉	통과 (0.23ms, 33.4MB)
// 테스트 3 〉	통과 (0.22ms, 33.4MB)
// 테스트 4 〉	통과 (0.52ms, 33.6MB)
// 테스트 5 〉	통과 (19.79ms, 37.7MB)
// 테스트 6 〉	통과 (26.41ms, 37.9MB)
// 테스트 7 〉	통과 (53.80ms, 38MB)
// 테스트 8 〉	통과 (55.75ms, 38MB)
// 테스트 9 〉	통과 (0.21ms, 33.4MB)
// 테스트 10 〉	통과 (2.54ms, 37.7MB)
// 테스트 11 〉	통과 (0.20ms, 33.4MB)
// 테스트 12 〉	통과 (4.21ms, 38.2MB)
// 테스트 13 〉	통과 (0.63ms, 33.7MB)
// 테스트 14 〉	통과 (0.40ms, 33.5MB)
// 테스트 15 〉	통과 (0.35ms, 33.4MB)
// 테스트 16 〉	통과 (0.35ms, 33.6MB)
// 테스트 17 〉	통과 (0.34ms, 33.5MB)
// 테스트 18 〉	통과 (0.30ms, 33.4MB)
// 테스트 19 〉	통과 (0.29ms, 33.6MB)
