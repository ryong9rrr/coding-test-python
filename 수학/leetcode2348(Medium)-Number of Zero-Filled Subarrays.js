/**
 * @param {number[]} nums
 * @return {number}
 */
var zeroFilledSubarray = function (nums) {
  let ans = 0
  let acc = 0

  for (const num of nums) {
    if (num === 0) {
      acc += 1
    } else {
      acc = 0
    }
    ans += acc
  }

  return ans
}
