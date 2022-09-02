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

function solution(genres, plays) {
  const genreMap = new Map()

  genres
    .map((genre, i) => [genre, plays[i]])
    .forEach(([genre, play], id) => {
      const data = genreMap.get(genre) || { total: 0, songs: [] }
      genreMap.set(genre, {
        total: data.total + play,
        songs: [...data.songs, { id, play }],
      })
    })

  return [...genreMap.entries()]
    .sort((a, b) => b[1].total - a[1].total)
    .map(([_, { songs }]) => songs.sort((a, b) => b.play - a.play).slice(0, 2))
    .flatMap((songs) => songs)
    .map((songs) => songs.id)
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.37ms, 29.9MB)
// 테스트 2 〉	통과 (0.44ms, 30MB)
// 테스트 3 〉	통과 (0.39ms, 30.2MB)
// 테스트 4 〉	통과 (0.33ms, 30.2MB)
// 테스트 5 〉	통과 (0.49ms, 30.2MB)
// 테스트 6 〉	통과 (0.52ms, 30.3MB)
// 테스트 7 〉	통과 (0.46ms, 30.2MB)
// 테스트 8 〉	통과 (0.42ms, 30.1MB)
// 테스트 9 〉	통과 (0.54ms, 30.2MB)
// 테스트 10 〉	통과 (0.48ms, 29.9MB)
// 테스트 11 〉	통과 (0.44ms, 30.2MB)
// 테스트 12 〉	통과 (0.44ms, 30.2MB)
// 테스트 13 〉	통과 (0.45ms, 30MB)
// 테스트 14 〉	통과 (0.46ms, 29.9MB)
// 테스트 15 〉	통과 (0.37ms, 30.2MB)

// 마지막에 정렬하고 자르지 않는 것보다 바로바로 정렬하고 자르는 것이 더 빠른...?
function solution(genres, plays) {
  const genreMap = new Map()

  genres
    .map((genre, i) => [genre, plays[i]])
    .forEach(([genre, play], id) => {
      const data = genreMap.get(genre) || { total: 0, songs: [] }
      genreMap.set(genre, {
        total: data.total + play,
        songs: [...data.songs, { id, play }].sort((a, b) => b.play - a.play).slice(0, 2),
      })
    })

  return [...genreMap.entries()]
    .sort((a, b) => b[1].total - a[1].total)
    .flatMap((item) => item[1].songs)
    .map((songs) => songs.id)
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.33ms, 29.9MB)
// 테스트 2 〉	통과 (0.36ms, 30.1MB)
// 테스트 3 〉	통과 (0.32ms, 30.1MB)
// 테스트 4 〉	통과 (0.30ms, 30MB)
// 테스트 5 〉	통과 (0.46ms, 30.1MB)
// 테스트 6 〉	통과 (0.44ms, 30.1MB)
// 테스트 7 〉	통과 (0.39ms, 30MB)
// 테스트 8 〉	통과 (0.37ms, 30.1MB)
// 테스트 9 〉	통과 (0.35ms, 30.1MB)
// 테스트 10 〉	통과 (0.46ms, 30.3MB)
// 테스트 11 〉	통과 (0.33ms, 30.2MB)
// 테스트 12 〉	통과 (0.40ms, 30.2MB)
// 테스트 13 〉	통과 (0.33ms, 30.2MB)
// 테스트 14 〉	통과 (0.49ms, 30.1MB)
// 테스트 15 〉	통과 (0.38ms, 30.4MB)
