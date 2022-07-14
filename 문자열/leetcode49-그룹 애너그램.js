var groupAnagrams = function (strs) {
  const anagrams = {}

  for (const word of strs) {
    const key = [...word].sort().join('')

    if (!anagrams[key]) anagrams[key] = []
    anagrams[key].push(word)
  }

  return Object.values(anagrams)
}
