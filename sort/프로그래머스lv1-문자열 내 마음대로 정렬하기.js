// 첫번째 풀이
function solution(strings, n) {
  return strings.sort((a, b) => {
    if (a[n] == b[n]) {
      return (a > b) - (a < b)
    } else {
      return (a[n] > b[n]) - (a[n] < b[n])
    }
  })
}

// 또는
function solution(strings, n) {
  function compare(a, b) {
    if (a[n] == b[n]) {
      return (a > b) - (a < b)
    }
    return (a[n] > b[n]) - (a[n] < b[n])
  }
  return strings.sort(compare)
}
/*
정확성  테스트
테스트 1 〉	통과 (0.08ms, 29.8MB)
테스트 2 〉	통과 (0.09ms, 30.2MB)
테스트 3 〉	통과 (0.07ms, 29.9MB)
테스트 4 〉	통과 (0.07ms, 30MB)
테스트 5 〉	통과 (0.09ms, 30MB)
테스트 6 〉	통과 (0.08ms, 29.9MB)
테스트 7 〉	통과 (0.06ms, 30MB)
테스트 8 〉	통과 (0.07ms, 30MB)
테스트 9 〉	통과 (0.07ms, 30.1MB)
테스트 10 〉	통과 (0.08ms, 30MB)
테스트 11 〉	통과 (0.06ms, 30.1MB)
테스트 12 〉	통과 (0.11ms, 30.1MB)
*/

// 두번째 풀이
function solution(strings, n) {
  return strings.sort((a, b) => (a[n] == b[n] ? a.localeCompare(b) : a[n].localeCompare(b[n])))
}
