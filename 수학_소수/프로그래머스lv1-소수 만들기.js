function makePrimeNumbers(n) {
  const primeNumbers = Array.from({ length: n + 1 }, (v) => true)
  primeNumbers.splice(0, 2, false, false)
  for (let num = 2; num < Math.floor(Math.sqrt(n)) + 1; num++) {
    if (primeNumbers[num]) {
      for (let i = num * num; i < n + 1; i += num) {
        primeNumbers[i] = false
      }
    }
  }
  return primeNumbers
}

function combine(nums, k) {
  const results = []

  function dfs(elements, start, k) {
    if (k === 0) {
      results.push([...elements])
      return
    }

    for (let i = start; i < nums.length; i++) {
      elements.push(nums[i])
      dfs(elements, i + 1, k - 1)
      elements.pop()
    }
  }
  dfs([], 0, k)
  return results
}

function solution(nums) {
  const RANGE = [...nums]
    .sort((a, b) => b - a)
    .slice(0, 3)
    .reduce((a, b) => a + b)

  const primeNumbers = makePrimeNumbers(RANGE)
  const totalNumbers = combine(nums, 3).map((numbers) => numbers.reduce((a, b) => a + b))

  return totalNumbers.reduce((acc, cur) => (primeNumbers[cur] ? acc + 1 : acc), 0)
}

// 정확성  테스트
// 테스트 1 〉	통과 (1.54ms, 30.2MB)
// 테스트 2 〉	통과 (2.70ms, 33MB)
// 테스트 3 〉	통과 (0.72ms, 29.9MB)
// 테스트 4 〉	통과 (0.54ms, 30MB)
// 테스트 5 〉	통과 (2.67ms, 32.7MB)
// 테스트 6 〉	통과 (4.39ms, 33MB)
// 테스트 7 〉	통과 (0.63ms, 30MB)
// 테스트 8 〉	통과 (8.03ms, 34.6MB)
// 테스트 9 〉	통과 (0.99ms, 30.2MB)
// 테스트 10 〉	통과 (27.41ms, 34.5MB)
// 테스트 11 〉	통과 (0.46ms, 29.9MB)
// 테스트 12 〉	통과 (0.45ms, 30MB)
// 테스트 13 〉	통과 (0.47ms, 30.1MB)
// 테스트 14 〉	통과 (0.40ms, 30.1MB)
// 테스트 15 〉	통과 (0.47ms, 30.1MB)
// 테스트 16 〉	통과 (33.86ms, 34.2MB)
// 테스트 17 〉	통과 (13.39ms, 35.9MB)
// 테스트 18 〉	통과 (0.88ms, 29.8MB)
// 테스트 19 〉	통과 (0.87ms, 30.1MB)
// 테스트 20 〉	통과 (11.77ms, 35.8MB)
// 테스트 21 〉	통과 (12.36ms, 36.7MB)
// 테스트 22 〉	통과 (3.08ms, 33MB)
// 테스트 23 〉	통과 (0.39ms, 30.2MB)
// 테스트 24 〉	통과 (8.62ms, 34.7MB)
// 테스트 25 〉	통과 (10.58ms, 34.6MB)
// 테스트 26 〉	통과 (0.35ms, 30MB)
