// 66ms(88.5%), 44MB(66.9%)
/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function (nums) {
  let answer = 0
  let curFar = 0
  let curEnd = 0

  for (let index = 0; index < nums.length - 1; index += 1) {
    curFar = Math.max(curFar, index + nums[index])

    if (index === curEnd) {
      answer += 1
      curEnd = curFar
    }
  }

  return answer
}
