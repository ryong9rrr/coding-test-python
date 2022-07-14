function solution(lottos, win_nums) {
  function rank(num) {
    switch (num) {
      case 6:
        return 1
        break
      case 5:
        return 2
        break
      case 4:
        return 3
        break
      case 3:
        return 4
        break
      case 2:
        return 5
        break
      default:
        return 6
        break
    }
  }

  let num = 0
  let unKnown = 0
  lottos.forEach((n) => {
    if (win_nums.indexOf(n) !== -1) {
      num++
    } else if (n === 0) {
      unKnown++
    }
  })
  let high = num + unKnown
  let low = num

  return [rank(high), rank(low)]
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.11ms, 30.1MB)
// 테스트 2 〉	통과 (0.11ms, 29.8MB)
// 테스트 3 〉	통과 (0.11ms, 30.1MB)
// 테스트 4 〉	통과 (0.11ms, 30MB)
// 테스트 5 〉	통과 (0.11ms, 29.9MB)
// 테스트 6 〉	통과 (0.07ms, 30MB)
// 테스트 7 〉	통과 (0.11ms, 29.9MB)
// 테스트 8 〉	통과 (0.11ms, 30MB)
// 테스트 9 〉	통과 (0.10ms, 30MB)
// 테스트 10 〉	통과 (0.12ms, 30MB)
// 테스트 11 〉	통과 (0.12ms, 30MB)
// 테스트 12 〉	통과 (0.11ms, 30.1MB)
// 테스트 13 〉	통과 (0.12ms, 29.9MB)
// 테스트 14 〉	통과 (0.08ms, 29.9MB)
// 테스트 15 〉	통과 (0.11ms, 30MB)

function solution(lottos, win_nums) {
  const SCORE = [6, 6, 5, 4, 3, 2, 1]
  const result = []

  //const win = lottos.filter(lotto => win_nums.find(n => n === lotto)).length;
  const win = lottos.filter((lotto) => win_nums.includes(lotto)).length
  const unknown = lottos.filter((lotto) => lotto === 0).length

  return [SCORE[win + unknown], SCORE[win]]
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.07ms, 30MB)
// 테스트 2 〉	통과 (0.12ms, 30MB)
// 테스트 3 〉	통과 (0.12ms, 30.1MB)
// 테스트 4 〉	통과 (0.10ms, 30.2MB)
// 테스트 5 〉	통과 (0.07ms, 30MB)
// 테스트 6 〉	통과 (0.07ms, 30MB)
// 테스트 7 〉	통과 (0.09ms, 30MB)
// 테스트 8 〉	통과 (0.10ms, 30MB)
// 테스트 9 〉	통과 (0.07ms, 30.2MB)
// 테스트 10 〉	통과 (0.09ms, 30.1MB)
// 테스트 11 〉	통과 (0.07ms, 30.1MB)
// 테스트 12 〉	통과 (0.07ms, 30.1MB)
// 테스트 13 〉	통과 (0.07ms, 30.1MB)
// 테스트 14 〉	통과 (0.08ms, 29.9MB)
// 테스트 15 〉	통과 (0.07ms, 29.8MB)
