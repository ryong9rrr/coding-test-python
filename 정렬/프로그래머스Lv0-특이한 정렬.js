function solution(numlist, n) {
  return numlist.sort((a, b) => {
    // 만약 절대값이 같다면 더 큰 값을 앞에다 두기
    if (Math.abs(a - n) === Math.abs(b - n)) {
      return a < b ? 1 : -1
    }
    // 절대값 차이를 기준으로 오름차순 정렬
    return Math.abs(a - n) - Math.abs(b - n)
  })
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.15ms, 33.4MB)
// 테스트 2 〉	통과 (0.17ms, 33.5MB)
// 테스트 3 〉	통과 (0.14ms, 33.4MB)
// 테스트 4 〉	통과 (0.15ms, 33.5MB)
// 테스트 5 〉	통과 (0.06ms, 33.4MB)
// 테스트 6 〉	통과 (0.13ms, 33.5MB)
// 테스트 7 〉	통과 (0.03ms, 33.6MB)

// 이런것도 가능;;
function solution(numlist, n) {
  return numlist.sort((a, b) => Math.abs(a - n) - Math.abs(b - n) || b - a)
}
