function solution(genres, plays) {
  const table = {}

  genres.forEach((genre, i) => {
    const play = plays[i]
    if (!table[genre]) {
      table[genre] = {
        total: 0,
        items: [],
      }
    }
    table[genre].total += play
    table[genre].items.push([i, play])
  })

  for (const genre in table) {
    table[genre].items.sort((a, b) => b[1] - a[1])
  }

  const sortedGenres = Object.entries(table).sort((a, b) => b[1].total - a[1].total)

  const result = sortedGenres.reduce((a, b) => {
    const array = b[1].items.filter((_, index) => index < 2).map((arr) => arr[0])
    return [...a, ...array]
  }, [])

  return result
}

/*
정확성  테스트
테스트 1 〉	통과 (0.22ms, 30.1MB)
테스트 2 〉	통과 (0.37ms, 30.2MB)
테스트 3 〉	통과 (0.31ms, 30.3MB)
테스트 4 〉	통과 (0.16ms, 30.1MB)
테스트 5 〉	통과 (0.46ms, 29.9MB)
테스트 6 〉	통과 (0.24ms, 30.2MB)
테스트 7 〉	통과 (0.39ms, 30.3MB)
테스트 8 〉	통과 (0.24ms, 30.1MB)
테스트 9 〉	통과 (0.17ms, 30.2MB)
테스트 10 〉	통과 (0.60ms, 30.2MB)
테스트 11 〉	통과 (0.19ms, 30MB)
테스트 12 〉	통과 (0.24ms, 30.1MB)
테스트 13 〉	통과 (0.70ms, 30.3MB)
테스트 14 〉	통과 (0.64ms, 30.2MB)
테스트 15 〉	통과 (0.47ms, 30.2MB)
*/
