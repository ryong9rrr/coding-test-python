// 50ms(99%), 45MB(20%)

/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function (nums) {
  const n = nums.length
  const sums = []
  let acc = 0
  nums.forEach((num) => {
    acc += num
    sums.push(acc)
  })

  const maxSum = sums[n - 1]
  for (let i = 0; i < n; i += 1) {
    const left = sums[i] - nums[i]
    const right = maxSum - sums[i]
    if (left === right) {
      return i
    }
  }

  return -1
}
