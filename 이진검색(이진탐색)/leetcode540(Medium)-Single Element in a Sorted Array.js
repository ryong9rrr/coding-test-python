// 62ms(84.83%), 44.9MB(52.92%)
/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNonDuplicate = function (nums) {
  let left = 0
  let right = nums.length - 1

  while (left < right) {
    const mid = Math.floor((left + right) / 2)
    if (
      (mid % 2 === 1 && nums[mid] === nums[mid - 1]) ||
      (mid % 2 === 0 && nums[mid] === nums[mid + 1])
    ) {
      left = mid + 1
    } else {
      right = mid
    }
  }

  return nums[left]
}
