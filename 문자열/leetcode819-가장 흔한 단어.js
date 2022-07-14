var mostCommonWord = function (paragraph, banned) {
  const regex = /[^\w]/g
  const counts = {}

  const words = paragraph.replace(regex, ' ').toLowerCase().split(' ')

  for (const word of words) {
    if (banned.includes(word) || word === '') continue
    if (!counts[word]) counts[word] = 0
    counts[word]++
  }

  const _max = Object.entries(counts).sort((a, b) => b[1] - a[1])

  return _max[0][0]
}
