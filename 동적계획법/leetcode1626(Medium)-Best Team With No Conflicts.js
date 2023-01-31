// 동적계획법 풀이 : O(N^2), 206ms(33.33%), 48.3MB(44.44%)
/**
 * @param {number[]} scores
 * @param {number[]} ages
 * @return {number}
 */
var bestTeamScore = function (scores, ages) {
  const N = scores.length

  // [age, score][]
  const pair = Array.from({ length: N }, (v, i) => i)
    .map((i) => [ages[i], scores[i]])
    .sort((a, b) => (a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]))

  const dp = pair.map(([_, score]) => score)

  for (let i = 0; i < N; i++) {
    const [_, curScore] = pair[i]
    for (let j = i - 1; j >= 0; j--) {
      const [_, prevScore] = pair[j]
      if (curScore >= prevScore) {
        dp[i] = Math.max(dp[i], curScore + dp[j])
      }
    }
  }

  return Math.max(...dp)
}

// 인덱스 트리(Fenwick Tree) : 89ms(100%), 47.4MB(55.56%)
/**
 * @param {number[]} scores
 * @param {number[]} ages
 * @return {number}
 */
var bestTeamScore = function (scores, ages) {
  const queryTree = (tree, age) => {
    let maxValue = -Infinity
    let i = age
    while (i > 0) {
      maxValue = Math.max(maxValue, tree[i])
      i -= i & -i
    }
    return maxValue
  }

  const updateTree = (tree, age, currentBest) => {
    i = age
    while (i < tree.length) {
      tree[i] = Math.max(tree[i], currentBest)
      i += i & -i
    }
  }

  const N = scores.length

  const scoreAgePair = Array.from({ length: N }, (v, i) => i)
    .map((i) => [scores[i], ages[i]])
    .sort((a, b) => (a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]))

  const highestAge = Math.max(...ages)
  const tree = new Array(highestAge + 1).fill(0)

  let answer = -Infinity
  scoreAgePair.forEach(([score, age]) => {
    const currentBest = score + queryTree(tree, age)

    updateTree(tree, age, currentBest)

    answer = Math.max(answer, currentBest)
  })

  return answer
}
