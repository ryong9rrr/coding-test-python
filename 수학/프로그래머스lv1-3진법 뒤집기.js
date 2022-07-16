function solution(n) {
  const reversedThree = [...n.toString(3)].reverse().join('')

  return [...reversedThree].reverse().reduce((result, s, i) => {
    result += 3 ** i * parseInt(s, 10)
    return result
  }, 0)
}
// 정확성  테스트
// 테스트 1 〉	통과 (0.06ms, 30.1MB)
// 테스트 2 〉	통과 (0.06ms, 30.1MB)
// 테스트 3 〉	통과 (0.05ms, 30MB)
// 테스트 4 〉	통과 (0.06ms, 30.1MB)
// 테스트 5 〉	통과 (0.06ms, 30.1MB)
// 테스트 6 〉	통과 (0.09ms, 30.2MB)
// 테스트 7 〉	통과 (0.12ms, 30.1MB)
// 테스트 8 〉	통과 (0.06ms, 30.3MB)
// 테스트 9 〉	통과 (0.07ms, 30.1MB)
// 테스트 10 〉	통과 (0.06ms, 30.2MB)
