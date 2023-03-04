// 81ms(84.34%), 50MB(6.2%)
/**
 * @param {number[]} nums
 * @param {number} minK
 * @param {number} maxK
 * @return {number}
 */
var countSubarrays = function (nums, minK, maxK) {
  let ans = 0

  let minPosition = -1
  let maxPosition = -1
  let leftBound = -1

  nums.forEach((num, i) => {
    if (num < minK || num > maxK) {
      leftBound = i
    }

    if (num === minK) {
      minPosition = i
    }

    if (num === maxK) {
      maxPosition = i
    }

    ans += Math.max(0, Math.min(minPosition, maxPosition) - leftBound)
  })

  return ans
}
