function solution(s) {
  const numbers = s.split(' ').map((str) => Number(str))
  return Math.min(...numbers) + ' ' + Math.max(...numbers)
}

/*
정확성  테스트
테스트 1 〉	통과 (0.08ms, 30.2MB)
테스트 2 〉	통과 (0.09ms, 30.1MB)
테스트 3 〉	통과 (0.06ms, 30.1MB)
테스트 4 〉	통과 (0.07ms, 30.1MB)
테스트 5 〉	통과 (0.26ms, 30.1MB)
테스트 6 〉	통과 (0.10ms, 30.2MB)
테스트 7 〉	통과 (0.06ms, 30.2MB)
테스트 8 〉	통과 (0.10ms, 30.2MB)
테스트 9 〉	통과 (0.07ms, 30.2MB)
테스트 10 〉	통과 (0.08ms, 30.2MB)
테스트 11 〉	통과 (0.06ms, 30.2MB)
테스트 12 〉	통과 (0.08ms, 30.2MB)
*/
