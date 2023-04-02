// 339ms(35.56%), 67MB(97%)
/**
 * @param {number[]} spells
 * @param {number[]} potions
 * @param {number} success
 * @return {number[]}
 */
var successfulPairs = function (spells, potions, success) {
  const dp = {}
  potions = potions.sort((a, b) => a - b)

  const search = (co) => {
    let left = 0
    let right = potions.length - 1
    while (left < right) {
      const mid = left + Math.floor((right - left) / 2)
      const num = potions[mid] * co
      if (num < success) {
        left = mid + 1
      } else {
        right = mid
      }
    }
    return left
  }

  return spells.map((spell) => {
    if (!dp[spell]) {
      const index = search(spell)
      const pairsCount =
        potions[index] * spell < success ? 0 : potions.length - index
      dp[spell] = pairsCount
    }
    return dp[spell]
  })
}
