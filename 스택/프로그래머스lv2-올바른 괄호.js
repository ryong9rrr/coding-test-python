function solution(s) {
  const stack = []

  for (const char of s) {
    if (char === '(') {
      stack.push(char)
      continue
    }

    if (stack.length === 0) return false
    if (stack.pop() !== '(') return false
  }

  if (stack.length > 0) return false
  return true
}

/*
정확성  테스트
테스트 1 〉	통과 (0.07ms, 29.9MB)
테스트 2 〉	통과 (0.05ms, 30.2MB)
테스트 3 〉	통과 (0.05ms, 30.1MB)
테스트 4 〉	통과 (0.06ms, 30.2MB)
테스트 5 〉	통과 (0.06ms, 30.1MB)
테스트 6 〉	통과 (0.05ms, 30.2MB)
테스트 7 〉	통과 (0.12ms, 30.1MB)
테스트 8 〉	통과 (0.12ms, 30.1MB)
테스트 9 〉	통과 (0.08ms, 30.1MB)
테스트 10 〉	통과 (0.05ms, 30.1MB)
테스트 11 〉	통과 (0.06ms, 30.1MB)
테스트 12 〉	통과 (0.07ms, 30.1MB)
테스트 13 〉	통과 (0.08ms, 30MB)
테스트 14 〉	통과 (0.08ms, 30.1MB)
테스트 15 〉	통과 (0.08ms, 30.1MB)
테스트 16 〉	통과 (0.08ms, 30.2MB)
테스트 17 〉	통과 (0.08ms, 30.3MB)
테스트 18 〉	통과 (0.13ms, 30MB)
효율성  테스트
테스트 1 〉	통과 (8.97ms, 35.4MB)
테스트 2 〉	통과 (7.19ms, 35.5MB)
*/

// 이 문제는 스택의 원리를 이용해서 변수 1개로 메모리를 절약하는 풀이가 가능하다.
function solution(s) {
  let acc = 0

  for (const char of [...s]) {
    if (char === '(') {
      acc++
      continue
    }
    if (acc === 0) {
      return false
    }
    acc--
  }

  return acc === 0
}

/*
정확성  테스트
테스트 1 〉	통과 (0.06ms, 30.3MB)
테스트 2 〉	통과 (0.05ms, 30.2MB)
테스트 3 〉	통과 (0.05ms, 30.2MB)
테스트 4 〉	통과 (0.05ms, 30.1MB)
테스트 5 〉	통과 (0.08ms, 30.1MB)
테스트 6 〉	통과 (0.08ms, 29.9MB)
테스트 7 〉	통과 (0.05ms, 30.1MB)
테스트 8 〉	통과 (0.08ms, 29.8MB)
테스트 9 〉	통과 (0.06ms, 30MB)
테스트 10 〉	통과 (0.05ms, 30.1MB)
테스트 11 〉	통과 (0.05ms, 30.1MB)
테스트 12 〉	통과 (0.09ms, 30.1MB)
테스트 13 〉	통과 (0.07ms, 29.9MB)
테스트 14 〉	통과 (0.07ms, 30.1MB)
테스트 15 〉	통과 (0.06ms, 30MB)
테스트 16 〉	통과 (0.06ms, 29.8MB)
테스트 17 〉	통과 (0.07ms, 30MB)
테스트 18 〉	통과 (0.06ms, 30.1MB)
효율성  테스트
테스트 1 〉	통과 (7.94ms, 35.6MB)
테스트 2 〉	통과 (10.14ms, 35.7MB)
*/
