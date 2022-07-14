/**
 * @param {string[][]} tickets
 * @return {string[]}
 */
var findItinerary = function (tickets) {
  tickets.sort()
  tickets.reverse()
  const dic = {}

  for (const [from, to] of tickets) {
    if (!dic[from]) {
      dic[from] = []
    }
    dic[from].push(to)
  }

  const result = []

  function dfs(path) {
    while (dic[path] && dic[path].length > 0) {
      dfs(dic[path].pop())
    }
    return result.push(path)
  }

  dfs('JFK')

  return result.reverse()
}
