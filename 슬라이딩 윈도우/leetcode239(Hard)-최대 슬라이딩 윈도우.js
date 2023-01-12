/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function (nums, k) {
  const windows = []
  const result = []

  for (let i = 0; i < nums.length; i++) {
    if (windows.length > 0 && i - windows[0] === k) {
      windows.shift()
    }

    while (windows.length > 0 && nums[windows[windows.length - 1]] <= nums[i]) {
      windows.pop()
    }

    windows.push(i)

    if (i + 1 >= k) {
      result.push(nums[windows[0]])
    }
  }

  return result
}
