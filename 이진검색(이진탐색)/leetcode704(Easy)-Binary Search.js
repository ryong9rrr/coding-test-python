/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  let left = 0
  let right = nums.length - 1

  while (left < right) {
    const mid = left + Math.floor((right - left) / 2)
    const num = nums[mid]

    if (num < target) {
      left = mid + 1
    } else {
      right = mid
    }
  }

  return nums[left] === target ? left : -1
}
