// 길이가 동일한 배열 a, b를 오름차순 정렬
function compare(a, b) {
  for (let i = 0; i < a.length; i++) {
    if (a[i] === b[i]) {
      continue
    }
    return a[i] - b[i]
  }
}
