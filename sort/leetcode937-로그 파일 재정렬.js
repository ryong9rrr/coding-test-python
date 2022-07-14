// 89ms
var reorderLogFiles = function (logs) {
  function isDigit(string) {
    return !Number.isNaN(Number(string))
  }

  function compare(a, b) {
    let i = 1
    while (a[i] && b[i]) {
      if (a[i] !== b[i]) {
        return (a[i] > b[i]) - (a[i] < b[i])
      } else i++
    }
    if (b[i]) return -1
    return (a[0] > b[0]) - (a[0] < b[0])
  }

  const d = []
  const l = []

  for (const log of logs) {
    const arr = log.split(' ')
    isDigit(arr[1]) ? d.push(log) : l.push(arr)
  }
  l.sort(compare)
  const sortedL = l.map((s) => s.join(' '))
  return [...sortedL, ...d]
}
